import pandas as pd
from pandas_datareader import b6
import datetime
import qqpat
b1 = datetime.datetime(2016, 1, 1)
b2 = datetime.datetime.now()
b3 = b6.DataReader('AAPL', 'yahoo', start=b1, end=b2)
b4 = b6.DataReader('SPY', 'yahoo', start=b1, end=b2)
b5 = b6.DataReader('IBM', 'yahoo', start=b1, end=b2)
b6 = pd.concat([b3['Close'], b4['Close'], b5['Close']], axis=1)
b6.b7 = ["AAPL", "SPY", "IBM"]
b8 = qqpat.Analizer(b6, column_type='price', titles=["AAPL", "SPY", "IBM"])
b9 = b8.get_statistics_summary()
for idx, statistics in enumerate(b9):
    print("\nStatistics for system {}:".format(idx))
    for s in statistics:
        print("{}: {}".format(s, b9[idx][s]))
    print("")
b8.plot_analysis_returns()
b8.min_variance_portfolio_optimization(b10 = True)
b8.plot_mc_wc_evolution_sharpe(b11 = 0, iterations=50, confidence=99, max_period_length=1000)
b8.plot_mc_wc_evolution_cagr(b11 = 0, iterations=50, confidence=99, max_period_length=1000)
b8.plot_mc_distributions(b11 = 0, iterations=100)
b8.plot_mc_simulations(b11 = 0, iterations=100)
b8.plot_analysis_rolling()
b8.plot_monthly_returns_heatmap()
b8.plot_annual_returns()
b8.plot_monthly_returns()
b8.plot_monthly_return_distribution()
b8.plot_drawdown_periods()
b8.plot_drawdown_distribution()
b8.plot_drawdown_length_distribution()