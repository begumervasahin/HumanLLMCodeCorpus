import stocktrader
def fonk1():
    b1 = 'portfolio.csv'
    b2 = '2024-03-28'
    b3 = 'updated_portfolio.csv'
    fonk2(b1)
    b4 = fonk3(b2)
    print(f"Total portfolio value on {b2}: {b4:.2f}")
    fonk4()
    fonk5(b3)
def fonk2(b1):
    stocktrader.loadPortfolio(b1)
    stocktrader.loadAllStocks()
def fonk3(b5):
    return stocktrader.valuatePortfolio(b5 = b5, b6=True)
def fonk4():
    print("\nExecuting Strategy 1: Buy as much as possible and sell all")
    stocktrader.tradeStrategy1(b6 = True)
    print("\nExecuting Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
    stocktrader.tradeStrategy2(b6 = True)
def fonk5(filename):
    print("\nSaving updated portfolio...")
    stocktrader.savePortfolio(filename)
if b7 = = "__main__":
    fonk1()