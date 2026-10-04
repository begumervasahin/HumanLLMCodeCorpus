import stocktrader
def fonk1():
    b1 = 'portfolio.csv'
    b2 = 'updated_portfolio.csv'
    b3 = '2024-03-28'
    fonk2(b1)
    fonk3(b3)
    fonk4()
    fonk6(b2)
def fonk2(file_path):
    stocktrader.loadPortfolio(file_path)
    stocktrader.loadAllStocks()
def fonk3(date):
    b4 = stocktrader.valuatePortfolio(date=date, b5=True)
    print(f"Total portfolio value on {date}: {b4:.2f}")
def fonk4():
    fonk5(stocktrader.tradeStrategy1, "Strategy 1: Buy as much as possible and sell all")
    fonk5(stocktrader.tradeStrategy2, "Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
def fonk5(strategy_function, strategy_description):
    print(f"\nExecuting {strategy_description}")
    strategy_function(b5 = True)
def fonk6(file_path):
    print("\nSaving updated portfolio...")
    stocktrader.savePortfolio(file_path)
if b6 = = "__main__":
    fonk1()