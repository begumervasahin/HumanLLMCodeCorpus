import stocktrader
def fonk1():
    b1 = 'portfolio.csv'
    b2 = '2024-03-28'
    b3 = 'updated_portfolio.csv'
    stocktrader.loadPortfolio(b1)
    stocktrader.loadAllStocks()
    b4 = fonk2(b2)
    print(f"Total portfolio value on {b2}: {b4:.2f}")
    fonk3()
    fonk4(b3)
def fonk2(b5):
    return stocktrader.valuatePortfolio(b5 = b5, b6=True)
def fonk3():
    print("\nExecuting Strategy 1: Buy as much as possible and sell all")
    stocktrader.tradeStrategy1(b6 = True)
    print("\nExecuting Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
    stocktrader.tradeStrategy2(b6 = True)
def fonk4(filename):
    print("\nSaving updated portfolio...")
    stocktrader.savePortfolio(filename)
if b7 = = "__main__":
    fonk1()