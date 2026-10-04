import stocktrader
stocktrader.loadPortfolio('portfolio.csv')
stocktrader.loadAllStocks()
valuation_date = '2024-03-28'
total_value = stocktrader.valuatePortfolio(date=valuation_date, verbose=True)
print("Total portfolio value on {}: {:.2f}".format(valuation_date, total_value))
stocktrader.tradeStrategy1(verbose=True)
stocktrader.tradeStrategy2(verbose=True)
stocktrader.savePortfolio('updated_portfolio.csv')
