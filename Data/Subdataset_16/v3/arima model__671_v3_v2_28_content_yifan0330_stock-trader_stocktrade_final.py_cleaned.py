
import stocktrader
def fonk1():
    print("Loading portfolio from 'portfolio.csv'...")
    stocktrader.loadPortfolio('portfolio.csv')
    print("Loading all historical stock data...")
    stocktrader.loadAllStocks()
def fonk2(date):
    print(f"Evaluating the portfolio on {date}...")
    b1 = stocktrader.valuatePortfolio(date=date, b2=True)
    print(f"Total portfolio value on {date}: {b1:.2f}")
    return b1
def fonk3():
    print("Executing Strategy 1: Buy as much as possible and sell all")
    stocktrader.tradeStrategy1(b2 = True)
    print("Executing Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
    stocktrader.tradeStrategy2(b2 = True)
def fonk4(filename):
    print(f"Saving updated portfolio to '{filename}'...")
    stocktrader.savePortfolio(filename)
def fonk5():
    fonk1()
    b3 = '2024-03-28'
    fonk2(b3)
    fonk3()
    fonk4('updated_portfolio.csv')
    print("Script execution completed. You can now perform additional analyses if needed.")
if b4 = = "__main__":
    fonk5()