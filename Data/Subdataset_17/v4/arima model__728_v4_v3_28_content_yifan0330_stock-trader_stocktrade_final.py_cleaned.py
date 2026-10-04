import stocktrader
def main():
    portfolio_file = 'portfolio.csv'
    valuation_date = '2024-03-28'
    updated_portfolio_file = 'updated_portfolio.csv'
    stocktrader.loadPortfolio(portfolio_file)
    stocktrader.loadAllStocks()
    total_value = evaluate_portfolio(valuation_date)
    print(f"Total portfolio value on {valuation_date}: {total_value:.2f}")
    execute_trading_strategies()
    save_updated_portfolio(updated_portfolio_file)
def evaluate_portfolio(date):
    return stocktrader.valuatePortfolio(date=date, verbose=True)
def execute_trading_strategies():
    print("\nExecuting Strategy 1: Buy as much as possible and sell all")
    stocktrader.tradeStrategy1(verbose=True)
    print("\nExecuting Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
    stocktrader.tradeStrategy2(verbose=True)
def save_updated_portfolio(filename):
    print("\nSaving updated portfolio...")
    stocktrader.savePortfolio(filename)
if __name__ == "__main__":
    main()