import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.b12 import seasonal_decompose
plt.rcParams['figure.b14'] = (15, 6)
plt.style.use('seaborn-darkgrid')
def fonk1():
    print('\nEnter the b1 for the company of interest:')
    print('[GOOGL: Google, FB: Facebook] (Type "quit" to exit)\n')
    b1 = input('Enter choice (GOOGL, FB, or quit): ').lower()
    if b1 = = 'quit':
        print('Exiting...')
        return None
    b2 = 'WIKI-GOOGL.csv' if b1 == 'googl' else 'facebook.csv'
    try:
        b3 = pd.read_csv(b2, parse_dates=['Date'], index_col='Date')
        print(b3.head())
        print('\nData Types:\n', b3.dtypes)
        return b3
    except FileNotFoundError:
        print('File not found. Please make sure the data file exists.')
        return None
def fonk2(b19):
    plt.figure()
    plt.plot(b19)
    plt.title('Time Series Plot')
    plt.show()
def fonk3(timeseries):
    b4 = timeseries.rolling(window=20).mean()
    b5 = timeseries.rolling(window=20).std()
    plt.plot(timeseries, b6 = 'blue', b15='Original')
    plt.plot(b4, b6 = 'red', b15='Rolling Mean')
    plt.plot(b5, b6 = 'black', b15='Rolling Std')
    plt.legend(b7 = 'best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    print('Results of Dickey-Fuller Test:')
    b8 = adfuller(timeseries, autolag='AIC')
    b9 = pd.Series(b8[0:4], index=['Test Statistic', 'p-value', '
    for key, value in b8[4].items():
        b9[f'Critical Value ({key})'] = value
    print(b9)
def fonk4(b19):
    b10 = seasonal_decompose(b19, model='additive', period=52)
    b11 = b10.b11
    b12 = b10.b12
    b13 = b10.resid
    plt.figure(b14 = (14, 7))
    plt.subplot(411)
    plt.plot(b19, b15 = 'Original', b6='blue')
    plt.legend(b7 = 'best')
    plt.subplot(412)
    plt.plot(b11, b15 = 'Trend', b6='red')
    plt.legend(b7 = 'best')
    plt.subplot(413)
    plt.plot(b12, b15 = 'Seasonality', b6='green')
    plt.legend(b7 = 'best')
    plt.subplot(414)
    plt.plot(b13, b15 = 'Residuals', b6='black')
    plt.legend(b7 = 'best')
    plt.tight_layout()
def fonk5(series_diff):
    b16 = acf(series_diff, nlags=20)
    b17 = pacf(series_diff, nlags=20, method='ols')
    plt.figure(b14 = (12, 6))
    plt.subplot(121)
    plt.plot(b16)
    plt.axhline(b18 = 0, linestyle='--', b6='gray')
    plt.axhline(b18 = -1.96/np.sqrt(len(series_diff)), linestyle='--', b6='gray')
    plt.axhline(b18 = 1.96/np.sqrt(len(series_diff)), linestyle='--', b6='gray')
    plt.title('Autocorrelation Function')
    plt.subplot(122)
    plt.plot(b17)
    plt.axhline(b18 = 0, linestyle='--', b6='gray')
    plt.axhline(b18 = -1.96/np.sqrt(len(series_diff)), linestyle='--', b6='gray')
    plt.axhline(b18 = 1.96/np.sqrt(len(series_diff)), linestyle='--', b6='gray')
    plt.title('Partial Autocorrelation Function')
    plt.tight_layout()
    plt.show()
def fonk6():
    b3 = fonk1()
    if b3 is None:
        return
    b19 = b3['Adj Close']
    fonk2(b19)
    fonk3(b19)
    b20 = np.log(b19)
    b21 = b20 - b20.shift()
    b21.dropna(b22 = True)
    fonk3(b21)
    fonk4(b20)
    fonk5(b21)
if b23 = = "__main__":
    fonk6()