import stocktrader
stocktrader.loadPortfolio('portfolio.csv')
stocktrader.loadAllStocks()
b1 = '2024-03-28'
b2 = stocktrader.valuatePortfolio(date=b1, b3=True)
print(f"Total portfolio value on {b1}: {b2:.2f}")
print("Executing Strategy 1: Buy as much as possible and sell all")
stocktrader.tradeStrategy1(b3 = True)
print("Executing Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
stocktrader.tradeStrategy2(b3 = True)
print("Saving updated portfolio...")
stocktrader.savePortfolio('updated_portfolio.csv')
