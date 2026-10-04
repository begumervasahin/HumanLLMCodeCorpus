import stocktrader
def main():
    portfolio_file = 'portfolio.csv'
    updated_portfolio_file = 'updated_portfolio.csv'
    valuation_date = '2024-03-28'
    load_portfolio(portfolio_file)
    load_historical_stock_data()
    total_value = evaluate_portfolio(valuation_date)
    print(f"Total portfolio value on {valuation_date}: {total_value:.2f}")
    execute_trading_strategies()
    save_updated_portfolio(updated_portfolio_file)
    print(f"Updated portfolio saved to {updated_portfolio_file}")
def load_portfolio(file_path):
    print(f"Loading portfolio from {file_path}")
    stocktrader.loadPortfolio(file_path)
def load_historical_stock_data():
    print("Loading historical stock data for all stocks")
    stocktrader.loadAllStocks()
def evaluate_portfolio(date):
    print(f"Evaluating portfolio value on {date}")
    return stocktrader.valuatePortfolio(date=date, verbose=True)
def execute_trading_strategies():
    print("Executing Strategy 1: Buy as much as possible and sell all")
    stocktrader.tradeStrategy1(verbose=True)
    print("Executing Strategy 2: Buy predicted gainers and sell predicted losers")
    stocktrader.tradeStrategy2(verbose=True)
def save_updated_portfolio(file_path):
    print(f"Saving updated portfolio to {file_path}")
    stocktrader.savePortfolio(file_path)
if __name__ == "__main__":
    main()