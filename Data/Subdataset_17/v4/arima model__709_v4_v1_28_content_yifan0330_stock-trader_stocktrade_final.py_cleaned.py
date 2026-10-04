import stocktrader
stocktrader.loadPortfolio('portfolio.csv')
stocktrader.loadAllStocks()
valuation_date = '2024-03-28'
total_value = stocktrader.valuatePortfolio(date=valuation_date, verbose=True)
print(f"Total portfolio value on {valuation_date}: {total_value:.2f}")
stocktrader.tradeStrategy1(verbose=True)
stocktrader.tradeStrategy2(verbose=True)
stocktrader.savePortfolio('updated_portfolio.csv')
