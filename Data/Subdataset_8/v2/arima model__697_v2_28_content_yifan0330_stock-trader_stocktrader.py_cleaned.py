
from datetime import datetime
import re
import csv
import os
import math
import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.tsa.stattools as st
class TransactionError(Exception):
    pass
class DateError(Exception):
    pass
class LinAlgError(Exception):
    pass
stocks = {}
portfolio = {}
transactions = []
def normaliseDate(date_string):
    if re.search(r'^\d{1,2}\.\d{1,2}\.\d{4}$', date_string):
        date_object = datetime.strptime(date_string, '%d.%m.%Y')
    elif re.search(r'^\d{4}\-\d{1,2}\-\d{1,2}$', date_string):
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
    elif re.search(r'^\d{4}\/\d{1,2}\/\d{1,2}$', date_string):
        date_object = datetime.strptime(date_string, '%Y/%m/%d')
    else:
        raise DateError("Invalid date format: {0}".format(date_string))
    return date_object.strftime("%Y-%m-%d")
def main():
    loadPortfolio('portfolio0.csv')
    loadAllStocks()
    tradeStrategy1(verbose=True)
    valuatePortfolio(date="2018-03-13", verbose=True)
if __name__ == '__main__':
    main()