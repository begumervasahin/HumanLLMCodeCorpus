import stocktrader
def main():
    stocktrader.loadPortfolio('portfolio.csv')
    stocktrader.loadAllStocks()
    valuation_date = '2024-03-28'
    total_value = stocktrader.valuatePortfolio(date=valuation_date, verbose=True)
    print("Total portfolio value on {}: {:.2f}".format(valuation_date, total_value))
    execute_trading_strategies()
    save_updated_portfolio()
def execute_trading_strategies():
    print("\nExecuting Strategy 1: Buy as much as possible and sell all")
    stocktrader.tradeStrategy1(verbose=True)
    print("\nExecuting Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
    stocktrader.tradeStrategy2(verbose=True)
def save_updated_portfolio():
    print("\nSaving updated portfolio...")
    stocktrader.savePortfolio('updated_portfolio.csv')
if __name__ == "__main__":
    main()