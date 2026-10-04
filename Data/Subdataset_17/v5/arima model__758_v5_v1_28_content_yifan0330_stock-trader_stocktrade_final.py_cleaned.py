import stocktrader
def main():
    load_data()
    valuation_date = '2024-03-28'
    total_value = evaluate_portfolio(valuation_date)
    print(f"Total portfolio value on {valuation_date}: {total_value:.2f}")
    execute_trading_strategies()
    save_updated_portfolio()
def load_data():
    stocktrader.loadPortfolio('portfolio.csv')
    stocktrader.loadAllStocks()
def evaluate_portfolio(date):
    return stocktrader.valuatePortfolio(date=date, verbose=True)
def execute_trading_strategies():
    stocktrader.tradeStrategy1(verbose=True)
    stocktrader.tradeStrategy2(verbose=True)
def save_updated_portfolio():
    stocktrader.savePortfolio('updated_portfolio.csv')
if __name__ == "__main__":
    main()