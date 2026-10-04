import pandas as pd
from pandas_datareader import b4
import datetime
import qqpat
b1 = b4.DataReader('AAPL','yahoo',start=datetime.datetime(2016, 1, 1),end=datetime.datetime.now())
b2 = b4.DataReader('SPY','yahoo',start=datetime.datetime(2016, 1, 1),end=datetime.datetime.now())
b3 = b4.DataReader('IBM','yahoo',start=datetime.datetime(2016, 1, 1),end=datetime.datetime.now())
b4 = pd.concat([b1['Close'], b2['Close'], b3['Close']], axis=1)
b5 = qqpat.Analizer(b4, column_type='price', titles=["APPL", "SPY", "IBM"])
b6 = b5.get_statistics_summary()
for idx, statistics in enumerate(b6):
    print ("")
    print ("statistics for system {}:".format(idx))
    for s in statistics:
        print ("{}: {}".format(s, b6[idx][s]))
    print ("")
b5.plot_analysis_returns()
b5.min_variance_portfolio_optimization(b7 = True)
b5.plot_mc_wc_evolution_sharpe(b8 = 0, iterations=50, confidence=99, max_period_length=1000)
b5.plot_mc_wc_evolution_cagr(b8 = 0, iterations=50, confidence=99, max_period_length=1000)
b5.plot_mc_distributions(b8 = 0, iterations=100)
b5.plot_mc_simulations(b8 = 0, iterations=100)
b5.plot_analysis_rolling()
b5.plot_monthly_returns_heatmap()
b5.plot_annual_returns()
b5.plot_monthly_returns()
b5.plot_annual_returns()
b5.plot_monthly_return_distribution()
b5.plot_drawdown_periods()
b5.plot_drawdown_distribution()
b5.plot_drawdown_length_distribution()