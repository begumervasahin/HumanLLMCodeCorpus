import re
from datetime import datetime
import csv
import os
import math
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
def fonk1(date_str):
    try:
        if re.match(r'^\d{1,2}\.\d{1,2}\.\d{4}$', date_str):
            b4 = datetime.strptime(date_str, '%d.%m.%Y')
        elif re.match(r'^\d{4}-\d{1,2}-\d{1,2}$', date_str):
            b4 = datetime.strptime(date_str, '%Y-%m-%d')
        elif re.match(r'^\d{4}/\d{1,2}/\d{1,2}$', date_str):
            b4 = datetime.strptime(date_str, '%Y/%m/%d')
        else:
            raise class2(f"Date format is not allowed: {date_str}")
        return b4.strftime("%Y-%m-%d")
    except ValueError as e:
        raise class2(f"Date format is incorrect: {date_str}") from e
def fonk2(file_path):
    global b2
    try:
        with open(file_path, 'r') as file:
            b5 = csv.DictReader(file)
            for row in b5:
                b2[row['stock']] = {
                    'quantity': int(row['quantity']),
                    'purchase_price': float(row['purchase_price'])
                }
    except Exception as e:
        print(f"Failed to load b2: {e}")
def fonk3():
    global b1
    pass
def fonk4(b6 = False):
    if b6:
        print("Executing trade strategy 1...")
def fonk5(b7, b6 = False):
    if b6:
        print(f"Valuating b2 on {b7}...")
def fonk6():
    fonk2('portfolio0.csv')
    fonk3()
    fonk4(b6 = True)
    fonk5(b7 = "2018-03-13", b6=True)
if b8 = = '__main__':
    fonk6()