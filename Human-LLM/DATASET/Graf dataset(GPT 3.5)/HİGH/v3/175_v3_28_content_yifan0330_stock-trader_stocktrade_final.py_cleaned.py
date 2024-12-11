import stocktrader
def fonk1():
    stocktrader.loadPortfolio('portfolio.csv')
    stocktrader.loadAllStocks()
    b1 = '2024-03-28'
    b2 = stocktrader.valuatePortfolio(date=b1, b3=True)
    print("Total portfolio value on {}: {:.2f}".format(b1, b2))
    fonk2()
    fonk3()
def fonk2():
    print("\nExecuting Strategy 1: Buy as much as possible and sell all")
    stocktrader.tradeStrategy1(b3 = True)
    print("\nExecuting Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
    stocktrader.tradeStrategy2(b3 = True)
def fonk3():
    print("\nSaving updated portfolio...")
    stocktrader.savePortfolio('updated_portfolio.csv')
if b4 = = "__main__":
    fonk1()