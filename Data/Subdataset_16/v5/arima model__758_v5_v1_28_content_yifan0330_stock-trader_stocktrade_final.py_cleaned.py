import stocktrader
def fonk1():
    fonk2()
    b1 = '2024-03-28'
    b2 = fonk3(b1)
    print(f"Total portfolio value on {b1}: {b2:.2f}")
    fonk4()
    fonk5()
def fonk2():
    stocktrader.loadPortfolio('portfolio.csv')
    stocktrader.loadAllStocks()
def fonk3(b3):
    return stocktrader.valuatePortfolio(b3 = b3, b4=True)
def fonk4():
    stocktrader.tradeStrategy1(b4 = True)
    stocktrader.tradeStrategy2(b4 = True)
def fonk5():
    stocktrader.savePortfolio('updated_portfolio.csv')
if b5 = = "__main__":
    fonk1()