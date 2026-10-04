import stocktrader
stocktrader.loadPortfolio('portfolio.csv')
stocktrader.loadAllStocks()
b1 = '2024-03-28'
b2 = stocktrader.valuatePortfolio(date=b1, b3=True)
print(f"Total portfolio value on {b1}: {b2:.2f}")
stocktrader.tradeStrategy1(b3 = True)
stocktrader.tradeStrategy2(b3 = True)
stocktrader.savePortfolio('updated_portfolio.csv')
