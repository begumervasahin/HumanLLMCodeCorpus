import os
import csv
import math
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.tsa.stattools as st
class TransactionError(Exception):
    pass
class DateError(Exception):
    pass
class LinAlgError(Exception):
    pass
stocks = {}
portfolio = {}
transactions = []
def normalize_date(date_str):
    date_formats = ['%Y-%m-%d', '%Y/%m/%d', '%d.%m.%Y']
    for date_format in date_formats:
        try:
            return datetime.strptime(date_str, date_format).strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise DateError("Date format not allowed: {}".format(date_str))
def load_stock(symbol):
    symbol = symbol.upper()
    symbol_dict = {}
    symbol_file = '{}.csv'.format(symbol)
    path = os.path.join('stockdata', symbol_file)
    if not os.path.exists(path):
        raise FileNotFoundError("No data found for the company in stockdata")
    with open(path, mode="rt", encoding="utf8") as file:
        file.readline()
        data_reader = csv.reader(file, delimiter=",")
        for row in data_reader:
            date = normalize_date(row[0])
            for i in range(1, 5):
                try:
                    row[i] = float(row[i])
                except ValueError:
                    raise ValueError("Some lines in the CSV file are in an invalid format")
            symbol_dict[date] = row[1:5]
    stocks[symbol] = symbol_dict
def load_portfolio(filename='portfolio.csv'):
    portfolio.clear()
    transactions.clear()
    if not os.path.exists(filename):
        raise FileNotFoundError("The file was not found")
    with open(filename, mode="rt", encoding="utf8") as file:
        reader = csv.reader(file, delimiter=",")
        for i, line in enumerate(reader):
            try:
                if i == 0:
                    portfolio["date"] = normalize_date(line[0])
                elif i == 1:
                    cash = float(line[0])
                    if cash < 0:
                        raise ValueError("Cash cannot be a negative number")
                    portfolio["cash"] = cash
                else:
                    stock_symbol = line[0]
                    stock_volume = int(line[1])
                    portfolio[stock_symbol] = stock_volume
                    load_stock(stock_symbol)
            except ValueError:
                raise ValueError("A line in the file has an invalid format")
def evaluate_portfolio(date=None, verbose=False):
    if date is None:
        date = portfolio.get('date')
    date = normalize_date(date)
    total_value = portfolio.get('cash')
    total_stocks = [{'Capital type': 'Cash', 'Volume': 1, 'Val/Unit*': portfolio.get('cash'), 'Value in Â£*': portfolio.get('cash')}]
    if date < portfolio.get('date'):
        raise DateError("The date is earlier than the portfolio date")
    else:
        for stock_symbol, volume in portfolio.items():
            if stock_symbol in stocks:
                if date not in stocks[stock_symbol]:
                    raise DateError("The date is not a trading day")
                unit_price = stocks[stock_symbol][date][2]
                stock_value = volume * unit_price
                total_value += stock_value
                total_stocks.append({'Capital type': "Shares of {}".format(stock_symbol),
                                     'Volume': volume,
                                     'Val/Unit*': unit_price,
                                     'Value in Â£*': stock_value})
    if verbose:
        print("Portfolio on {}:".format(date))
        print("[* share values based on the lowest price on {}]\n".format(date))
        print("{0:<22} | {1} | {2} | {3:^8}".format("Capital type","Volume","Val/Unit*","Value in Â£*"))
        print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11+ "+" + "-" * 13)
        for item in total_stocks:
            print("{Capital type:<22} | {Volume:>6} | {Val/Unit*:9.2f} | {Value in Â£*: 11.2f}".format(**item))
        print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11+ "+" + "-" * 13)
        print("TOTAL VALUE{:>46.2f}".format(total_value))
    return total_value
def add_transaction(transaction, verbose=False):
    date = normalize_date(transaction.get('date'))
    symbol = transaction.get('symbol')
    volume = transaction.get('volume')
    if symbol not in stocks:
        raise ValueError("The symbol in the transaction is not in the stocks dictionary")
    if date < portfolio['date']:
        raise DateError("The transaction date is earlier than the portfolio date")
    price = stocks[symbol][date][2 if volume < 0 else 1]
    total_price = price * volume
    cash = portfolio.get('cash') - total_price
    if (cash < 0 or
        portfolio.get(symbol) is None and volume < 0 or
        portfolio.get(symbol, 0) + volume < 0):
        raise TransactionError("Not enough cash or shares to sell")
    portfolio['date'] = date
    portfolio['cash'] = cash
    if portfolio.get(symbol) is not None:
        if portfolio[symbol] + volume != 0:
            portfolio[symbol] += volume
        else:
            del portfolio[symbol]
    else:
        portfolio[symbol] = volume
    transactions.append(transaction)
    if verbose:
        transaction_type = 'Sold' if volume < 0 else 'Bought'
        transaction_info = "{}: {} {} shares of {} for a total of {:.2f}\n{} cash: Â£ {:.2f}".format(date,
                                                                                                       transaction_type,
                                                                                                       abs(volume),
                                                                                                       symbol,
                                                                                                       abs(total_price),
                                                                                                       'Available' if volume < 0 else 'Remaining',
                                                                                                       cash)
        print(transaction_info)
def save_portfolio(filename="portfolio.csv"):
    with open(filename, mode="wt", encoding="utf8") as file:
        writer = csv.writer(file)
        for key, value in portfolio.items():
            writer.writerow([key, value])
def sell_all(date=None, verbose=False):
    if date is None:
        date = portfolio.get('date')
    date = normalize_date(date)
    for stock_symbol in portfolio.copy():
        if stock_symbol in stocks:
            transaction = {'date': date, 'symbol': stock_symbol, 'volume': -portfolio[stock_symbol]}
            add_transaction(transaction, verbose)
def load_all_stocks():
    all_files = [file for file in os.listdir('stockdata') if file.endswith('.csv')]
    for filename in all_files:
        try:
            symbol = filename.replace('.csv', '')
            load_stock(symbol)
        except ValueError:
            continue
def trade_strategy_1(verbose=True):
    first_dict = next(iter(stocks.values()))
    trading_days = sorted(list(first_dict.keys()))
    begin_date = portfolio.get('date')
    cash = portfolio.get('cash')
    if begin_date in trading_days:
        j = trading_days.index(begin_date)
    else:
        closest_date = min([x for x in trading_days if x > begin_date])
        if trading_days.index(closest_date) > 9:
            j = trading_days.index(closest_date)
        else:
            j = 9
    while j < len(trading_days):
        cash = portfolio.get('cash')
        sorted_symbols = sorted(stocks.keys(), key=lambda s: (-Q_buy(s, j), str.upper))
        symbol = sorted_symbols[0]
        unit_value = stocks[symbol][trading_days[j]][1]
        volume = math.floor(cash / unit_value)
        transaction = {'date': trading_days[j], 'symbol': symbol, 'volume': volume}
        add_transaction(transaction, True)
        k = j + 1
        while k < len(trading_days):
            if L(symbol, k) / H(symbol, j) > 1.3 or L(symbol, k) / H(symbol, j) < 0.7:
                sell_transaction = {'date': trading_days[k], 'symbol': symbol, 'volume': -volume}
                add_transaction(sell_transaction, True)
                break
            k += 1
        j = k + 1
def trading_day_index(date):
    date = normalize_date(date)
    first_dict = next(iter(stocks.values()))
    trading_days = sorted(list(first_dict.keys()))
    return trading_days.index(date)
def predict_stock(symbol, start_date, end_date, predict_duration, buy=True, verbose=True):
    symbol = symbol.upper()
    start_date = normalize_date(start_date)
    end_date = normalize_date(end_date)
    i = trading_day_index(end_date)
    price_stocks = {}
    try:
        for date, prices in stocks[symbol].items():
            if start_date <= date <= end_date:
                price_stocks[date] = prices[1] if buy else prices[2]
        if verbose:
            plt.plot(*zip(*sorted(price_stocks.items())))
            plt.title("High stock prices of {} between {} and {}".format(symbol, start_date, end_date))
            plt.show()
        df = pd.DataFrame(price_stocks, index=[0])
        df.index = pd.to_datetime(df.index)
        ts = df.iloc[0]
        ts_log = np.log(ts)
        if verbose:
            plt.plot(*zip(*sorted(ts_log.items())))
            plt.title("High stock prices of {} after log transformation between {} and {}".format(symbol, start_date, end_date))
            plt.show()
        model = ARIMA(ts_log, order=(1, 1, 0))
        model_fit = model.fit(disp=0)
        predictions = model_fit.predict(i + 1, i + predict_duration, typ='levels')
        actual_predictions = np.exp(predictions)
        if verbose:
            print(model_fit.summary())
            plt.plot(actual_predictions)
            plt.title("Predicted high stock prices of {} in the next {} days".format(symbol, predict_duration))
            plt.show()
    except KeyError:
        raise FileNotFoundError("No data found for the company in stockdata")
    return actual_predictions
def price_increase(symbol, date, verbose=False):
    symbol = symbol.upper()
    load_stock(symbol)
    if trading_day_index(date) > 20:
        start_date = trading_days[trading_day_index(date) - 15]
    else:
        start_date = trading_days[10]
    actual_predictions = predict_stock(symbol, start_date, end_date=date, predict_duration=5, buy=True, verbose=False)
    return all(x <= y for x, y in zip(actual_predictions, actual_predictions[1:]))
def price_decrease(symbol, date, verbose=False):
    symbol = symbol.upper()
    load_stock(symbol)
    if trading_day_index(date) > 20:
        start_date = trading_days[trading_day_index(date) - 15]
    else:
        start_date = trading_days[10]
    actual_predictions = predict_stock(symbol, start_date, end_date=date, predict_duration=5, buy=False, verbose=False)
    return all(x >= y for x, y in zip(actual_predictions, actual_predictions[1:]))
def trade_strategy_2(verbose=True):
    first_dict = next(iter(stocks.values()))
    trading_days = sorted(list(first_dict.keys()))
    begin_date = portfolio.get('date')
    cash = portfolio.get('cash')
    if begin_date in trading_days:
        j = trading_days.index(begin_date)
    else:
        closest_date = min([x for x in trading_days if x > begin_date])
        j = 20 if trading_days.index(closest_date) < 15 else trading_days.index(closest_date)
    while j < len(trading_days):
        cash = portfolio.get('cash')
        increase_stock_list = [stock for stock in stocks.keys() if price_increase(stock, date=trading_days[j], verbose=False)]
        buy_stock_list = sorted(increase_stock_list, key=lambda s: -buy_stock(s, j))
        if len(buy_stock_list) == 0:
            pass
        else:
            symbol = buy_stock_list[0]
            unit_value = stocks[symbol][trading_days[j]][1]
            volume = math.floor(cash / unit_value)
            transaction = {'date': trading_days[j], 'symbol': symbol, 'volume': volume}
            add_transaction(transaction, True)
            k = j + 1
            while k < len(trading_days):
                if price_decrease(symbol, date=trading_days[k], verbose=False):
                    sell_transaction = {'date': trading_days[k], 'symbol': symbol, 'volume': -volume}
                    add_transaction(sell_transaction, True)
                    break
                k += 1
            j = k + 1
def main():
    load_portfolio('portfolio0.csv')
    load_all_stocks()
    evaluate_portfolio(date='2012-08-06', verbose=True)
    predict_stock(symbol='GFS', start_date='2012-03-13', end_date='2013-03-25', predict_duration=5, buy=False, verbose=True)
    trade_strategy_2(verbose=True)
if __name__ == "__main__":
    main()