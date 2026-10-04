import stocktrader
def fonk1():
    b1 = 'portfolio.csv'
    b2 = 'updated_portfolio.csv'
    b3 = '2024-03-28'
    fonk2(b1)
    fonk3()
    b4 = fonk4(b3)
    print(f"Total portfolio value on {b3}: {b4:.2f}")
    fonk5()
    fonk6(b2)
    print(f"Updated portfolio saved to {b2}")
def fonk2(file_path):
    print(f"Loading portfolio from {file_path}")
    stocktrader.loadPortfolio(file_path)
def fonk3():
    print("Loading historical stock data for all stocks")
    stocktrader.loadAllStocks()
def fonk4(b5):
    print(f"Evaluating portfolio value on {b5}")
    return stocktrader.valuatePortfolio(b5 = b5, b6=True)
def fonk5():
    print("Executing Strategy 1: Buy as much as possible and sell all")
    stocktrader.tradeStrategy1(b6 = True)
    print("Executing Strategy 2: Buy predicted gainers and sell predicted losers")
    stocktrader.tradeStrategy2(b6 = True)
def fonk6(file_path):
    print(f"Saving updated portfolio to {file_path}")
    stocktrader.savePortfolio(file_path)
if b7 = = "__main__":
    fonk1()