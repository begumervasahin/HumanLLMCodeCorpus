
from datetime import datetime
import re
import csv
import os
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
class TransactionError(Exception):
    pass
class DateError(Exception):
    pass
class LinAlgError(Exception):
    pass
stocks = {}
portfolio = {}
transactions = []
def normalise_date(date_string):
    date_patterns = [
        (r'^\d{1,2}\.\d{1,2}\.\d{4}$', '%d.%m.%Y'),
        (r'^\d{4}\-\d{1,2}\-\d{1,2}$', '%Y-%m-%d'),
        (r'^\d{4}\/\d{1,2}\/\d{1,2}$', '%Y/%m/%d')
    ]
    for pattern, date_format in date_patterns:
        if re.search(pattern, date_string):
            date_object = datetime.strptime(date_string, date_format)
            return date_object.strftime("%Y-%m-%d")
    raise DateError(f"Invalid date format: {date_string}")
def load_portfolio(filename):
    global portfolio
    try:
        with open(filename, mode='r') as infile:
            reader = csv.reader(infile)
            portfolio = {rows[0]: int(rows[1]) for rows in reader}
    except Exception as e:
        raise TransactionError(f"Error loading portfolio: {e}")
def load_all_stocks():
    global stocks
    stock_files = os.listdir('stocks')
    for file in stock_files:
        if file.endswith('.csv'):
            stock_name = file.split('.')[0]
            stock_data = pd.read_csv(f'stocks/{file}', parse_dates=['Date'], index_col='Date')
            stocks[stock_name] = stock_data
def trade_strategy_1(verbose=False):
    global transactions
    for stock_name, stock_data in stocks.items():
        transactions.append({
            'Date': datetime.now().strftime('%Y-%m-%d'),
            'Stock': stock_name,
            'Shares': 10,
            'Type': 'Buy'
        })
        if verbose:
            print(f"Bought 10 shares of {stock_name}")
def valuate_portfolio(date, verbose=False):
    global portfolio
    date = normalise_date(date)
    total_value = 0
    for stock_name, shares in portfolio.items():
        if stock_name in stocks:
            stock_data = stocks[stock_name]
            if date in stock_data.index:
                price = stock_data.loc[date]['Close']
                total_value += shares * price
                if verbose:
                    print(f"{shares} shares of {stock_name} at {price} each on {date}")
            else:
                if verbose:
                    print(f"No data for {stock_name} on {date}")
    if verbose:
        print(f"Total portfolio value on {date}: {total_value}")
    return total_value
def main():
    load_portfolio('portfolio0.csv')
    load_all_stocks()
    trade_strategy_1(verbose=True)
    valuate_portfolio(date="2018-03-13", verbose=True)
if __name__ == '__main__':
    main()