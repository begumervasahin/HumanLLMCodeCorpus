import stocktrader
def fonk1():
    stocktrader.loadPortfolio('portfolio.csv')
    stocktrader.loadAllStocks()
def fonk2(date):
    b1 = stocktrader.valuatePortfolio(date=date, b2=True)
    print(f"Total portfolio value on {date}: {b1:.2f}")
def fonk3():
    print("Executing Strategy 1: Buy as much as possible and sell all")
    stocktrader.tradeStrategy1(b2 = True)
    print("Executing Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
    stocktrader.tradeStrategy2(b2 = True)
def fonk4():
    print("Saving updated portfolio...")
    stocktrader.savePortfolio('updated_portfolio.csv')
def fonk5():
    fonk1()
    b3 = '2024-03-28'
    fonk2(b3)
    fonk3()
    fonk4()
if b4 = = "__main__":
    fonk5()