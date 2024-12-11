import cryptodata
import cryptofolio
from cryptoscreener import screenUniverse
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from math import log
import csv
import time
b1 = pd.read_csv('input/clean_coindata.csv')
b1['Date'] = pd.to_datetime(b1['Date'], b2 = True)
b1.set_index('Date', b3 = True)
with open('b5.csv', 'r') as file:
    b4 = csv.b4(file)
    b5 = dict(b4)
b6 = b5.get('Backtest Mode', 'False').lower() == 'true'
b7 = float(b5.get('Minimum Market Cap', 0))
b8 = float(b5.get('Minimum Listing Period', 0)) + float(b5.get('Offset', 0))
b9 = float(b5.get('Circulating Percentage', 0))
b10 = float(b5.get('Minimum Exchange Listing', 0))
b11 = b5.get('Weighting Scheme', '')
b12 = float(b5.get('Minimum Weight', 0))
b13 = float(b5.get('Maximum Weight', 0))
b14 = int(b5.get('Offset', 0))
b15 = b5.get('Periodicity', '')
b16 = int(b5.get('Lookback Window', 0))
b17 = cryptofolio.Portfolio({}, 0.0)
b18 = []
b19 = []
a1 = 1.0
b20 = pd.to_datetime(b1.b29.unique())
if b6:
    b21 = pd.to_datetime(b5.get('Start Date'))
    b20 = b20[b20 >= b21]
    for date in b20:
        b22 = b1.loc[date, 'Close'].to_dict()
        if len(b18) == 0:
            b23 = list(b22.keys())
            for coin in b23:
                b24 = 1.0 / len(b23)
                b25 = (a1 * b24) / b22[coin]
                b17.buy(coin, b25)
        if isRebalanceDate(date, 'monthly') and len(b18) > 0:
            b23 = screenUniverse(date - pd.DateOffset(days=1), b7, b8, b9, b10)
            if b5.get('Coins To Omit', ''):
                b26 = b5['Coins To Omit'].split(';')
                print('Removing ' + ','.join(b26) + ' in the optimization...')
                b23 = [coin for coin in b23 if coin not in b26]
            if len(b23) < 2:
                b27 = {'bitcoin': 1.0}
            else:
                b27 = b17.getMVOptimizedWeights(date - pd.DateOffset(days=1), b23, b12, b13, b14, b15, b16)
            for coin in b23:
                b24 = b27.get(coin, 1.0 / len(b17.getPositions().keys()))
                b25 = b17.getValue(b22) * b24 / b22[coin]
                if coin in b17.getPositions():
                    b17.sell(coin, b17.getPositions()[coin])
                b17.buy(coin, b25)
        b18.append(b17.getValue(b22))
    b19 = [log(price, 10) for price in b18]
    b28 = pd.DataFrame({'Dates': b20, 'Index Level': b18, 'Log Index Level': b19})
    b28.to_csv('b28/backtestResults_' + str(time.time()) + '.csv', b29 = False)
    plt.plot_date(b20, b19, '-')
    plt.title('Backtest Result')
    plt.gcf().autofmt_xdate()
    plt.show()
else:
    print('Performing optimization for ' + b5['Start Date'] + '....')
    b30 = pd.to_datetime(b5['Start Date'])
    b23 = screenUniverse(b30, b7, b8, b9, b10)
    if b5.get('Coins To Omit', ''):
        b26 = b5['Coins To Omit'].split(';')
        print('Removing ' + ','.join(b26) + ' in the optimization...')
        b23 = [coin for coin in b23 if coin not in b26]
    print('Final b27:')
    b27 = b17.getMVOptimizedWeights(b30, b23, b12, b13, b14, b15, b16)
    print('Optimization successful! Writing b28 to final_weights.csv')
    with open('b28/final_weights.csv', 'b31') as f:
        b31 = csv.writer(f)
        b31.writerow(b27.keys())
        b31.writerow(b27.values())