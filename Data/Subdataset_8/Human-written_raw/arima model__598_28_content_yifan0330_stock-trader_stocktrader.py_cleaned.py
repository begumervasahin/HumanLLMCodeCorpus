
from datetime import datetime
import re
import csv
from pprint import pprint
import os
from os.path import isfile, join
import math
import matplotlib.pyplot as plt
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
def normaliseDate(s):
    if re.search(r'^\d{1,2}\.\d{1,2}\.\d{4}$',s):
        date_str = datetime.strptime(s,'%d.%m.%Y')
    elif re.search(r'^\d{4}\-\d{1,2}\-\d{1,2}$',s):
        date_str = datetime.strptime(s,'%Y-%m-%d')
    elif re.search(r'^\d{4}\/\d{1,2}\/\d{1,2}$',s):
        date_str = datetime.strptime(s,'%Y/%m/%d')
    else:
        raise DateError("Date Format is not allowed:{0}".format(s))
    return date_str.strftime("%Y-%m-%d")
def loadStock(symbol):
    symbol_dict = {}
    symbol = symbol.upper()
    symbol_file = '{}.csv'.format(symbol)
    path = os.path.join('stockdata',symbol_file)
    if os.path.exists(path) is False:
        raise FileNotFoundError("The corresponding company data is not contained in stockdata")
    else:
        with open (path, mode="rt", encoding="utf8") as ifile:
            ifile.readline()
            data_reader = csv.reader(ifile, delimiter=",")
            for row in data_reader:
                Date = normaliseDate(row[0])
                for i in range(1,5):
                    try:
                        row[i] = float(row[i])
                    except ValueError:
                        raise ValueError("Some lines in the CSV file is of invalid format")
                symbol_dict[Date] = row[1:5]
        stocks[symbol] = symbol_dict
        return
def loadPortfolio(fname='portfolio.csv'):
    portfolio.clear()
    transactions.clear()
    if os.path.exists(fname) is False:
        raise FileNotFoundError("The file is not found")
    else:
        with open(fname, mode="rt",encoding="utf8") as f:
            f_reader = csv.reader(f,delimiter= ",")
            for i,line in enumerate(f_reader):
                try:
                    if i == 0:
                        portfolio["date"] = normaliseDate(line[0])
                    if i == 1:
                        portfolio["cash"] = float(line[0])
                        if portfolio["cash"] < 0:
                            raise ValueError("cash cannot be a negative floating point number")
                    if i >= 2:
                        portfolio[line[0]] = int(line[1])
                        loadStock(line[0])
                except ValueError:
                    raise ValueError("The format of a line in the file is invalid")
    return
def valuatePortfolio(date=None,verbose=False):
    if date is None:
        date = portfolio.get('date')
    date = normaliseDate(date)
    total_stock = list()
    total_stock.append({'Capital type': 'Cash', 'Volume': 1, 'Val/Unit*': portfolio.get('cash'), 'Value in Â£*': portfolio.get('cash')})
    total_value = portfolio.get('cash')
    if date < portfolio.get('date'):
        raise DateError("The date is earlier than the date of the portfolio")
    else:
        for stock in portfolio.keys():
            if stock in stocks.keys():
                stock_value = dict()
                stock_value["Capital type"] = "Shares of {}".format(stock)
                volume = portfolio.get(stock)
                stock_value["Volume"] = volume
                if date not in stocks[stock].keys():
                    raise DateError("The date is not a trading day")
                else:
                    unit_value = stocks[stock][date][2]
                    stock_value["Val/Unit*"] = unit_value
                    value = volume * unit_value
                    stock_value["Value in Â£*"] = value
                    total_value += value
                    total_stock.append(stock_value)
        if verbose == True:
            print("Your portfolio on {}:".format(date))
            print("[* share values based on the lowest price on {}]\n".format(date))
            print("{0:<22} | {1} | {2} | {3:^8}".format("Capital type","Volume","Val/Unit*","Value in Â£*"))
            print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11+ "+" + "-" * 13)
            for items in total_stock:
                print("{Capital type:<22} | {Volume:>6} | {Val/Unit*:9.2f} | {Value in Â£*: 11.2f}".format(**items))
            print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11+ "+" + "-" * 13)
            print("TOTAL VALUE{:>46.2f}".format(total_value))
        return total_value
def addTransaction(trans,verbose=False):
    date = normaliseDate(trans.get('date'))
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
        if portfolio.get(symbol) + volume !=0:
            portfolio[symbol] = portfolio.get(symbol) + volume
        else:
            del portfolio[symbol]
    else:
        portfolio[symbol] = volume
    transactions.append(trans)
    if verbose == True:
        args = [date, 'Sold' if volume<0 else 'Bought',abs(volume), symbol, abs(total_price),'Available' if volume<0 else 'Remaining',cash]
        trans_info = "{}: {} {} shares of {} for a total of {} \n{} cash: Â£ {:.2f}".format(*args)
        print(trans_info)
    return
def savePortfolio(fname="portfolio.csv"):
    """
    input string `fname`(including ".csv")
    save the updated dictionary `portfolio` to csv, named `fname`
    """
    with open (fname, mode="wt",encoding="utf8") as csv_file:
        f_writer = csv.writer(csv_file)
        for key, value in portfolio.items():
            f_writer.writerow([key, value])
def sellAll(date=None, verbose=False):
    if date is None:
        date = portfolio.get('date')
    date = normaliseDate(date)
    for key in portfolio.copy():
        if key in stocks.keys():
            key_trans = {'date' : date, 'symbol' : key, 'volume' :-portfolio[key]}
            addTransaction(key_trans,verbose)
    return
def loadAllStocks():
    all_file = [file for file in os.listdir('stockdata')if isfile(join('stockdata',file)) and re.search('\.csv',file)]
    for x in all_file:
        try:
            x = re.sub('\.csv$','',x)
            loadStock(x)
        except ValueError:
            pass
    return
def H(s,j):
    first_dict = next (iter (stocks.values()))
    trading_day = list(first_dict.keys())
    trade_date = trading_day[j]
    high_price = stocks.get(s).get(trade_date)[1]
    return high_price
def Q_buy(s,j):
    if j >= 9:
        denominator = 0
        for i in range(0,10):
            denominator += H(s,j-i)
        answer = 10 * H(s,j)/denominator
    else:
        answer = 0
    return answer
def L(s,j):
    first_dict = next (iter (stocks.values()))
    trading_day = list(first_dict.keys())
    trade_date = trading_day[j]
    low_price = stocks.get(s).get(trade_date)[2]
    return low_price
def tradeStrategy1(verbose=True):
    first_dict = next (iter (stocks.values()))
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
        sym_list = sorted(stocks.keys(), key= lambda s:(-Q_buy(s,j),str.upper))
        for x in sym_list:
            print(x,Q_buy(x,j))
        sym = sym_list[0]
        unit_value = stocks[sym][trading_day[j]][1]
        vol = math.floor(cash/unit_value)
        trans = {'date': trading_day[j],'symbol': sym, 'volume': vol}
        addTransaction(trans,True)
        k = j + 1
        while k< len(trading_day):
            if L(sym,k)/ H(sym,j) > 1.3 or L(sym,k)/ H(sym,j) < 0.7:
                sell_trans = {'date':trading_day[k],'symbol':sym,'volume':-vol}
                addTransaction(sell_trans,True)
                break
            k += 1
        j = k + 1
    return
def trading_day_index(date):
    date = normaliseDate(date)
    first_dict = next (iter (stocks.values()))
    trading_day = list(first_dict.keys())
    return trading_day.index(date)
def predict_stock(symbol,start_date,end_date,predict_duration,buy=True,verbose=True):
    symbol = symbol.upper()
    start_date = normaliseDate(start_date)
    end_date = normaliseDate(end_date)
    i = trading_day_index(end_date)
    price_stocks = dict()
    try:
        for day in stocks[symbol].keys():
            if day >= start_date and day <= end_date:
                if buy == True:
                    price_stocks[day] = stocks[symbol][day][1]
                else:
                    price_stocks[day] = stocks[symbol][day][2]
        if verbose == True:
            plt.plot(*zip(*sorted(price_stocks.items())))
            plt.title("The high stock price of {} during {} and {}".format(symbol,start_date,end_date))
            plt.show()
        df= pd.DataFrame(price_stocks,index=[0])
        df.index = pd.to_datetime(df.index)
        ts = df.iloc[0]
        ts.head().index
        ts_log = np.log(ts)
        log_price_matrix = ts_log.as_matrix()
        if verbose == True:
            plt.plot(*zip(*sorted(ts_log.items())))
            plt.title("The high stock price of {} after log transformation during {} and {}".format(symbol,start_date,end_date))
            plt.show()
        model = ARIMA(log_price_matrix,order=(1,1,0))
        model_fit = model.fit(disp=0)
        predictions = model_fit.predict(i+1,i+predict_duration,typ='levels')
        actual_predictions = np.exp(predictions)
        if verbose == True:
            print(model_fit.summary())
            plt.plot(actual_predictions)
            plt.title("The prection of high stock price of {} in next {} days".format(symbol,predict_duration))
            plt.show()
    except KeyError:
        raise FileNotFoundError("The corresponding company data is not contained in stockdata")
    return actual_predictions
def price_increase(symbol,date,verbose=False):
    symbol = symbol.upper()
    loadStock(symbol)
    first_dict = next (iter (stocks.values()))
    trading_day = list(first_dict.keys())
    if trading_day_index(date) > 20:
        start_date=trading_day[trading_day_index(date)-15]
    else:
        start_date=trading_day[10]
    actual_predictions = predict_stock(symbol,start_date,end_date=date,predict_duration=5,buy=True,verbose=False)
    if all(x <= y for x, y in zip(actual_predictions, actual_predictions[1:])):
        return True
    else:
        return False
def buy_stock(symbol,j):
    symbol = symbol.upper()
    loadStock(symbol)
    first_dict = next (iter (stocks.values()))
    trading_day = list(first_dict.keys())
    date = trading_day[j]
    if trading_day_index(date) > 20:
        start_date=trading_day[trading_day_index(date)-15]
    else:
        start_date=trading_day[10]
    date = trading_day[j]
    actual_predictions = predict_stock(symbol,start_date,end_date=date,predict_duration=5,buy=True,verbose=False)
    increase = float(actual_predictions[4])-float(actual_predictions[0])
    return increase
def price_decrease(symbol,date,verbose=False):
    symbol = symbol.upper()
    loadStock(symbol)
    first_dict = next (iter (stocks.values()))
    trading_day = list(first_dict.keys())
    if trading_day_index(date) > 20:
        start_date=trading_day[trading_day_index(date)-15]
    else:
        start_date=trading_day[10]
    actual_predictions = predict_stock(symbol,start_date,end_date=date,predict_duration=5,buy=False,verbose=False)
    if all(x >= y for x, y in zip(actual_predictions, actual_predictions[1:])):
        return True
    else:
        return False
def sell_stock(symbol,j):
    symbol = symbol.upper()
    loadStock(symbol)
    first_dict = next (iter (stocks.values()))
    trading_day = list(first_dict.keys())
    date = trading_day[j]
    if trading_day_index(date) > 20:
        start_date=trading_day[trading_day_index(date)-15]
    else:
        start_date=trading_day[10]
    date = trading_day[j]
    actual_predictions = predict_stock(symbol,start_date,end_date=date,predict_duration=5,buy=False,verbose=False)
    decrease_rate = float(actual_predictions[4])/float(actual_predictions[0])
    if decrease_rate > 1.1 or decrease_rate < 0.9:
        return True
    else:
        return False
def tradeStrategy2(verbose=True):
    first_dict = next (iter (stocks.values()))
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
        increase_stock_list = list()
        for stock in stocks.keys():
            if price_increase(stock,date=trading_day[j],verbose=False) is True:
                increase_stock_list.append(stock)
        buy_stock_list = sorted(increase_stock_list, key= lambda s:-buy_stock(s,j))
        if len(buy_stock_list) == 0:
            pass
        else:
            sym = buy_stock_list[0]
            unit_value = stocks[sym][trading_day[j]][1]
            vol = math.floor(cash/unit_value)
            trans = {'date': trading_day[j],'symbol': sym, 'volume': vol}
            addTransaction(trans,True)
            k = j + 30
            while k< len(trading_day):
                if price_decrease(sym,date=trading_day[k],verbose=False) is True:
                    sell_trans = {'date':trading_day[k],'symbol':sym,'volume':-vol}
                    addTransaction(sell_trans,True)
                    break
                k += 1
            j = k + 20
    return
def main():
    """
    s = '8.5.2012'
    print(normaliseDate(s))
    symbol = "ezj"
    pprint(loadStock(symbol))
    print(loadPortfolio())
    print(valuatePortfolio('2012-2-6', True))
    print(addTransaction({ 'date':'2013-08-12', 'symbol':'SKY', 'volume':-5 }, True))
    fname = "portfolio5.csv"
    savePortfolio(fname)
    sellAll(verbose=True)
    loadAllStocks()
    print(H('BATS',1))
    print(L('SKY',1))
    print( Q_buy('SKY',0))
    """
    loadPortfolio('portfolio0.csv')
    loadAllStocks()
    tradeStrategy1(verbose=True)
    valuatePortfolio(date="2018-03-13", verbose=True)
    """
    loadPortfolio('portfolio0.csv')
    loadAllStocks()
    valuatePortfolio(date='2012-01-01',verbose=True)
    tradeStrategy2(verbose=True)
    valuatePortfolio(date="2018-03-13", verbose=True)
if __name__ == '__main__' or __name__ == 'builtins':
    main()
"""