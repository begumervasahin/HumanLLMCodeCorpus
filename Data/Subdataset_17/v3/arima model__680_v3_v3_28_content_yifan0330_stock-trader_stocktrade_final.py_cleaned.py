import stocktrader
def main():
    portfolio_file = 'portfolio.csv'
    updated_portfolio_file = 'updated_portfolio.csv'
    valuation_date = '2024-03-28'
    load_portfolio_data(portfolio_file)
    evaluate_portfolio(valuation_date)
    execute_trading_strategies()
    save_portfolio_data(updated_portfolio_file)
def load_portfolio_data(file_path):
    stocktrader.loadPortfolio(file_path)
    stocktrader.loadAllStocks()
def evaluate_portfolio(date):
    total_value = stocktrader.valuatePortfolio(date=date, verbose=True)
    print(f"Total portfolio value on {date}: {total_value:.2f}")
def execute_trading_strategies():
    execute_strategy(stocktrader.tradeStrategy1, "Strategy 1: Buy as much as possible and sell all")
    execute_strategy(stocktrader.tradeStrategy2, "Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
def execute_strategy(strategy_function, strategy_description):
    print(f"\nExecuting {strategy_description}")
    strategy_function(verbose=True)
def save_portfolio_data(file_path):
    print("\nSaving updated portfolio...")
    stocktrader.savePortfolio(file_path)
if __name__ == "__main__":
    main()