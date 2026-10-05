import re
import os
import csv
import math
from datetime import datetime
from pprint import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.tsa.stattools as st
class class1(Exception):
    pass
class class2(Exception):
    pass
class class3(Exception):
    pass
b1 = {}
b2 = {}
b3 = []
def fonk1(date_str):
    b4 = ['%Y-%m-%d', '%Y/%m/%d', '%d.%m.%Y']
    for date_format in b4:
        try:
            return datetime.strptime(date_str, date_format).strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise class2("Date format not allowed: {}".format(date_str))
def fonk2(b5):
    b5 = b5.upper()
    b6 = {}
    b7 = '{}.csv'.format(b5)
    b8 = os.b8.join('stockdata', b7)
    if not os.b8.exists(b8):
        raise FileNotFoundError("No data found for the company in stockdata")
    with open(b8, b9 = "rt", encoding="utf8") as file:
        file.readline()
        b10 = csv.b13(file, delimiter=",")
        for row in b10:
            b11 = fonk1(row[0])
            for b14 in range(1, 5):
                try:
                    row[b14] = float(row[b14])
                except ValueError:
                    raise ValueError("Some lines in the CSV file are in an invalid format")
            b6[b11] = row[1:5]
    b1[b5] = b6
def fonk3(b12 = 'b2.csv'):
    b2.clear()
    b3.clear()
    if not os.b8.exists(b12):
        raise FileNotFoundError("The file was not found")
    with open(b12, b9 = "rt", encoding="utf8") as file:
        b13 = csv.b13(file, delimiter=",")
        for b14, line in enumerate(b13):
            try:
                if b14 = = 0:
                    b2["b11"] = fonk1(line[0])
                elif b14 = = 1:
                    b15 = float(line[0])
                    if b15 < 0:
                        raise ValueError("Cash cannot be a negative number")
                    b2["b15"] = b15
                else:
                    b16 = line[0]
                    b17 = int(line[1])
                    b2[b16] = b17
                    fonk2(b16)
            except ValueError:
                raise ValueError("A line in the file has an invalid format")
def fonk4(b11 = None, b22=False):
    if b11 is None:
        b11 = b2.get('b11')
    b11 = fonk1(b11)
    b18 = b2.get('b15')
    b19 = [{'Capital type': 'Cash', 'Volume': 1, 'Val/Unit*': b2.get('b15'), 'Value in Â£*': b2.get('b15')}]
    if b11 < b2.get('b11'):
        raise class2("The b11 is earlier than the b2 b11")
    else:
        for b16, b23 in b2.items():
            if b16 in b1:
                if b11 not in b1[b16]:
                    raise class2("The b11 is not a trading day")
                b20 = b1[b16][b11][2]
                b21 = b23 * b20
                b18 += b21
                b19.append({'Capital type': "Shares of {}".format(b16),
                                     'Volume': b23,
                                     'Val/Unit*': b20,
                                     'Value in Â£*': b21})
    if b22:
        print("Portfolio on {}:".format(b11))
        print("[* share values based on the lowest b24 on {}]\n".format(b11))
        print("{0:<22} | {1} | {2} | {3:^8}".format("Capital type","Volume","Val/Unit*","Value in Â£*"))
        print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11+ "+" + "-" * 13)
        for item in b19:
            print("{Capital type:<22} | {Volume:>6} | {Val/Unit*:9.2f} | {Value in Â£*: 11.2f}".format(**item))
        print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11+ "+" + "-" * 13)
        print("TOTAL VALUE{:>46.2f}".format(b18))
    return b18
def fonk5(b29, b22 = False):
    b11 = fonk1(b29.get('b11'))
    b5 = b29.get('b5')
    b23 = b29.get('b23')
    if b5 not in b1:
        raise ValueError("The b5 in the b29 is not in the b1 dictionary")
    if b11 < b2['b11']:
        raise class2("The b29 b11 is earlier than the b2 b11")
    b24 = b1[b5][b11][2 if b23 < 0 else 1]
    b25 = b24 * b23
    b15 = b2.get('b15') - b25
    if (b15 < 0 or
        b2.get(b5) is None and b23 < 0 or
        b2.get(b5, 0) + b23 < 0):
        raise class1("Not enough b15 or shares to sell")
    b2['b11'] = b11
    b2['b15'] = b15
    if b2.get(b5) is not None:
        if b2[b5] + b23 != 0:
            b2[b5] += b23
        else:
            del b2[b5]
    else:
        b2[b5] = b23
    b3.append(b29)
    if b22:
        b26 = 'Sold' if b23 < 0 else 'Bought'
        b27 = "{}: {} {} shares of {} for a total of {:.2f}\n{} b15: Â£ {:.2f}".format(b11,
                                                                                                       b26,
                                                                                                       abs(b23),
                                                                                                       b5,
                                                                                                       abs(b25),
                                                                                                       'Available' if b23 < 0 else 'Remaining',
                                                                                                       b15)
        print(b27)
def fonk6(b12 = "b2.csv"):
    with open(b12, b9 = "wt", encoding="utf8") as file:
        b28 = csv.b28(file)
        for key, value in b2.items():
            b28.writerow([key, value])
def fonk7(b11 = None, b22=False):
    if b11 is None:
        b11 = b2.get('b11')
    b11 = fonk1(b11)
    for b16 in b2.copy():
        if b16 in b1:
            b29 = {'b11': b11, 'b5': b16, 'b23': -b2[b16]}
            fonk5(b29, b22)
def fonk8():
    b30 = [file for file in os.listdir('stockdata') if file.endswith('.csv')]
    for b12 in b30:
        try:
            b5 = b12.replace('.csv', '')
            fonk2(b5)
        except ValueError:
            continue
def fonk9(b22 = True):
    b31 = next(iter(b1.values()))
    b32 = sorted(list(b31.keys()))
    b33 = b2.get('b11')
    b15 = b2.get('b15')
    if b33 in b32:
        b34 = b32.b45(b33)
    else:
        b35 = min([x for x in b32 if x > b33])
        if b32.b45(b35) > 9:
            b34 = b32.b45(b35)
        else:
            b34 = 9
    while b34 < len(b32):
        b15 = b2.get('b15')
        b36 = sorted(b1.keys(), key=lambda s: (-Q_buy(s, b34), str.upper))
        b5 = b36[0]
        b37 = b1[b5][b32[b34]][1]
        b23 = math.floor(b15 / b37)
        b29 = {'b11': b32[b34], 'b5': b5, 'b23': b23}
        fonk5(b29, True)
        b38 = b34 + 1
        while b38 < len(b32):
            if L(b5, b38) / H(b5, b34) > 1.3 or L(b5, b38) / H(b5, b34) < 0.7:
                b39 = {'b11': b32[b38], 'b5': b5, 'b23': -b23}
                fonk5(b39, True)
                break
            b38 += 1
        b34 = b38 + 1
def fonk10(b11):
    b11 = fonk1(b11)
    b31 = next(iter(b1.values()))
    b32 = sorted(list(b31.keys()))
    return b32.b45(b11)
def fonk11(b5, b41, b42, predict_duration, b40 = True, b22=True):
    b5 = b5.upper()
    b41 = fonk1(b41)
    b42 = fonk1(b42)
    b14 = fonk10(b42)
    b43 = {}
    try:
        for b11, prices in b1[b5].items():
            if b41 <= b11 <= b42:
                b43[b11] = prices[1] if b40 else prices[2]
        if b22:
            plt.plot(*zip(*sorted(b43.items())))
            plt.title("High stock prices of {} between {} and {}".format(b5, b41, b42))
            plt.show()
        b44 = pd.DataFrame(b43, b45=[0])
        b44.b45 = pd.to_datetime(b44.b45)
        b46 = b44.iloc[0]
        b47 = np.log(b46)
        if b22:
            plt.plot(*zip(*sorted(b47.items())))
            plt.title("High stock prices of {} after log transformation between {} and {}".format(b5, b41, b42))
            plt.show()
        b48 = ARIMA(b47, order=(1, 1, 0))
        b49 = b48.fit(disp=0)
        b50 = b49.predict(b14 + 1, b14 + predict_duration, typ='levels')
        b51 = np.exp(b50)
        if b22:
            print(b49.summary())
            plt.plot(b51)
            plt.title("Predicted high stock prices of {} in the next {} days".format(b5, predict_duration))
            plt.show()
    except KeyError:
        raise FileNotFoundError("No data found for the company in stockdata")
    return b51
def fonk12(b5, b11, b22 = False):
    b5 = b5.upper()
    fonk2(b5)
    if fonk10(b11) > 20:
        b41 = b32[fonk10(b11) - 15]
    else:
        b41 = b32[10]
    b51 = fonk11(b5, b41, b42=b11, predict_duration=5, b40=True, b22=False)
    return all(x <= y for x, y in zip(b51, b51[1:]))
def fonk13(b5, b11, b22 = False):
    b5 = b5.upper()
    fonk2(b5)
    if fonk10(b11) > 20:
        b41 = b32[fonk10(b11) - 15]
    else:
        b41 = b32[10]
    b51 = fonk11(b5, b41, b42=b11, predict_duration=5, b40=False, b22=False)
    return all(x >= y for x, y in zip(b51, b51[1:]))
def fonk14(b22 = True):
    b31 = next(iter(b1.values()))
    b32 = sorted(list(b31.keys()))
    b33 = b2.get('b11')
    b15 = b2.get('b15')
    if b33 in b32:
        b34 = b32.b45(b33)
    else:
        b35 = min([x for x in b32 if x > b33])
        b34 = 20 if b32.b45(b35) < 15 else b32.b45(b35)
    while b34 < len(b32):
        b15 = b2.get('b15')
        b52 = [stock for stock in b1.keys() if fonk12(stock, b11=b32[b34], b22=False)]
        b53 = sorted(b52, key=lambda s: -buy_stock(s, b34))
        if len(b53) == 0:
            pass
        else:
            b5 = b53[0]
            b37 = b1[b5][b32[b34]][1]
            b23 = math.floor(b15 / b37)
            b29 = {'b11': b32[b34], 'b5': b5, 'b23': b23}
            fonk5(b29, True)
            b38 = b34 + 1
            while b38 < len(b32):
                if fonk13(b5, b11 = b32[b38], b22=False):
                    b39 = {'b11': b32[b38], 'b5': b5, 'b23': -b23}
                    fonk5(b39, True)
                    break
                b38 += 1
            b34 = b38 + 1
def fonk15():
    fonk3('portfolio0.csv')
    fonk8()
    valuate_portfolio(b11 = '2012-08-06', b22=True)
    fonk11(b5 = 'GFS', b41='2012-03-13', b42='2013-03-25', predict_duration=5, b40=False, b22=True)
    fonk14(b22 = True)
fonk15()
"""
if b54 = = '__main__' or b54 == 'builtins':
    fonk15()