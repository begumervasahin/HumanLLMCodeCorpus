
import stocktrader
def load_data():
    print("Loading portfolio from 'portfolio.csv'...")
    stocktrader.loadPortfolio('portfolio.csv')
    print("Loading all historical stock data...")
    stocktrader.loadAllStocks()
def evaluate_portfolio(date):
    print(f"Evaluating the portfolio on {date}...")
    total_value = stocktrader.valuatePortfolio(date=date, verbose=True)
    print(f"Total portfolio value on {date}: {total_value:.2f}")
    return total_value
def execute_trading_strategies():
    print("Executing Strategy 1: Buy as much as possible and sell all")
    stocktrader.tradeStrategy1(verbose=True)
    print("Executing Strategy 2: Buy stocks predicted to increase in price and sell when predicted to decrease")
    stocktrader.tradeStrategy2(verbose=True)
def save_portfolio(filename):
    print(f"Saving updated portfolio to '{filename}'...")
    stocktrader.savePortfolio(filename)
def main():
    load_data()
    valuation_date = '2024-03-28'
    evaluate_portfolio(valuation_date)
    execute_trading_strategies()
    save_portfolio('updated_portfolio.csv')
    print("Script execution completed. You can now perform additional analyses if needed.")
if __name__ == "__main__":
    main()