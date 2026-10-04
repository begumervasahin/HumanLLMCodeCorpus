import pandas as pd
from pandas_datareader import b7
import datetime
import qqpat
def fonk1(ticker, b2, b3):
    return b7.DataReader(ticker, 'yahoo', b1 = b2, end=b3)
def fonk2(b10):
    for idx, statistics in enumerate(b10):
        print("\nStatistics for system {}:".format(idx))
        for stat, value in statistics.items():
            print("{}: {}".format(stat, value))
        print("")
def fonk3():
    b2 = datetime.datetime(2016, 1, 1)
    b3 = datetime.datetime.now()
    b4 = fonk1('AAPL', b2, b3)
    b5 = fonk1('SPY', b2, b3)
    b6 = fonk1('IBM', b2, b3)
    b7 = pd.concat([b4['Close'], b5['Close'], b6['Close']], axis=1)
    b7.b8 = ["AAPL", "SPY", "IBM"]
    b9 = qqpat.Analizer(b7, column_type='price', titles=["AAPL", "SPY", "IBM"])
    b10 = b9.get_statistics_summary()
    fonk2(b10)
    b9.plot_analysis_returns()
    b9.min_variance_portfolio_optimization(b11 = True)
    b9.plot_mc_wc_evolution_sharpe(b12 = 0, iterations=50, confidence=99, max_period_length=1000)
    b9.plot_mc_wc_evolution_cagr(b12 = 0, iterations=50, confidence=99, max_period_length=1000)
    b9.plot_mc_distributions(b12 = 0, iterations=100)
    b9.plot_mc_simulations(b12 = 0, iterations=100)
    b9.plot_analysis_rolling()
    b9.plot_monthly_returns_heatmap()
    b9.plot_annual_returns()
    b9.plot_monthly_returns()
    b9.plot_monthly_return_distribution()
    b9.plot_drawdown_periods()
    b9.plot_drawdown_distribution()
    b9.plot_drawdown_length_distribution()
if b13 = = "__main__":
    fonk3()