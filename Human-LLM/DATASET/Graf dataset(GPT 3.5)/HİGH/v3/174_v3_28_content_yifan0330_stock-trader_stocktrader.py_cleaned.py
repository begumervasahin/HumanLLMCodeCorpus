from datetime import datetime
import re
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
def fonk1(date_string):
    b4 = ['%Y-%m-%d', '%Y/%m/%d', '%d.%m.%Y']
    for fmt in b4:
        try:
            b5 = datetime.strptime(date_string, fmt)
            return b5.strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise class2("Invalid b7 format: {0}".format(date_string))
def fonk2():
    load_portfolio('portfolio0.csv')
    load_all_stocks()
    execute_trading_strategy(b6 = True)
    evaluate_portfolio(b7 = "2018-03-13", b6=True)
if b8 = = '__main__':
    fonk2()