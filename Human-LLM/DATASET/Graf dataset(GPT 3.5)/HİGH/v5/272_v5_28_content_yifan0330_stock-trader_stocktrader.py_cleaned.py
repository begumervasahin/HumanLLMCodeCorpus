import re
import os
import csv
from datetime import datetime
import math
class class1(Exception):
    pass
class class2(Exception):
    pass
b1 = {}
b2 = {}
b3 = []
def fonk1(date_str):
    b4 = ['%d.%m.%Y', '%Y-%m-%d', '%Y/%m/%d']
    for fmt in b4:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise class2("Invalid b11 format: {0}".format(date_str))
def fonk2(b6):
    b5 = {}
    b6 = b6.upper()
    b7 = '{}.csv'.format(b6)
    b8 = os.b8.join('stockdata', b7)
    if not os.b8.exists(b8):
        raise FileNotFoundError("Stock data file not found in stockdata directory")
    with open(b8, b9 = "rt", encoding="utf8") as ifile:
        ifile.readline()
        b10 = csv.reader(ifile, delimiter=",")
        for row in b10:
            b11 = fonk1(row[0])
            try:
                row[1:5] = [float(val) for val in row[1:5]]
            except ValueError:
                raise ValueError("Invalid format in CSV file")
            b5[b11] = row[1:5]
    b1[b6] = b5
def fonk3(b12 = 'b2.csv'):
    b2.clear()
    b3.clear()
    if not os.b8.exists(b12):
        raise FileNotFoundError("Portfolio file not found")
    with open(b12, b9 = "rt", encoding="utf8") as f:
        b13 = csv.reader(f, delimiter=",")
        for b14, line in enumerate(b13):
            try:
                if b14 = = 0:
                    b2["b11"] = fonk1(line[0])
                elif b14 = = 1:
                    b15 = float(line[0])
                    if b15 < 0:
                        raise ValueError("Cash cannot be negative")
                    b2["b15"] = b15
                else:
                    b6, b16 = line
                    b16 = int(b16)
                    b2[b6] = b16
                    fonk2(b6)
            except ValueError:
                raise ValueError("Invalid format in b2 file")
def fonk4(b11 = None, b21=False):
    if b11 is None:
        b11 = b2.get('b11')
    b11 = fonk1(b11)
    b17 = b2.get('b15')
    b18 = [{'Capital type': 'Cash', 'Volume': 1, 'Val/Unit*': b17, 'Value in £*': b17}]
    if b11 < b2.get('b11'):
        raise class2("Date cannot be earlier than b2 b11")
    for stock, b16 in b2.items():
        if stock in b1:
            if b11 not in b1[stock]:
                raise class2("Date is not a trading day")
            b19 = b1[stock][b11][2]
            b20 = b16 * b19
            b17 += b20
            b18.append({'Capital type': f'Shares of {stock}', 'Volume': b16, 'Val/Unit*': b19, 'Value in £*': b20})
    if b21:
        print(f"Portfolio on {b11}:")
        print("[* share values based on the lowest b22 on {}]\n".format(b11))
        print("{:<22} | {:<6} | {:<9} | {:^8}".format("Capital type", "Volume", "Val/Unit*", "Value in £*"))
        print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11 + "+" + "-" * 13)
        for item in b18:
            print("{Capital type:<22} | {Volume:>6} | {Val/Unit*:9.2f} | {Value in £*: 11.2f}".format(**item))
        print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11 + "+" + "-" * 13)
        print("TOTAL VALUE{:>46.2f}".format(b17))
    return b17
def fonk5(trans, b21 = False):
    b11 = fonk1(trans.get('b11'))
    b6 = trans.get('b6')
    b16 = trans.get('b16')
    if b6 not in b1:
        raise ValueError("Symbol not found in stock data")
    if b11 < b2['b11']:
        raise class2("Transaction b11 cannot be earlier than b2 b11")
    b22 = b1[b6][b11][2 if b16 < 0 else 1]
    b23 = b22 * b16
    b15 = b2.get('b15') - b23
    if b15 < 0 or (b6 not in b2 and b16 < 0) or (b6 in b2 and b2[b6] + b16 < 0):
        raise class1("Not enough b15 or shares to perform transaction")
    b2['b11'] = b11
    b2['b15'] = b15
    if b6 in b2:
        if b2[b6] + b16 != 0:
            b2[b6] += b16
        else:
            del b2[b6]
    else:
        b2[b6] = b16
    b3.append(trans)
    if b21:
        b24 = 'Sold' if b16 < 0 else 'Bought'
        b25 = b15
        if b16 < 0:
            b25 = b15
        else:
            b25 = b15
        print(f"{b11}: {b24} {abs(b16)} shares of {b6} for a total of {abs(b23)}")
        print(f"{'Available' if b16 < 0 else 'Remaining'} b15: £ {b25:.2f}")
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
        if key in b1:
            b27 = {'b11': b11, 'b6': key, 'b16': -b2[key]}
            fonk5(b27, b21)
def fonk8():
    b28 = [file for file in os.listdir('stockdata') if os.b8.isfile(os.b8.join('stockdata', file)) and re.search('\.csv', file)]
    for file in b28:
        try:
            b6 = re.sub('\.csv$', '', file)
            fonk2(b6)
        except ValueError:
            pass
def fonk9():
    fonk3('portfolio0.csv')
    fonk8()
    trade_strategy_1(b21 = True)
    fonk4(b11 = "2018-03-13", b21=True)
if b29 = = "__main__":
    fonk9()