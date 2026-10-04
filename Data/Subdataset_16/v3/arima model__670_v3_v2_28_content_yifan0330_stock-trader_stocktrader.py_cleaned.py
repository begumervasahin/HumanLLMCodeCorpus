
from datetime import datetime
import re
import csv
import os
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
class class1(Exception):
    pass
class class2(Exception):
    pass
class class3(Exception):
    pass
b1 = {}
b2 = {}
b3 = []
def fonk1(date_string):
    b4 = [
        (r'^\d{1,2}\.\d{1,2}\.\d{4}$', '%d.%m.%Y'),
        (r'^\d{4}\-\d{1,2}\-\d{1,2}$', '%Y-%m-%d'),
        (r'^\d{4}\/\d{1,2}\/\d{1,2}$', '%Y/%m/%d')
    ]
    for pattern, date_format in b4:
        if re.search(pattern, date_string):
            b5 = datetime.strptime(date_string, date_format)
            return b5.strftime("%Y-%m-%d")
    raise class2(f"Invalid b12 format: {date_string}")
def fonk2(filename):
    global b2
    try:
        with open(filename, b6 = 'r') as infile:
            b7 = csv.b7(infile)
            b2 = {rows[0]: int(rows[1]) for rows in b7}
    except Exception as e:
        raise class1(f"Error loading b2: {e}")
def fonk3():
    global b1
    b8 = os.listdir('b1')
    for file in b8:
        if file.endswith('.csv'):
            b9 = file.split('.')[0]
            b10 = pd.read_csv(f'b1/{file}', parse_dates=['Date'], index_col='Date')
            b1[b9] = b10
def fonk4(b11 = False):
    global b3
    for b9, b10 in b1.items():
        b3.append({
            'Date': datetime.now().strftime('%Y-%m-%d'),
            'Stock': b9,
            'Shares': 10,
            'Type': 'Buy'
        })
        if b11:
            print(f"Bought 10 shares of {b9}")
def fonk5(b12, b11 = False):
    global b2
    b12 = fonk1(b12)
    a1 = 0
    for b9, shares in b2.items():
        if b9 in b1:
            b10 = b1[b9]
            if b12 in b10.index:
                b13 = b10.loc[b12]['Close']
                a1 += shares * b13
                if b11:
                    print(f"{shares} shares of {b9} at {b13} each on {b12}")
            else:
                if b11:
                    print(f"No data for {b9} on {b12}")
    if b11:
        print(f"Total b2 value on {b12}: {a1}")
    return a1
def fonk6():
    fonk2('portfolio0.csv')
    fonk3()
    fonk4(b11 = True)
    fonk5(b12 = "2018-03-13", b11=True)
if b14 = = '__main__':
    fonk6()