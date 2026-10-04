import pandas as pd
from pandas_datareader import data
import datetime
import qqpat
def fonk1(b3, b4, b5):
    b1 = {ticker: data.DataReader(ticker, 'yahoo', start=b4, end=b5) for ticker in b3}
    return b1
def fonk2(b1):
    b2 = pd.concat([b1[ticker]['Close'] for ticker in b1], axis=1, keys=b1.keys())
    return b2
def fonk3(b7):
    for idx, statistics in enumerate(b7):
        print(f"\nStatistics for system {idx}:")
        for stat, value in statistics.items():
            print(f"{stat}: {value}")
def fonk4():
    b3 = ['AAPL', 'SPY', 'IBM']
    b4 = datetime.datetime(2016, 1, 1)
    b5 = datetime.datetime.now()
    b1 = fonk1(b3, b4, b5)
    b2 = fonk2(b1)
    b6 = qqpat.Analizer(b2, column_type='price', titles=b3)
    b7 = b6.get_statistics_summary()
    fonk3(b7)
    b6.plot_analysis_returns()
    b6.min_variance_portfolio_optimization(b8 = True)
    b6.plot_mc_wc_evolution_sharpe(b9 = 0, iterations=50, confidence=99, max_period_length=1000)
    b6.plot_mc_wc_evolution_cagr(b9 = 0, iterations=50, confidence=99, max_period_length=1000)
    b6.plot_mc_distributions(b9 = 0, iterations=100)
    b6.plot_mc_simulations(b9 = 0, iterations=100)
    b6.plot_analysis_rolling()
    b6.plot_monthly_returns_heatmap()
    b6.plot_annual_returns()
    b6.plot_monthly_return_distribution()
    b6.plot_drawdown_periods()
    b6.plot_drawdown_distribution()
    b6.plot_drawdown_length_distribution()
if b10 = = "__main__":
    fonk4()