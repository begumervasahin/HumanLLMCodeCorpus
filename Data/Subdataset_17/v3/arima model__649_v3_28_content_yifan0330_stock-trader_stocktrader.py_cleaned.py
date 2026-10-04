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
def normalize_date(date_string):
    date_formats = ['%Y-%m-%d', '%Y/%m/%d', '%d.%m.%Y']
    for fmt in date_formats:
        try:
            date_object = datetime.strptime(date_string, fmt)
            return date_object.strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise DateError("Invalid date format: {0}".format(date_string))
def main():
    load_portfolio('portfolio0.csv')
    load_all_stocks()
    execute_trading_strategy(verbose=True)
    evaluate_portfolio(date="2018-03-13", verbose=True)
if __name__ == '__main__':
    main()