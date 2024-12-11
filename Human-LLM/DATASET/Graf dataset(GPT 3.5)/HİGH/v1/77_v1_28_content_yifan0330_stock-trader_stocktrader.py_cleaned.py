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
def fonk1(s):
    if re.search(r'^\d{1,2}\.\d{1,2}\.\d{4}$', s):
        b4 = datetime.strptime(s, '%d.%m.%Y')
    elif re.search(r'^\d{4}\-\d{1,2}\-\d{1,2}$', s):
        b4 = datetime.strptime(s, '%Y-%m-%d')
    elif re.search(r'^\d{4}\/\d{1,2}\/\d{1,2}$', s):
        b4 = datetime.strptime(s, '%Y/%m/%d')
    else:
        raise class2("Date Format is not allowed: {0}".format(s))
    return b4.strftime("%Y-%m-%d")
def fonk2():
    loadPortfolio('portfolio0.csv')
    loadAllStocks()
    tradeStrategy1(b5 = True)
    valuatePortfolio(b6 = "2018-03-13", b5=True)
if b7 = = '__main__':
    fonk2()