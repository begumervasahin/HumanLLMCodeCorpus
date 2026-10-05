import re
import os
import csv
from datetime import datetime
import math
from pprint import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as st
from statsmodels.tsa.arima_model import ARIMA
class TransactionError(Exception):
    pass
class DateError(Exception):
    pass
class LinAlgError(Exception):
    pass
stocks = {}
portfolio = {}
transactions = []
def normalize_date(s):
    if re.search(r'^\d{1,2}\.\d{1,2}\.\d{4}$', s):
        date_str = datetime.strptime(s, '%d.%m.%Y')
    elif re.search(r'^\d{4}\-\d{1,2}\-\d{1,2}$', s):
        date_str = datetime.strptime(s, '%Y-%m-%d')
    elif re.search(r'^\d{4}\/\d{1,2}\/\d{1,2}$', s):
        date_str = datetime.strptime(s, '%Y/%m/%d')
    else:
        raise DateError("Invalid date format: {0}".format(s))
    return date_str.strftime("%Y-%m-%d")
def load_stock(symbol):
    symbol_dict = {}
    symbol = symbol.upper()
    symbol_file = '{}.csv'.format(symbol)
    path = os.path.join('stockdata', symbol_file)
    if os.path.exists(path) is False:
        raise FileNotFoundError("Stock data file not found in stockdata directory")
    else:
        with open(path, mode="rt", encoding="utf8") as ifile:
            ifile.readline()
            data_reader = csv.reader(ifile, delimiter=",")
            for row in data_reader:
                date = normalize_date(row[0])
                for i in range(1, 5):
                    try:
                        row[i] = float(row[i])
                    except ValueError:
                        raise ValueError("Invalid format in CSV file")
                symbol_dict[date] = row[1:5]
        stocks[symbol] = symbol_dict
def load_portfolio(fname='portfolio.csv'):
    portfolio.clear()
    transactions.clear()
    if os.path.exists(fname) is False:
        raise FileNotFoundError("Portfolio file not found")
    else:
        with open(fname, mode="rt", encoding="utf8") as f:
            f_reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(f_reader):
                try:
                    if i == 0:
                        portfolio["date"] = normalize_date(line[0])
                    if i == 1:
                        portfolio["cash"] = float(line[0])
                        if portfolio["cash"] < 0:
                            raise ValueError("Cash cannot be negative")
                    if i >= 2:
                        portfolio[line[0]] = int(line[1])
                        load_stock(line[0])
                except ValueError:
                    raise ValueError("Invalid format in portfolio file")
def evaluate_portfolio(date=None, verbose=False):
    if date is None:
        date = portfolio.get('date')
    date = normalize_date(date)
    total_stock = []
    total_stock.append({'Capital type': 'Cash', 'Volume': 1, 'Val/Unit*': portfolio.get('cash'), 'Value in £*': portfolio.get('cash')})
    total_value = portfolio.get('cash')
    if date < portfolio.get('date'):
        raise DateError("Date cannot be earlier than portfolio date")
    else:
        for stock in portfolio.keys():
            if stock in stocks.keys():
                stock_value = {}
                stock_value["Capital type"] = "Shares of {}".format(stock)
                volume = portfolio.get(stock)
                stock_value["Volume"] = volume
                if date not in stocks[stock].keys():
                    raise DateError("Date is not a trading day")
                else:
                    unit_value = stocks[stock][date][2]
                    stock_value["Val/Unit*"] = unit_value
                    value = volume * unit_value
                    stock_value["Value in £*"] = value
                    total_value += value
                    total_stock.append(stock_value)
        if verbose:
            print("Portfolio on {}:".format(date))
            print("[* share values based on the lowest price on {}]\n".format(date))
            print("{0:<22} | {1} | {2} | {3:^8}".format("Capital type", "Volume", "Val/Unit*", "Value in £*"))
            print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11 + "+" + "-" * 13)
            for item in total_stock:
                print("{Capital type:<22} | {Volume:>6} | {Val/Unit*:9.2f} | {Value in £*: 11.2f}".format(**item))
            print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11 + "+" + "-" * 13)
            print("TOTAL VALUE{:>46.2f}".format(total_value))
        return total_value
def add_transaction(trans, verbose=False):
    date = normalize_date(trans.get('date'))
    symbol = trans.get('symbol')
    volume = trans.get('volume')
    if symbol not in stocks.keys():
        raise ValueError("Symbol not found in stock data")
    if date < portfolio['date']:
        raise DateError("Transaction date cannot be earlier than portfolio date")
    price = stocks[symbol][date][2 if volume < 0 else 1]
    total_price = price * volume
    cash = portfolio.get('cash') - total_price
    if (cash < 0 or
       portfolio.get(symbol) is None and volume < 0 or
       portfolio.get(symbol) is not None and portfolio.get(symbol) + volume < 0):
        raise TransactionError("Not enough cash or shares to perform transaction")
    portfolio['date'] = date
    portfolio['cash'] = cash
    if portfolio.get(symbol) is not None:
        if portfolio.get(symbol) + volume != 0:
            portfolio[symbol] = portfolio.get(symbol) + volume
        else:
            del portfolio[symbol]
    else:
        portfolio[symbol] = volume
    transactions.append(trans)
    if verbose:
        transaction_info = "{}: {} {} shares of {} for a total of {} \n{} cash: £ {:.2f}".format(date, 'Sold' if volume<0 else 'Bought',
                                                                                                  abs(volume), symbol, abs(total_price),
                                                                                                  'Available' if volume<0 else 'Remaining', cash)
        print(transaction_info)
    return
def save_portfolio(fname="portfolio.csv"):
    with open(fname, mode="wt", encoding="utf8") as csv_file:
        f_writer = csv.writer(csv_file)
        for key, value in portfolio.items():
            f_writer.writerow([key, value])
def sell_all(date=None, verbose=False):
    if date is None:
        date = portfolio.get('date')
    date = normalize_date(date)
    for key in portfolio.copy():
        if key in stocks.keys():
            key_trans = {'date': date, 'symbol': key, 'volume': -portfolio[key]}
            add_transaction(key_trans, verbose)
    return
def load_all_stocks():
    all_files = [file for file in os.listdir('stockdata') if os.path.isfile(os.path.join('stockdata', file)) and re.search('\.csv', file)]
    for file in all_files:
        try:
            file = re.sub('\.csv$', '', file)
            load_stock(file)
        except ValueError:
            pass
    return
def trade_strategy_1(verbose=True):
    first_dict = next(iter(stocks.values()))
    trading_day = list(first_dict.keys())
    begin_date = portfolio.get('date')
    cash = portfolio.get('cash')
    if begin_date in trading_day:
        j = trading_day.index(begin_date)
    else:
        closest_date = min([x for x in trading_day if x > begin_date])
        if trading_day.index(closest_date) > 9:
            j = trading_day.index(closest_date)
        else:
            j = 9
    while j < len(trading_day):
        cash = portfolio.get('cash')
        sym_list = sorted(stocks.keys(), key=lambda s: (-calculate_q_buy(s, j), str.upper))
        for sym in sym_list:
            print(sym, calculate_q_buy(sym, j))
        sym = sym_list[0]
        unit_value = stocks[sym][trading_day[j]][1]
        vol = math.floor(cash / unit_value)
        trans = {'date': trading_day[j], 'symbol': sym, 'volume': vol}
        add_transaction(trans, True)
        k = j + 1
        while k < len(trading_day):
            if calculate_l(sym, k) / calculate_h(sym, j) > 1.3 or calculate_l(sym, k) / calculate_h(sym, j) < 0.7:
                sell_trans = {'date': trading_day[k], 'symbol': sym, 'volume': -vol}
                add_transaction(sell_trans, True)
                break
            k += 1
        j = k + 1
    return
def calculate_q_buy(s, j):
    if j >= 9:
        denominator = 0
        for i in range(0, 10):
            denominator += calculate_h(s, j - i)
        answer = 10 * calculate_h(s, j) / denominator
    else:
        answer = 0
    return answer
def calculate_h(s, j):
    first_dict = next(iter(stocks.values()))
    trading_day = list(first_dict.keys())
    trade_date = trading_day[j]
    high_price = stocks.get(s).get(trade_date)[1]
    return high_price
def calculate_l(s, j):
    first_dict = next(iter(stocks.values()))
    trading_day = list(first_dict.keys())
    trade_date = trading_day[j]
    low_price = stocks.get(s).get(trade_date)[2]
    return low_price
def trade_strategy_2(verbose=True):
    first_dict = next(iter(stocks.values()))
    trading_day = list(first_dict.keys())
    begin_date = portfolio.get('date')
    cash = portfolio.get('cash')
    if begin_date in trading_day:
        j = trading_day.index(begin_date)
    else:
        closest_date = min([x for x in trading_day if x > begin_date])
        if trading_day.index(closest_date) < 15:
            j = 20
        else:
            j = trading_day.index(closest_date)
    while j < len(trading_day):
        cash = portfolio.get('cash')
        increase_stock_list = []
        for stock in stocks.keys():
            if predict_price_increase(stock, date=trading_day[j], verbose=False):
                increase_stock_list.append(stock)
        buy_stock_list = sorted(increase_stock_list, key=lambda s: -calculate_increase(s, j))
        if len(buy_stock_list) == 0:
            pass
        else:
            sym = buy_stock_list[0]
            unit_value = stocks[sym][trading_day[j]][1]
            vol = math.floor(cash / unit_value)
            trans = {'date': trading_day[j], 'symbol': sym, 'volume': vol}
            add_transaction(trans, True)
            k = j + 30
            while k < len(trading_day):
                if predict_price_decrease(sym, date=trading_day[k], verbose=False):
                    sell_trans = {'date': trading_day[k], 'symbol': sym, 'volume': -vol}
                    add_transaction(sell_trans, True)
                    break
                k += 1
            j = k + 20
    return
def predict_price_increase(symbol, date, verbose=False):
    symbol = symbol.upper()
    load_stock(symbol)
    first_dict = next(iter(stocks.values()))
    trading_day = list(first_dict.keys())
    if trading_day_index(date) > 20:
        start_date = trading_day[trading_day_index(date) - 15]
    else:
        start_date = trading_day[10]
    actual_predictions = predict_stock(symbol, start_date, end_date=date, predict_duration=5, buy=True, verbose=False)
    if all(x <= y for x, y in zip(actual_predictions, actual_predictions[1:])):
        return True
    else:
        return False
def calculate_increase(symbol, j):
    symbol = symbol.upper()
    load_stock(symbol)
    first_dict = next(iter(stocks.values()))
    trading_day = list(first_dict.keys())
    date = trading_day[j]
    if trading_day_index(date) > 20:
        start_date = trading_day[trading_day_index(date) - 15]
    else:
        start_date = trading_day[10]
    date = trading_day[j]
    actual_predictions = predict_stock(symbol, start_date, end_date=date, predict_duration=5, buy=True, verbose=False)
    increase = float(actual_predictions[4]) - float(actual_predictions[0])
    return increase
def predict_price_decrease(symbol, date, verbose=False):
    symbol = symbol.upper()
    load_stock(symbol)
    first_dict = next(iter(stocks.values()))
    trading_day = list(first_dict.keys())
    if trading_day_index(date) > 20:
        start_date = trading_day[trading_day_index(date) - 15]
    else:
        start_date = trading_day[10]
    actual_predictions = predict_stock(symbol, start_date, end_date=date, predict_duration=5, buy=False, verbose=False)
    if all(x >= y for x, y in zip(actual_predictions, actual_predictions[1:])):
        return True
    else:
        return False
def add_transaction(trans, verbose=False):
    date = normalize_date(trans.get('date'))
    symbol = trans.get('symbol')
    volume = trans.get('volume')
    if symbol not in stocks.keys():
        raise ValueError("The symbol in transaction is not in stocks dictionary")
    if date < portfolio['date']:
        raise DateError("The date of transaction is earlier than that of portfolio")
    price = stocks[symbol][date][2 if volume < 0 else 1]
    total_price = price * volume
    cash = portfolio.get('cash') - total_price
    if (cash < 0 or
        portfolio.get(symbol) is None and volume < 0 or
        portfolio.get(symbol) is not None and portfolio.get(symbol) + volume < 0):
        raise TransactionError("Not enough cash or Not enough shares to sell")
    portfolio['date'] = date
    portfolio['cash'] = cash
    if portfolio.get(symbol) is not None:
        if portfolio.get(symbol) + volume != 0:
            portfolio[symbol] = portfolio.get(symbol) + volume
        else:
            del portfolio[symbol]
    else:
        portfolio[symbol] = volume
    transactions.append(trans)
    if verbose:
        args = [date, 'Sold' if volume < 0 else 'Bought', abs(volume), symbol, abs(total_price), 'Available' if volume < 0 else 'Remaining', cash]
        trans_info = "{}: {} {} shares of {} for a total of {} \n{} cash: Â£ {:.2f}".format(*args)
        print(trans_info)
    return
def main():
    load_portfolio('portfolio0.csv')
    load_all_stocks()
    trade_strategy_1(verbose=True)
    valuate_portfolio(date="2018-03-13", verbose=True)
main()