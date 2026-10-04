import csv
import os
import math
from datetime import datetime
import re
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
    raise DateError(f"Invalid date format: {date_string}")
def load_portfolio(file_path):
    global portfolio
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                portfolio[row['Stock']] = int(row['Quantity'])
    except FileNotFoundError:
        print(f"File not found: {file_path}")
def load_all_stocks():
    global stocks
    pass
def execute_trading_strategy(verbose=False):
    global transactions
    pass
def evaluate_portfolio(date, verbose=False):
    global portfolio
    normalized_date = normalize_date(date)
    if verbose:
        print(f"Evaluating portfolio on {normalized_date}")
def main():
    load_portfolio('portfolio0.csv')
    load_all_stocks()
    execute_trading_strategy(verbose=True)
    evaluate_portfolio(date="2018-03-13", verbose=True)
if __name__ == '__main__':
    main()