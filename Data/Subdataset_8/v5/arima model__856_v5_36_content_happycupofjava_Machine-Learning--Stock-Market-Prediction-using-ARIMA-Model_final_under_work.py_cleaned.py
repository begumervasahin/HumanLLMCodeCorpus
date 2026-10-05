import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
plt.rcParams['figure.figsize'] = (15, 6)
plt.style.use('seaborn-darkgrid')
def load_data():
    print('\nEnter the symbol for the company of interest:')
    print('[GOOGL: Google, FB: Facebook] (Type "quit" to exit)\n')
    symbol = input('Enter choice (GOOGL, FB, or quit): ').lower()
    if symbol == 'quit':
        print('Exiting...')
        return None
    filename = 'WIKI-GOOGL.csv' if symbol == 'googl' else 'facebook.csv'
    try:
        stock_data = pd.read_csv(filename, parse_dates=['Date'], index_col='Date')
        print(stock_data.head())
        print('\nData Types:\n', stock_data.dtypes)
        return stock_data
    except FileNotFoundError:
        print('File not found. Please make sure the data file exists.')
        return None
def plot_time_series(series):
    plt.figure()
    plt.plot(series)
    plt.title('Time Series Plot')
    plt.show()
def test_stationarity(timeseries):
    rolling_mean = timeseries.rolling(window=20).mean()
    rolling_std = timeseries.rolling(window=20).std()
    plt.plot(timeseries, color='blue', label='Original')
    plt.plot(rolling_mean, color='red', label='Rolling Mean')
    plt.plot(rolling_std, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '
    for key, value in dftest[4].items():
        dfoutput[f'Critical Value ({key})'] = value
    print(dfoutput)
def decompose_series(series):
    decomposition = seasonal_decompose(series, model='additive', period=52)
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    plt.figure(figsize=(14, 7))
    plt.subplot(411)
    plt.plot(series, label='Original', color='blue')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend, label='Trend', color='red')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal, label='Seasonality', color='green')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual, label='Residuals', color='black')
    plt.legend(loc='best')
    plt.tight_layout()
def plot_acf_pacf(series_diff):
    lag_acf = acf(series_diff, nlags=20)
    lag_pacf = pacf(series_diff, nlags=20, method='ols')
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.plot(lag_acf)
    plt.axhline(y=0, linestyle='--', color='gray')
    plt.axhline(y=-1.96/np.sqrt(len(series_diff)), linestyle='--', color='gray')
    plt.axhline(y=1.96/np.sqrt(len(series_diff)), linestyle='--', color='gray')
    plt.title('Autocorrelation Function')
    plt.subplot(122)
    plt.plot(lag_pacf)
    plt.axhline(y=0, linestyle='--', color='gray')
    plt.axhline(y=-1.96/np.sqrt(len(series_diff)), linestyle='--', color='gray')
    plt.axhline(y=1.96/np.sqrt(len(series_diff)), linestyle='--', color='gray')
    plt.title('Partial Autocorrelation Function')
    plt.tight_layout()
    plt.show()
def main():
    stock_data = load_data()
    if stock_data is None:
        return
    series = stock_data['Adj Close']
    plot_time_series(series)
    test_stationarity(series)
    series_log = np.log(series)
    series_log_diff = series_log - series_log.shift()
    series_log_diff.dropna(inplace=True)
    test_stationarity(series_log_diff)
    decompose_series(series_log)
    plot_acf_pacf(series_log_diff)
if __name__ == "__main__":
    main()