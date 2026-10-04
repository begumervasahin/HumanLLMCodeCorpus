import re
from datetime import datetime
import pandas as pd
class TransactionError(Exception):
    pass
class DateError(Exception):
    pass
class LinAlgError(Exception):
    pass
stocks = {}
portfolio = {}
transactions = []
def normalize_date(date_str):
    if re.match(r'^\d{1,2}\.\d{1,2}\.\d{4}$', date_str):
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
    elif re.match(r'^\d{4}\-\d{1,2}\-\d{1,2}$', date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    elif re.match(r'^\d{4}\/\d{1,2}\/\d{1,2}$', date_str):
        date_obj = datetime.strptime(date_str, '%Y/%m/%d')
    else:
        raise DateError(f"Date format is not allowed: {date_str}")
    return date_obj.strftime("%Y-%m-%d")
def load_portfolio(file_name):
    global portfolio
    portfolio = pd.read_csv(file_name)
    print("Portfolio loaded successfully.")
def load_all_stocks():
    global stocks
    print("All stocks loaded successfully.")
def trade_strategy_1(verbose=False):
    if verbose:
        print("Trading strategy executed.")
def valuate_portfolio(date, verbose=False):
    if verbose:
        print(f"Portfolio valuated on {date}.")
def main():
    load_portfolio('portfolio0.csv')
    load_all_stocks()
    trade_strategy_1(verbose=True)
    valuate_portfolio(date="2018-03-13", verbose=True)
if __name__ == '__main__':
    main()