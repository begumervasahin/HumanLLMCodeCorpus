import pandas as pd
import datetime
import matplotlib.pyplot as plt
import csv
import time
from cryptodata import read_clean_coindata
from cryptofolio import Portfolio
from cryptoscreener import screenUniverse
from math import log
coindata = read_clean_coindata('input/clean_coindata.csv')
def is_rebalance_date(date, freq):
    if freq.lower() == 'monthly':
        first_day_of_month = datetime.datetime(date.year, date.month, 1, 0, 0, 0)
        return first_day_of_month == date
    else:
        pass
with open('parameters.csv', 'r') as file:
    reader = csv.reader(file)
    parameters = {row[0]: row[1] for row in reader}
backtest_mode = parameters['Backtest Mode'] == 'True'
min_market_cap = float(parameters['Minimum Market Cap'])
minimum_listing_period = float(parameters['Minimum Listing Period']) + float(parameters['Offset'])
circulating_pct = float(parameters['Circulating Percentage'])
min_exchanges = float(parameters['Minimum Exchange Listing'])
weighting_scheme = parameters['Weighting Scheme']
min_weight = float(parameters['Minimum Weight'])
max_weight = float(parameters['Maximum Weight'])
return_freq = int(parameters['Offset'])
periodicity = parameters['Periodicity']
lookback = int(parameters['Lookback Window'])
index_level = []
initial_investment = 1.0
portfolio = Portfolio({}, 0.0)
if backtest_mode:
    start_backtest = pd.to_datetime(parameters['Start Date'])
    dates = pd.to_datetime(coindata['Date'].unique(), infer_datetime_format=True).sort_values(ascending=True).tolist()
    start_ptr = dates.index(start_backtest)
    dates = dates[start_ptr:]
    for date in dates:
        print(date)
        latest_prices = coindata.loc[coindata['Date'] == date, ['Coin', 'Close']].set_index('Coin')['Close'].to_dict()
        if not index_level:
            universe = list(latest_prices.keys())
            for coin in universe:
                weight = 1.0 / len(universe)
                quantity = (initial_investment * weight) / latest_prices[coin]
                portfolio.buy(coin, quantity)
        if is_rebalance_date(date, 'monthly') and index_level:
            universe = screenUniverse(date - pd.DateOffset(days=1), min_market_cap, minimum_listing_period,
                                      circulating_pct, min_exchanges)
            if parameters['Coins To Omit']:
                coins_to_remove = parameters['Coins To Omit'].split(';')
                print('Removing ' + ', '.join(coins_to_remove) + ' in the optimization...')
                universe = [coin for coin in universe if coin not in coins_to_remove]
            if len(universe) < 2:
                weights = {'bitcoin': 1.0}
                print(weights)
            else:
                weights = portfolio.getMVOptimizedWeights(date - pd.DateOffset(days=1), universe, min_weight,
                                                          max_weight, return_freq, periodicity, lookback)
            for coin in universe:
                if weighting_scheme == 'MeanVariance':
                    weight = weights[coin]
                else:
                    weight = 1.0 / len(portfolio.getPositions().keys())
                quantity = portfolio.getValue(latest_prices) * weight / latest_prices[coin]
                if coin in portfolio.getPositions():
                    portfolio.sell(coin, portfolio.getPositions()[coin])
                portfolio.buy(coin, quantity)
            index_level.append(portfolio.getValue(latest_prices))
    index_level_log = [log(price, 10) for price in index_level]
    results = pd.DataFrame({'Dates': dates, 'Index Level': index_level, 'Log Index Level': index_level_log})
    results.to_csv('results/backtestResults_' + str(time.time()) + '.csv', index=False)
    plt.plot_date(dates, index_level_log, '-')
    plt.title('Backtest Result')
    plt.gcf().autofmt_xdate()
    plt.show()
else:
    print('Performing optimization for ' + parameters['Start Date'] + '....')
    universe_selection_date = pd.to_datetime(parameters['Start Date'])
    universe = screenUniverse(universe_selection_date, min_market_cap, minimum_listing_period, circulating_pct,
                              min_exchanges)
    if parameters['Coins To Omit']:
        coins_to_remove = parameters['Coins To Omit'].split(';')
        print('Removing ' + ', '.join(coins_to_remove) + ' in the optimization...')
        universe = [coin for coin in universe if coin not in coins_to_remove]
    weights = portfolio.getMVOptimizedWeights(universe_selection_date, universe, min_weight, max_weight,
                                               return_freq, periodicity, lookback)
    print('Final weights:')
    print(weights)
    with open('results/final_weights.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(weights.keys())
        writer.writerow(weights.values())