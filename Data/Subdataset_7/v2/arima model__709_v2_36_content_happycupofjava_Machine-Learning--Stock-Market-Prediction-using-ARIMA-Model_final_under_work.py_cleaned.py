import pandas as pd
import numpy as np
import math
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.b17 import seasonal_decompose
from statsmodels.tsa.arima.b23 import ARIMA
from statsmodels.tsa.stattools import acf, pacf
def fonk1():
    print('Welcome! Please choose a company from the following options:')
    print('1: Google')
    print('2: Facebook')
    print('3: Quit')
    b1 = int(input('Enter your b1: '))
    b2 = None
    if b1 = = 1:
        b2 = pd.read_csv('WIKI-GOOGL.csv')
    elif b1 = = 2:
        b2 = pd.read_csv('facebook.csv')
    else:
        print('Invalid b1. Exiting.')
        exit()
    print(b2.head())
    print('\nFeatures and their Data Types:')
    print(b2.dtypes)
    b3 = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
    b2 = pd.read_csv('WIKI-GOOGL.csv', parse_dates=['Date'], index_col='Date', date_parser=b3)
    return b2
def fonk2(b2):
    b4 = b2['Adj Close']
    b4.head(10)
    print(b4['2017'])
    plt.plot(b4)
    return b4
def fonk3(b4):
    b5 = b4.rolling(window=20).mean()
    b6 = b4.rolling(window=20).std()
    print("Plotting Rolling Mean & Standard Deviation:")
    plt.plot(b4, b7 = 'blue', b19='Original')
    plt.plot(b5, b7 = 'red', b19='Rolling Mean')
    plt.plot(b6, b7 = 'black', b19='Rolling Std')
    plt.legend(b8 = 'best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    print('Results of Dickey-Fuller Test:')
    b9 = adfuller(b4, autolag='AIC')
    b10 = pd.Series(b9[0:4], index=['Test Statistic', 'p-value', '
    for key, value in b9[4].items():
        b10['Critical Value (%s)' % key] = value
    print(b10)
def fonk4(b4):
    b11 = np.log(b4)
    plt.plot(b11)
    return b11
def fonk5(b11):
    b12 = b11.rolling(10, min_periods=1).mean()
    print("Smoothing Data:")
    plt.figure(1)
    plt.subplot(211)
    plt.plot(b11, b7 = 'blue', b19='Original')
    plt.plot(b12, b7 = 'red', b19='Moving Average')
    plt.legend()
    plt.show()
    b13 = b11 - b12
    b13.dropna(b14 = True)
    print("Plotting Smoothed Data:")
    plt.subplot(212)
    fonk3(b13)
    plt.show()
    return b12
def fonk6(b11):
    b15 = seasonal_decompose(b11, freq=52)
    b16 = b15.b16
    b17 = b15.b17
    b18 = b15.resid
    plt.subplot(411)
    plt.plot(b11, b19 = 'Original')
    plt.legend(b8 = 'best')
    plt.show()
    plt.subplot(412)
    plt.plot(b16, b19 = 'Trend')
    plt.legend(b8 = 'best')
    plt.show()
    plt.subplot(413)
    plt.plot(b17, b19 = 'Seasonality')
    plt.legend(b8 = 'best')
    plt.show()
    plt.subplot(414)
    plt.plot(b18, b19 = 'Residuals')
    plt.legend(b8 = 'best')
    plt.tight_layout()
    plt.show()
def fonk7(b30):
    b20 = acf(b30, nlags=20)
    b21 = pacf(b30, nlags=20, method='ols')
    print("Plotting Autocorrelation Function (ACF):")
    plt.subplot(121)
    plt.plot(b20)
    plt.axhline(b22 = 0, linestyle='--', b7='gray')
    plt.title('Autocorrelation Function')
    plt.show()
    print("Plotting Partial Autocorrelation Function (PACF):")
    plt.subplot(122)
    plt.plot(b21)
    plt.axhline(b22 = 0, linestyle='--', b7='gray')
    plt.title('Partial Autocorrelation Function')
    plt.tight_layout()
    plt.show()
def fonk8(b11, b30):
    b23 = ARIMA(b11, order=(2, 1, 0))
    b24 = b23.fit()
    plt.plot(b30)
    plt.plot(b24.fittedvalues, b7 = 'red')
    plt.title('AR Model: Residual Sum of Squares (RSS): %.4f' % sum((b24.fittedvalues - b30) ** 2))
    plt.show()
def fonk9(b11, b30):
    b23 = ARIMA(b11, order=(0, 1, 2))
    b25 = b23.fit()
    plt.plot(b30)
    plt.plot(b25.fittedvalues, b7 = 'red')
    plt.title('MA Model: Residual Sum of Squares (RSS): %.4f' % sum((b25.fittedvalues - b30) ** 2))
    plt.show()
def fonk10(b11, b30):
    b23 = ARIMA(b11, order=(2, 1, 2))
    b26 = b23.fit()
    plt.plot(b30)
    plt.plot(b26.fittedvalues, b7 = 'red')
    plt.title('ARIMA Model: RSS (Root Squared Sum): %.4f' % sum((b26.fittedvalues - b30) ** 2))
    plt.show()
    return b26
def fonk11(b4, b32):
    b27 = np.exp(b32)
    b28 = []
    for i in range(len(b4)):
        print("Actual:", b4[i], "Predicted:", b27[len(b4) - i - 1])
        b28.append(100 - (abs(b4[i] - b27[len(b4) - i - 1]) / b4[i]) * 100)
    print("Average Accuracy:", sum(b28) / len(b4))
    plt.plot(b4)
    plt.plot(b27)
    plt.title('RMSE and Predictions')
    plt.show()
def fonk12():
    b29 = fonk1()
    b4 = fonk2(b29)
    fonk3(b4)
    b11 = fonk4(b4)
    b12 = fonk5(b11)
    b30 = b11 - b11.shift()
    b30.dropna(b14 = True)
    fonk3(b30)
    fonk6(b11)
    fonk7(b30)
    fonk8(b11, b30)
    fonk9(b11, b30)
    b26 = fonk10(b11, b30)
    b31 = pd.Series(b26.fittedvalues, copy=True)
    b32 = cumulative_sum(b11, b31)
    fonk11(b4, b32)
if b33 = = "__main__":
    fonk12()