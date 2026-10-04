import re
from datetime import datetime
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
def normalise_date(date_str):
    try:
        if re.match(r'^\d{1,2}\.\d{1,2}\.\d{4}$', date_str):
            date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        elif re.match(r'^\d{4}-\d{1,2}-\d{1,2}$', date_str):
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        elif re.match(r'^\d{4}/\d{1,2}/\d{1,2}$', date_str):
            date_obj = datetime.strptime(date_str, '%Y/%m/%d')
        else:
            raise DateError(f"Date format is not allowed: {date_str}")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError as e:
        raise DateError(f"Date format is incorrect: {date_str}") from e
def load_portfolio(file_path):
    global portfolio
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                portfolio[row['stock']] = {
                    'quantity': int(row['quantity']),
                    'purchase_price': float(row['purchase_price'])
                }
    except Exception as e:
        print(f"Failed to load portfolio: {e}")
def load_all_stocks():
    global stocks
    pass
def trade_strategy1(verbose=False):
    if verbose:
        print("Executing trade strategy 1...")
def valuate_portfolio(date, verbose=False):
    if verbose:
        print(f"Valuating portfolio on {date}...")
def main():
    load_portfolio('portfolio0.csv')
    load_all_stocks()
    trade_strategy1(verbose=True)
    valuate_portfolio(date="2018-03-13", verbose=True)
if __name__ == '__main__':
    main()