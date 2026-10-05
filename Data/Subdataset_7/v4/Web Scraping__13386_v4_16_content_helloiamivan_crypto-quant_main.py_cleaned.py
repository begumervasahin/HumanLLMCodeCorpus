import pandas as pd
import datetime
import matplotlib.pyplot as plt
import csv
import time
from cryptodata import read_clean_coindata
from cryptofolio import Portfolio
from cryptoscreener import screenUniverse
from math import log
b1 = read_clean_coindata('input/clean_coindata.csv')
def fonk1(date, freq):
    if freq.lower() == 'monthly':
        b2 = datetime.datetime(date.year, date.month, 1, 0, 0, 0)
        return b2 = = date
    else:
        pass
with open('b4.csv', 'r') as file:
    b3 = csv.b3(file)
    b4 = {row[0]: row[1] for row in b3}
b5 = b4['Backtest Mode'] == 'True'
b6 = float(b4['Minimum Market Cap'])
b7 = float(b4['Minimum Listing Period']) + float(b4['Offset'])
b8 = float(b4['Circulating Percentage'])
b9 = float(b4['Minimum Exchange Listing'])
b10 = b4['Weighting Scheme']
b11 = float(b4['Minimum Weight'])
b12 = float(b4['Maximum Weight'])
b13 = int(b4['Offset'])
b14 = b4['Periodicity']
b15 = int(b4['Lookback Window'])
b16 = []
a1 = 1.0
b17 = Portfolio({}, 0.0)
if b5:
    b18 = pd.to_datetime(b4['Start Date'])
    b19 = pd.to_datetime(b1['Date'].unique(), infer_datetime_format=True).sort_values(ascending=True).tolist()
    b20 = b19.b29(b18)
    b19 = b19[b20:]
    for date in b19:
        print(date)
        b21 = b1.loc[b1['Date'] == date, ['Coin', 'Close']].set_index('Coin')['Close'].to_dict()
        if not b16:
            b22 = list(b21.keys())
            for coin in b22:
                b23 = 1.0 / len(b22)
                b24 = (a1 * b23) / b21[coin]
                b17.buy(coin, b24)
        if fonk1(date, 'monthly') and b16:
            b22 = screenUniverse(date - pd.DateOffset(days=1), b6, b7,
                                      b8, b9)
            if b4['Coins To Omit']:
                b25 = b4['Coins To Omit'].split(';')
                print('Removing ' + ', '.join(b25) + ' in the optimization...')
                b22 = [coin for coin in b22 if coin not in b25]
            if len(b22) < 2:
                b26 = {'bitcoin': 1.0}
                print(b26)
            else:
                b26 = b17.getMVOptimizedWeights(date - pd.DateOffset(days=1), b22, b11,
                                                          b12, b13, b14, b15)
            for coin in b22:
                if b10 = = 'MeanVariance':
                    b23 = b26[coin]
                else:
                    b23 = 1.0 / len(b17.getPositions().keys())
                b24 = b17.getValue(b21) * b23 / b21[coin]
                if coin in b17.getPositions():
                    b17.sell(coin, b17.getPositions()[coin])
                b17.buy(coin, b24)
            b16.append(b17.getValue(b21))
    b27 = [log(price, 10) for price in b16]
    b28 = pd.DataFrame({'Dates': b19, 'Index Level': b16, 'Log Index Level': b27})
    b28.to_csv('b28/backtestResults_' + str(time.time()) + '.csv', b29 = False)
    plt.plot_date(b19, b27, '-')
    plt.title('Backtest Result')
    plt.gcf().autofmt_xdate()
    plt.show()
else:
    print('Performing optimization for ' + b4['Start Date'] + '....')
    b30 = pd.to_datetime(b4['Start Date'])
    b22 = screenUniverse(b30, b6, b7, b8,
                              b9)
    if b4['Coins To Omit']:
        b25 = b4['Coins To Omit'].split(';')
        print('Removing ' + ', '.join(b25) + ' in the optimization...')
        b22 = [coin for coin in b22 if coin not in b25]
    b26 = b17.getMVOptimizedWeights(b30, b22, b11, b12,
                                               b13, b14, b15)
    print('Final b26:')
    print(b26)
    with open('b28/final_weights.csv', 'w') as file:
        b31 = csv.b31(file)
        b31.writerow(b26.keys())
        b31.writerow(b26.values())