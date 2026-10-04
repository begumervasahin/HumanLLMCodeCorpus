import stocktrader
stocktrader.loadPortfolio('portfolio.csv')
stocktrader.loadAllStocks()
valuation_date = '2024-03-28'
total_value = stocktrader.valuatePortfolio(date=valuation_date, verbose=True)
print(f"Total portfolio value on {valuation_date}: {total_value:.2f}")
print("Executing Strategy 1: Buy as much as possible and sell all")
stocktrader.tradeStrategy1(verbose=True)
print("Executing Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
stocktrader.tradeStrategy2(verbose=True)
print("Saving updated portfolio...")
stocktrader.savePortfolio('updated_portfolio.csv')
