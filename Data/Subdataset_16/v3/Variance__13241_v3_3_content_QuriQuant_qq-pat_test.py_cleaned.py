import pandas as pd
from pandas_datareader import data
import datetime
import qqpat
def fonk1(b5, b6, b7):
    return {ticker: data.DataReader(ticker, 'yahoo', b1 = b6, end=b7) for ticker in b5}
def fonk2(b8):
    return pd.concat([b8[ticker]['Close'] for ticker in b8], b2 = 1, keys=b8.keys())
def fonk3(b11):
    for idx, statistics in enumerate(b11):
        print(f"\nStatistics for system {idx}:")
        for stat, value in statistics.items():
            print(f"{stat}: {value}")
def fonk4(b10):
    b10.plot_analysis_returns()
    b10.min_variance_portfolio_optimization(b3 = True)
    b10.plot_mc_wc_evolution_sharpe(b4 = 0, iterations=50, confidence=99, max_period_length=1000)
    b10.plot_mc_wc_evolution_cagr(b4 = 0, iterations=50, confidence=99, max_period_length=1000)
    b10.plot_mc_distributions(b4 = 0, iterations=100)
    b10.plot_mc_simulations(b4 = 0, iterations=100)
    b10.plot_analysis_rolling()
    b10.plot_monthly_returns_heatmap()
    b10.plot_annual_returns()
    b10.plot_monthly_return_distribution()
    b10.plot_drawdown_periods()
    b10.plot_drawdown_distribution()
    b10.plot_drawdown_length_distribution()
def fonk5():
    b5 = ['AAPL', 'SPY', 'IBM']
    b6 = datetime.datetime(2016, 1, 1)
    b7 = datetime.datetime.now()
    b8 = fonk1(b5, b6, b7)
    b9 = fonk2(b8)
    b10 = qqpat.Analizer(b9, column_type='price', titles=b5)
    b11 = b10.get_statistics_summary()
    fonk3(b11)
    fonk4(b10)
if b12 = = "__main__":
    fonk5()