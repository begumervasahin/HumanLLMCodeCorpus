import pandas as pd
from pandas_datareader import data
import datetime
import qqpat
def fetch_stock_data(tickers, start_date, end_date):
    return {ticker: data.DataReader(ticker, 'yahoo', start=start_date, end=end_date) for ticker in tickers}
def concatenate_close_prices(stock_data):
    return pd.concat([stock_data[ticker]['Close'] for ticker in stock_data], axis=1, keys=stock_data.keys())
def print_statistics_summary(summary):
    for idx, statistics in enumerate(summary):
        print(f"\nStatistics for system {idx}:")
        for stat, value in statistics.items():
            print(f"{stat}: {value}")
def analyze_and_plot(analyzer):
    analyzer.plot_analysis_returns()
    analyzer.min_variance_portfolio_optimization(plotWeights=True)
    analyzer.plot_mc_wc_evolution_sharpe(index=0, iterations=50, confidence=99, max_period_length=1000)
    analyzer.plot_mc_wc_evolution_cagr(index=0, iterations=50, confidence=99, max_period_length=1000)
    analyzer.plot_mc_distributions(index=0, iterations=100)
    analyzer.plot_mc_simulations(index=0, iterations=100)
    analyzer.plot_analysis_rolling()
    analyzer.plot_monthly_returns_heatmap()
    analyzer.plot_annual_returns()
    analyzer.plot_monthly_return_distribution()
    analyzer.plot_drawdown_periods()
    analyzer.plot_drawdown_distribution()
    analyzer.plot_drawdown_length_distribution()
def main():
    tickers = ['AAPL', 'SPY', 'IBM']
    start_date = datetime.datetime(2016, 1, 1)
    end_date = datetime.datetime.now()
    stock_data = fetch_stock_data(tickers, start_date, end_date)
    close_prices = concatenate_close_prices(stock_data)
    analyzer = qqpat.Analizer(close_prices, column_type='price', titles=tickers)
    summary = analyzer.get_statistics_summary()
    print_statistics_summary(summary)
    analyze_and_plot(analyzer)
if __name__ == "__main__":
    main()