import pandas as pd
from pandas_datareader import data
import datetime
import qqpat
def fonk1(b5, b6, b7):
    b1 = {}
    for ticker in b5:
        b1[ticker] = data.DataReader(ticker, 'yahoo', b2 = b6, end=b7)
    return b1
def fonk2(b1):
    b3 = [b1[ticker]['Close'] for ticker in b1]
    return pd.concat(b3, b4 = 1, keys=b1.keys())
def fonk3(b9):
    for idx, statistics in enumerate(b9):
        print(f"\nStatistics for system {idx}:")
        for stat, value in statistics.items():
            print(f"{stat}: {value}")
        print("")
def fonk4():
    b5 = ['AAPL', 'SPY', 'IBM']
    b6 = datetime.datetime(2016, 1, 1)
    b7 = datetime.datetime.now()
    b1 = fonk1(b5, b6, b7)
    b3 = fonk2(b1)
    b8 = qqpat.Analizer(b3, column_type='price', titles=b5)
    b9 = b8.get_statistics_summary()
    fonk3(b9)
    b8.plot_analysis_returns()
    b8.min_variance_portfolio_optimization(b10 = True)
    b8.plot_mc_wc_evolution_sharpe(b11 = 0, iterations=50, confidence=99, max_period_length=1000)
    b8.plot_mc_wc_evolution_cagr(b11 = 0, iterations=50, confidence=99, max_period_length=1000)
    b8.plot_mc_distributions(b11 = 0, iterations=100)
    b8.plot_mc_simulations(b11 = 0, iterations=100)
    b8.plot_analysis_rolling()
    b8.plot_monthly_returns_heatmap()
    b8.plot_annual_returns()
    b8.plot_monthly_return_distribution()
    b8.plot_drawdown_periods()
    b8.plot_drawdown_distribution()
    b8.plot_drawdown_length_distribution()
if b12 = = "__main__":
    fonk4()