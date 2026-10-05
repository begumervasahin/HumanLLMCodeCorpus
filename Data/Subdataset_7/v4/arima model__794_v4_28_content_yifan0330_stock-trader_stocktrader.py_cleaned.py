import re
import os
import csv
from datetime import datetime
import math
from pprint import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as st
from statsmodels.tsa.arima_model import ARIMA
class class1(Exception):
    pass
class class2(Exception):
    pass
class class3(Exception):
    pass
b1 = {}
b2 = {}
b3 = []
def fonk1(s):
    if re.search(r'^\d{1,2}\.\d{1,2}\.\d{4}$', s):
        b4 = datetime.strptime(s, '%d.%m.%Y')
    elif re.search(r'^\d{4}\-\d{1,2}\-\d{1,2}$', s):
        b4 = datetime.strptime(s, '%Y-%m-%d')
    elif re.search(r'^\d{4}\/\d{1,2}\/\d{1,2}$', s):
        b4 = datetime.strptime(s, '%Y/%m/%d')
    else:
        raise class2("Invalid b11 format: {0}".format(s))
    return b4.strftime("%Y-%m-%d")
def fonk2(b6):
    b5 = {}
    b6 = b6.upper()
    b7 = '{}.csv'.format(b6)
    b8 = os.b8.join('stockdata', b7)
    if os.b8.exists(b8) is False:
        raise FileNotFoundError("Stock data b29 not found in stockdata directory")
    else:
        with open(b8, b9 = "rt", encoding="utf8") as ifile:
            ifile.readline()
            b10 = csv.reader(ifile, delimiter=",")
            for row in b10:
                b11 = fonk1(row[0])
                for b14 in range(1, 5):
                    try:
                        row[b14] = float(row[b14])
                    except ValueError:
                        raise ValueError("Invalid format in CSV b29")
                b5[b11] = row[1:5]
        b1[b6] = b5
def fonk3(b12 = 'b2.csv'):
    b2.clear()
    b3.clear()
    if os.b8.exists(b12) is False:
        raise FileNotFoundError("Portfolio b29 not found")
    else:
        with open(b12, b9 = "rt", encoding="utf8") as f:
            b13 = csv.reader(f, delimiter=",")
            for b14, line in enumerate(b13):
                try:
                    if b14 = = 0:
                        b2["b11"] = fonk1(line[0])
                    if b14 = = 1:
                        b2["b24"] = float(line[0])
                        if b2["b24"] < 0:
                            raise ValueError("Cash cannot be negative")
                    if b14 >= 2:
                        b2[line[0]] = int(line[1])
                        fonk2(line[0])
                except ValueError:
                    raise ValueError("Invalid format in b2 b29")
def fonk4(b11 = None, b21=False):
    if b11 is None:
        b11 = b2.get('b11')
    b11 = fonk1(b11)
    b15 = []
    b15.append({'Capital type': 'Cash', 'Volume': 1, 'Val/Unit*': b2.get('b24'), 'Value in £*': b2.get('b24')})
    b16 = b2.get('b24')
    if b11 < b2.get('b11'):
        raise class2("Date cannot be earlier than b2 b11")
    else:
        for stock in b2.keys():
            if stock in b1.keys():
                b17 = {}
                b17["Capital type"] = "Shares of {}".format(stock)
                b18 = b2.get(stock)
                b17["Volume"] = b18
                if b11 not in b1[stock].keys():
                    raise class2("Date is not a trading day")
                else:
                    b19 = b1[stock][b11][2]
                    b17["Val/Unit*"] = b19
                    b20 = b18 * b19
                    b17["Value in £*"] = b20
                    b16 += b20
                    b15.append(b17)
        if b21:
            print("Portfolio on {}:".format(b11))
            print("[* share values based on the lowest b22 on {}]\n".format(b11))
            print("{0:<22} | {1} | {2} | {3:^8}".format("Capital type", "Volume", "Val/Unit*", "Value in £*"))
            print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11 + "+" + "-" * 13)
            for item in b15:
                print("{Capital type:<22} | {Volume:>6} | {Val/Unit*:9.2f} | {Value in £*: 11.2f}".format(**item))
            print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11 + "+" + "-" * 13)
            print("TOTAL VALUE{:>46.2f}".format(b16))
        return b16
def fonk5(b38, b21 = False):
    b11 = fonk1(b38.get('b11'))
    b6 = b38.get('b6')
    b18 = b38.get('b18')
    if b6 not in b1.keys():
        raise ValueError("Symbol not found in stock data")
    if b11 < b2['b11']:
        raise class2("Transaction b11 cannot be earlier than b2 b11")
    b22 = b1[b6][b11][2 if b18 < 0 else 1]
    b23 = b22 * b18
    b24 = b2.get('b24') - b23
    if (b24 < 0 or
       b2.get(b6) is None and b18 < 0 or
       b2.get(b6) is not None and b2.get(b6) + b18 < 0):
        raise class1("Not enough b24 or shares to perform transaction")
    b2['b11'] = b11
    b2['b24'] = b24
    if b2.get(b6) is not None:
        if b2.get(b6) + b18 != 0:
            b2[b6] = b2.get(b6) + b18
        else:
            del b2[b6]
    else:
        b2[b6] = b18
    b3.append(b38)
    if b21:
        b25 = "{}: {} {} shares of {} for a total of {} \n{} b24: £ {:.2f}".format(b11, 'Sold' if b18<0 else 'Bought',
                                                                                                  abs(b18), b6, abs(b23),
                                                                                                  'Available' if b18<0 else 'Remaining', b24)
        print(b25)
    return
def fonk6(b12 = "b2.csv"):
    with open(b12, b9 = "wt", encoding="utf8") as csv_file:
        b26 = csv.writer(csv_file)
        for key, b20 in b2.items():
            b26.writerow([key, b20])
def fonk7(b11 = None, b21=False):
    if b11 is None:
        b11 = b2.get('b11')
    b11 = fonk1(b11)
    for key in b2.copy():
        if key in b1.keys():
            b27 = {'b11': b11, 'b6': key, 'b18': -b2[key]}
            fonk17(b27, b21)
    return
def fonk8():
    b28 = [b29 for b29 in os.listdir('stockdata') if os.b8.isfile(os.b8.join('stockdata', b29)) and re.search('\.csv', b29)]
    for b29 in b28:
        try:
            b29 = re.sub('\.csv$', '', b29)
            fonk2(b29)
        except ValueError:
            pass
    return
def fonk9(b21 = True):
    b30 = next(iter(b1.values()))
    b31 = list(b30.keys())
    b32 = b2.get('b11')
    b24 = b2.get('b24')
    if b32 in b31:
        b33 = b31.index(b32)
    else:
        b34 = min([x for x in b31 if x > b32])
        if b31.index(b34) > 9:
            b33 = b31.index(b34)
        else:
            b33 = 9
    while b33 < len(b31):
        b24 = b2.get('b24')
        b35 = sorted(b1.keys(), key=lambda s: (-fonk10(s, b33), str.upper))
        for b36 in b35:
            print(b36, fonk10(b36, b33))
        b36 = b35[0]
        b19 = b1[b36][b31[b33]][1]
        b37 = math.floor(b24 / b19)
        b38 = {'b11': b31[b33], 'b6': b36, 'b18': b37}
        fonk17(b38, True)
        b39 = b33 + 1
        while b39 < len(b31):
            if fonk12(b36, b39) / fonk11(b36, b33) > 1.3 or fonk12(b36, b39) / fonk11(b36, b33) < 0.7:
                b40 = {'b11': b31[b39], 'b6': b36, 'b18': -b37}
                fonk17(b40, True)
                break
            b39 += 1
        b33 = b39 + 1
    return
def fonk10(s, b33):
    if b33 >= 9:
        a1 = 0
        for b14 in range(0, 10):
            a1 += fonk11(s, b33 - b14)
        b41 = 10 * fonk11(s, b33) / a1
    else:
        b41 = 0
    return b41
def fonk11(s, b33):
    b30 = next(iter(b1.values()))
    b31 = list(b30.keys())
    b42 = b31[b33]
    b43 = b1.get(s).get(b42)[1]
    return b43
def fonk12(s, b33):
    b30 = next(iter(b1.values()))
    b31 = list(b30.keys())
    b42 = b31[b33]
    b44 = b1.get(s).get(b42)[2]
    return b44
def fonk13(b21 = True):
    b30 = next(iter(b1.values()))
    b31 = list(b30.keys())
    b32 = b2.get('b11')
    b24 = b2.get('b24')
    if b32 in b31:
        b33 = b31.index(b32)
    else:
        b34 = min([x for x in b31 if x > b32])
        if b31.index(b34) < 15:
            b33 = 20
        else:
            b33 = b31.index(b34)
    while b33 < len(b31):
        b24 = b2.get('b24')
        b45 = []
        for stock in b1.keys():
            if fonk14(stock, b11 = b31[b33], b21=False):
                b45.append(stock)
        b46 = sorted(b45, key=lambda s: -fonk15(s, b33))
        if len(b46) == 0:
            pass
        else:
            b36 = b46[0]
            b19 = b1[b36][b31[b33]][1]
            b37 = math.floor(b24 / b19)
            b38 = {'b11': b31[b33], 'b6': b36, 'b18': b37}
            fonk17(b38, True)
            b39 = b33 + 30
            while b39 < len(b31):
                if fonk16(b36, b11 = b31[b39], b21=False):
                    b40 = {'b11': b31[b39], 'b6': b36, 'b18': -b37}
                    fonk17(b40, True)
                    break
                b39 += 1
            b33 = b39 + 20
    return
def fonk14(b6, b11, b21 = False):
    b6 = b6.upper()
    fonk2(b6)
    b30 = next(iter(b1.values()))
    b31 = list(b30.keys())
    if trading_day_index(b11) > 20:
        b47 = b31[trading_day_index(b11) - 15]
    else:
        b47 = b31[10]
    b48 = predict_stock(b6, b47, end_date=b11, predict_duration=5, buy=True, b21=False)
    if all(x <= y for x, y in zip(b48, b48[1:])):
        return True
    else:
        return False
def fonk15(b6, b33):
    b6 = b6.upper()
    fonk2(b6)
    b30 = next(iter(b1.values()))
    b31 = list(b30.keys())
    b11 = b31[b33]
    if trading_day_index(b11) > 20:
        b47 = b31[trading_day_index(b11) - 15]
    else:
        b47 = b31[10]
    b11 = b31[b33]
    b48 = predict_stock(b6, b47, end_date=b11, predict_duration=5, buy=True, b21=False)
    b49 = float(b48[4]) - float(b48[0])
    return b49
def fonk16(b6, b11, b21 = False):
    b6 = b6.upper()
    fonk2(b6)
    b30 = next(iter(b1.values()))
    b31 = list(b30.keys())
    if trading_day_index(b11) > 20:
        b47 = b31[trading_day_index(b11) - 15]
    else:
        b47 = b31[10]
    b48 = predict_stock(b6, b47, end_date=b11, predict_duration=5, buy=False, b21=False)
    if all(x >= y for x, y in zip(b48, b48[1:])):
        return True
    else:
        return False
def fonk17(b38, b21 = False):
    b11 = fonk1(b38.get('b11'))
    b6 = b38.get('b6')
    b18 = b38.get('b18')
    if b6 not in b1.keys():
        raise ValueError("The b6 in transaction is not in b1 dictionary")
    if b11 < b2['b11']:
        raise class2("The b11 of transaction is earlier than that of b2")
    b22 = b1[b6][b11][2 if b18 < 0 else 1]
    b23 = b22 * b18
    b24 = b2.get('b24') - b23
    if (b24 < 0 or
        b2.get(b6) is None and b18 < 0 or
        b2.get(b6) is not None and b2.get(b6) + b18 < 0):
        raise class1("Not enough b24 or Not enough shares to sell")
    b2['b11'] = b11
    b2['b24'] = b24
    if b2.get(b6) is not None:
        if b2.get(b6) + b18 != 0:
            b2[b6] = b2.get(b6) + b18
        else:
            del b2[b6]
    else:
        b2[b6] = b18
    b3.append(b38)
    if b21:
        b50 = [b11, 'Sold' if b18 < 0 else 'Bought', abs(b18), b6, abs(b23), 'Available' if b18 < 0 else 'Remaining', b24]
        b51 = "{}: {} {} shares of {} for a total of {} \n{} b24: Â£ {:.2f}".format(*b50)
        print(b51)
    return
def fonk18():
    fonk3('portfolio0.csv')
    fonk8()
    fonk9(b21 = True)
    valuate_portfolio(b11 = "2018-03-13", b21=True)
fonk18()