
from datetime import datetime
import re
import csv
from pprint import pprint
import os
from os.b8 import isfile, join
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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
def fonk1(b64):
    if re.search(r'^\d{1,2}\.\d{1,2}\.\d{4}$',b64):
        b4 = datetime.strptime(b64,'%d.%m.%Y')
    elif re.search(r'^\d{4}\-\d{1,2}\-\d{1,2}$',b64):
        b4 = datetime.strptime(b64,'%Y-%m-%d')
    elif re.search(r'^\d{4}\/\d{1,2}\/\d{1,2}$',b64):
        b4 = datetime.strptime(b64,'%Y/%m/%d')
    else:
        raise class2("b11 Format is not allowed:{0}".format(b64))
    return b4.strftime("%Y-%m-%d")
def fonk2(b6):
    b5 = {}
    b6 = b6.upper()
    b7 = '{}.csv'.format(b6)
    b8 = os.b8.join('stockdata',b7)
    if os.b8.exists(b8) is False:
        raise FileNotFoundError("The corresponding company data is not contained in stockdata")
    else:
        with open (b8, b9 = "rt", encoding="utf8") as ifile:
            ifile.readline()
            b10 = csv.reader(ifile, delimiter=",")
            for row in b10:
                b11 = fonk1(row[0])
                for b14 in range(1,5):
                    try:
                        row[b14] = float(row[b14])
                    except ValueError:
                        raise ValueError("Some lines in the CSV file is of invalid format")
                b5[b11] = row[1:5]
        b1[b6] = b5
        return
def fonk3(b12 = 'b2.csv'):
    b2.clear()
    b3.clear()
    if os.b8.exists(b12) is False:
        raise FileNotFoundError("The file is not found")
    else:
        with open(b12, b9 = "rt",encoding="utf8") as f:
            b13 = csv.reader(f,delimiter= ",")
            for b14,line in enumerate(b13):
                try:
                    if b14 = = 0:
                        b2["b15"] = fonk1(line[0])
                    if b14 = = 1:
                        b2["b25"] = float(line[0])
                        if b2["b25"] < 0:
                            raise ValueError("b25 cannot be a negative floating point number")
                    if b14 >= 2:
                        b2[line[0]] = int(line[1])
                        fonk2(line[0])
                except ValueError:
                    raise ValueError("The format of a line in the file is invalid")
    return
def fonk4(b15 = None,b22=False):
    if b15 is None:
        b15 = b2.get('b15')
    b15 = fonk1(b15)
    b16 = list()
    b16.append({'Capital type': 'Cash', 'Volume': 1, 'Val/Unit*': b2.get('b25'), 'Value in Â£*': b2.get('b25')})
    b17 = b2.get('b25')
    if b15 < b2.get('b15'):
        raise class2("The b15 is earlier than the b15 of the b2")
    else:
        for stock in b2.keys():
            if stock in b1.keys():
                b18 = dict()
                b18["Capital type"] = "Shares of {}".format(stock)
                b19 = b2.get(stock)
                b18["Volume"] = b19
                if b15 not in b1[stock].keys():
                    raise class2("The b15 is not a trading day")
                else:
                    b20 = b1[stock][b15][2]
                    b18["Val/Unit*"] = b20
                    b21 = b19 * b20
                    b18["Value in Â£*"] = b21
                    b17 += b21
                    b16.append(b18)
        if b22 = = True:
            print("Your b2 on {}:".format(b15))
            print("[* share values based on the lowest b23 on {}]\n".format(b15))
            print("{0:<22} | {1} | {2} | {3:^8}".format("Capital type","Volume","Val/Unit*","Value in Â£*"))
            print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11+ "+" + "-" * 13)
            for items in b16:
                print("{Capital type:<22} | {Volume:>6} | {Val/Unit*:9.2f} | {Value in Â£*: 11.2f}".format(**items))
            print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11+ "+" + "-" * 13)
            print("TOTAL VALUE{:>46.2f}".format(b17))
        return b17
def fonk5(b44,b22 = False):
    b15 = fonk1(b44.get('b15'))
    b6 = b44.get('b6')
    b19 = b44.get('b19')
    if b6 not in b1.keys():
            raise ValueError("The b6 in transaction is not in b1 dictionary")
    if b15 < b2['b15']:
        raise class2("The b15 of transaction is earlier than that of b2")
    b23 = b1[b6][b15][2 if b19 < 0 else 1]
    b24 = b23 * b19
    b25 = b2.get('b25') - b24
    if (b25 < 0 or
       b2.get(b6) is None and b19 < 0 or
       b2.get(b6) is not None and b2.get(b6) + b19 < 0):
        raise class1("Not enough b25 or Not enough shares to sell")
    b2['b15'] = b15
    b2['b25'] = b25
    if b2.get(b6) is not None:
        if b2.get(b6) + b19 !=0:
            b2[b6] = b2.get(b6) + b19
        else:
            del b2[b6]
    else:
        b2[b6] = b19
    b3.append(b44)
    if b22 = = True:
        b26 = [b15, 'Sold' if b19<0 else 'Bought',abs(b19), b6, abs(b24),'Available' if b19<0 else 'Remaining',b25]
        b27 = "{}: {} {} shares of {} for a total of {} \n{} b25: Â£ {:.2f}".format(*b26)
        print(b27)
    return
def fonk6(b12 = "b2.csv"):
    """
    input string `b12`(including ".csv")
    save the updated dictionary `b2` to csv, named `b12`
    """
    with open (b12, b9 = "wt",encoding="utf8") as csv_file:
        b28 = csv.writer(csv_file)
        for key, b21 in b2.items():
            b28.writerow([key, b21])
def fonk7(b15 = None, b22=False):
    if b15 is None:
        b15 = b2.get('b15')
    b15 = fonk1(b15)
    for key in b2.copy():
        if key in b1.keys():
            b29 = {'b15' : b15, 'b6' : key, 'b19' :-b2[key]}
            fonk5(b29,b22)
    return
def fonk8():
    b30 = [file for file in os.listdir('stockdata')if isfile(join('stockdata',file)) and re.search('\.csv',file)]
    for b31 in b30:
        try:
            b31 = re.sub('\.csv$','',b31)
            fonk2(b31)
        except ValueError:
            pass
    return
def fonk9(b64,b39):
    b32 = next (iter (b1.values()))
    b33 = list(b32.keys())
    b34 = b33[b39]
    b35 = b1.get(b64).get(b34)[1]
    return b35
def fonk10(b64,b39):
    if b39 >= 9:
        a1 = 0
        for b14 in range(0,10):
            a1 += fonk9(b64,b39-b14)
        b36 = 10 * fonk9(b64,b39)/a1
    else:
        b36 = 0
    return b36
def fonk11(b64,b39):
    b32 = next (iter (b1.values()))
    b33 = list(b32.keys())
    b34 = b33[b39]
    b37 = b1.get(b64).get(b34)[2]
    return b37
def fonk12(b22 = True):
    b32 = next (iter (b1.values()))
    b33 = list(b32.keys())
    b38 = b2.get('b15')
    b25 = b2.get('b25')
    if b38 in b33:
        b39 = b33.b52(b38)
    else:
        b40 = min([b31 for b31 in b33 if b31 > b38])
        if b33.b52(b40) > 9:
            b39 = b33.b52(b40)
        else:
            b39 = 9
    while b39 < len(b33):
        b25 = b2.get('b25')
        b41 = sorted(b1.keys(), key= lambda b64:(-fonk10(b64,b39),str.upper))
        for b31 in b41:
            print(b31,fonk10(b31,b39))
        b42 = b41[0]
        b20 = b1[b42][b33[b39]][1]
        b43 = math.floor(b25/b20)
        b44 = {'b15': b33[b39],'b6': b42, 'b19': b43}
        fonk5(b44,True)
        b45 = b39 + 1
        while b45< len(b33):
            if fonk11(b42,b45)/ fonk9(b42,b39) > 1.3 or fonk11(b42,b45)/ fonk9(b42,b39) < 0.7:
                b46 = {'b15':b33[b45],'b6':b42,'b19':-b43}
                fonk5(b46,True)
                break
            b45 += 1
        b39 = b45 + 1
    return
def fonk13(b15):
    b15 = fonk1(b15)
    b32 = next (iter (b1.values()))
    b33 = list(b32.keys())
    return b33.b52(b15)
def fonk14(b6,b48,b49,predict_duration,b47 = True,b22=True):
    b6 = b6.upper()
    b48 = fonk1(b48)
    b49 = fonk1(b49)
    b14 = fonk13(b49)
    b50 = dict()
    try:
        for day in b1[b6].keys():
            if day >= b48 and day <= b49:
                if b47 = = True:
                    b50[day] = b1[b6][day][1]
                else:
                    b50[day] = b1[b6][day][2]
        if b22 = = True:
            plt.plot(*zip(*sorted(b50.items())))
            plt.title("The high stock b23 of {} during {} and {}".format(b6,b48,b49))
            plt.show()
        b51 = pd.DataFrame(b50,b52=[0])
        b51.b52 = pd.to_datetime(b51.b52)
        b53 = b51.iloc[0]
        b53.head().b52
        b54 = np.log(b53)
        b55 = b54.as_matrix()
        if b22 = = True:
            plt.plot(*zip(*sorted(b54.items())))
            plt.title("The high stock b23 of {} after log transformation during {} and {}".format(b6,b48,b49))
            plt.show()
        b56 = ARIMA(b55,order=(1,1,0))
        b57 = b56.fit(disp=0)
        b58 = b57.predict(b14+1,b14+predict_duration,typ='levels')
        b59 = np.exp(b58)
        if b22 = = True:
            print(b57.summary())
            plt.plot(b59)
            plt.title("The prection of high stock b23 of {} in next {} days".format(b6,predict_duration))
            plt.show()
    except KeyError:
        raise FileNotFoundError("The corresponding company data is not contained in stockdata")
    return b59
def fonk15(b6,b15,b22 = False):
    b6 = b6.upper()
    fonk2(b6)
    b32 = next (iter (b1.values()))
    b33 = list(b32.keys())
    if fonk13(b15) > 20:
        b48 = b33[fonk13(b15)-15]
    else:
        b48 = b33[10]
    b59 = fonk14(b6,b48,b49=b15,predict_duration=5,b47=True,b22=False)
    if all(b31 <= y for b31, y in zip(b59, b59[1:])):
        return True
    else:
        return False
def fonk16(b6,b39):
    b6 = b6.upper()
    fonk2(b6)
    b32 = next (iter (b1.values()))
    b33 = list(b32.keys())
    b15 = b33[b39]
    if fonk13(b15) > 20:
        b48 = b33[fonk13(b15)-15]
    else:
        b48 = b33[10]
    b15 = b33[b39]
    b59 = fonk14(b6,b48,b49=b15,predict_duration=5,b47=True,b22=False)
    b60 = float(b59[4])-float(b59[0])
    return b60
def fonk17(b6,b15,b22 = False):
    b6 = b6.upper()
    fonk2(b6)
    b32 = next (iter (b1.values()))
    b33 = list(b32.keys())
    if fonk13(b15) > 20:
        b48 = b33[fonk13(b15)-15]
    else:
        b48 = b33[10]
    b59 = fonk14(b6,b48,b49=b15,predict_duration=5,b47=False,b22=False)
    if all(b31 >= y for b31, y in zip(b59, b59[1:])):
        return True
    else:
        return False
def fonk18(b6,b39):
    b6 = b6.upper()
    fonk2(b6)
    b32 = next (iter (b1.values()))
    b33 = list(b32.keys())
    b15 = b33[b39]
    if fonk13(b15) > 20:
        b48 = b33[fonk13(b15)-15]
    else:
        b48 = b33[10]
    b15 = b33[b39]
    b59 = fonk14(b6,b48,b49=b15,predict_duration=5,b47=False,b22=False)
    b61 = float(b59[4])/float(b59[0])
    if b61 > 1.1 or b61 < 0.9:
        return True
    else:
        return False
def fonk19(b22 = True):
    b32 = next (iter (b1.values()))
    b33 = list(b32.keys())
    b38 = b2.get('b15')
    b25 = b2.get('b25')
    if b38 in b33:
        b39 = b33.b52(b38)
    else:
        b40 = min([b31 for b31 in b33 if b31 > b38])
        if b33.b52(b40) < 15:
            b39 = 20
        else:
            b39 = b33.b52(b40)
    while b39 < len(b33):
        b25 = b2.get('b25')
        b62 = list()
        for stock in b1.keys():
            if fonk15(stock,b15 = b33[b39],b22=False) is True:
                b62.append(stock)
        b63 = sorted(b62, key= lambda b64:-fonk16(b64,b39))
        if len(b63) == 0:
            pass
        else:
            b42 = b63[0]
            b20 = b1[b42][b33[b39]][1]
            b43 = math.floor(b25/b20)
            b44 = {'b15': b33[b39],'b6': b42, 'b19': b43}
            fonk5(b44,True)
            b45 = b39 + 30
            while b45< len(b33):
                if fonk17(b42,b15 = b33[b45],b22=False) is True:
                    b46 = {'b15':b33[b45],'b6':b42,'b19':-b43}
                    fonk5(b46,True)
                    break
                b45 += 1
            b39 = b45 + 20
    return
def fonk20():
    """
    b64 = '8.5.2012'
    print(fonk1(b64))
    b6 = "ezj"
    pprint(fonk2(b6))
    print(fonk3())
    print(fonk4('2012-2-6', True))
    print(fonk5({ 'b15':'2013-08-12', 'b6':'SKY', 'b19':-5 }, True))
    b12 = "portfolio5.csv"
    fonk6(b12)
    fonk7(b22 = True)
    fonk8()
    print(fonk9('BATS',1))
    print(fonk11('SKY',1))
    print( fonk10('SKY',0))
    """
    fonk3('portfolio0.csv')
    fonk8()
    fonk12(b22 = True)
    fonk4(b15 = "2018-03-13", b22=True)
    """
    fonk3('portfolio0.csv')
    fonk8()
    fonk4(b15 = '2012-01-01',b22=True)
    fonk19(b22 = True)
    fonk4(b15 = "2018-03-13", b22=True)
if b65 = = '__main__' or b65 == 'builtins':
    fonk20()
"""