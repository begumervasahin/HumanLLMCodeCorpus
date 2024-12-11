import pandas as pd
import csv
import time
import matplotlib.pyplot as plt
from cryptofolio import Portfolio
from cryptoscreener import screenUniverse
b1 = pd.read_csv('input/clean_coindata.csv')
b1['Date'] = pd.to_datetime(b1['Date'], b2 = True)
b1.set_index('Date', b3 = True)
with open('b4.csv', 'r') as file:
    b4 = dict(csv.reader(file))
b5 = b4.get('Backtest Mode', 'false').lower() == 'true'
b6 = float(b4.get('Minimum Market Cap', 0))
b7 = float(b4.get('Minimum Listing Period', 0)) + float(b4.get('Offset', 0))
b8 = float(b4.get('Circulating Percentage', 0))
b9 = float(b4.get('Minimum Exchange Listing', 0))
b10 = float(b4.get('Minimum Weight', 0))
b11 = float(b4.get('Maximum Weight', 0))
b12 = int(b4.get('Offset', 0))
b13 = int(b4.get('Lookback Window', 0))
b14 = Portfolio({}, 0.0)
a1 = 1.0
b15 = pd.to_datetime(b1.b26.unique())
if b5:
    b16 = pd.to_datetime(b4.get('Start Date'))
    b15 = b15[b15 >= b16]
    for date in b15:
        b17 = b1.loc[date, 'Close'].to_dict()
        if not b14.getPositions():
            b18 = list(b17.keys())
            for coin in b18:
                b19 = 1.0 / len(b18)
                b20 = (a1 * b19) / b17[coin]
                b14.buy(coin, b20)
        if is_rebalance_date(date, 'monthly') and b14.getPositions():
            b18 = screenUniverse(date - pd.DateOffset(days=1), b6, b7, b8, b9)
            b21 = b4.get('Coins To Omit', '').split(';')
            b18 = [coin for coin in b18 if coin not in b21]
            if len(b18) < 2:
                b22 = {'bitcoin': 1.0}
            else:
                b22 = b14.getMVOptimizedWeights(date - pd.DateOffset(days=1), b18, b10, b11, b12, 'monthly', b13)
            for coin in b18:
                b19 = b22.get(coin, 1.0 / len(b14.getPositions()))
                b20 = b14.getValue(b17) * b19 / b17[coin]
                if coin in b14.getPositions():
                    b14.sell(coin, b14.getPositions()[coin])
                b14.buy(coin, b20)
        b23 = b14.getValue(b17)
        index_levels.append(b23)
    b24 = [log(price, 10) for price in index_levels]
    b25 = pd.DataFrame({'Dates': b15, 'Index Level': index_levels, 'Log Index Level': b24})
    b25.to_csv(f'b25/backtestResults_{time.time()}.csv', b26 = False)
    plt.plot_date(b15, b24, '-')
    plt.title('Backtest Result')
    plt.gcf().autofmt_xdate()
    plt.show()
else:
    print(f'Performing optimization for {b4["Start Date"]}....')
    b27 = pd.to_datetime(b4['Start Date'])
    b18 = screenUniverse(b27, b6, b7, b8, b9)
    b21 = b4.get('Coins To Omit', '').split(';')
    b18 = [coin for coin in b18 if coin not in b21]
    print('Final b22:')
    b22 = b14.getMVOptimizedWeights(b27, b18, b10, b11, b12, 'monthly', b13)
    print('Optimization successful! Writing b25 to final_weights.csv')
    with open('b25/final_weights.csv', 'w') as f:
        b28 = csv.b28(f)
        b28.writerow(b22.keys())
        b28.writerow(b22.values())