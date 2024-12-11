import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.b15 import seasonal_decompose
from statsmodels.tsa.arima.b21 import ARIMA
def fonk1():
    print('Welcome! Please choose a company from the following options:')
    print('1: Google')
    print('2: Facebook')
    print('3: Quit')
    b1 = int(input('Enter your b1: '))
    b2 = None
    if b1 = = 1:
        b2 = pd.read_csv('WIKI-GOOGL.csv', parse_dates=['Date'], index_col='Date')
    elif b1 = = 2:
        b2 = pd.read_csv('facebook.csv', parse_dates=['Date'], index_col='Date')
    else:
        print('Invalid b1. Exiting.')
        exit()
    print(b2.head())
    print('\nFeatures and their Data Types:')
    print(b2.dtypes)
    return b2
def fonk2(b28):
    plt.plot(b28)
    plt.title('Adjusted Close Prices Over Time')
    plt.show()
def fonk3(b28):
    b3 = b28.rolling(window=20).mean()
    b4 = b28.rolling(window=20).std()
    plt.plot(b28, b5 = 'blue', b17='Original')
    plt.plot(b3, b5 = 'red', b17='Rolling Mean')
    plt.plot(b4, b5 = 'black', b17='Rolling Std')
    plt.legend(b6 = 'best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    print('Results of Dickey-Fuller Test:')
    b7 = adfuller(b28, autolag='AIC')
    b8 = pd.Series(b7[0:4], index=['Test Statistic', 'p-value', '
    for key, value in b7[4].items():
        b8['Critical Value (%s)' % key] = value
    print(b8)
def fonk4(b28):
    b9 = np.log(b28)
    plt.plot(b9)
    plt.title('Log Transformed Series')
    plt.show()
    return b9
def fonk5(b9):
    b10 = b9.rolling(10, min_periods=1).mean()
    plt.plot(b9, b5 = 'blue', b17='Original')
    plt.plot(b10, b5 = 'red', b17='Moving Average')
    plt.legend()
    plt.title('Smoothed Data')
    plt.show()
    b11 = b9 - b10
    b11.dropna(b12 = True)
    fonk3(b11)
    return b10
def fonk6(b9):
    b13 = seasonal_decompose(b9, freq=52)
    b14 = b13.b14
    b15 = b13.b15
    b16 = b13.resid
    plt.plot(b9, b17 = 'Original')
    plt.legend(b6 = 'best')
    plt.title('Original Series')
    plt.show()
    plt.plot(b14, b17 = 'Trend')
    plt.legend(b6 = 'best')
    plt.title('Trend Component')
    plt.show()
    plt.plot(b15, b17 = 'Seasonality')
    plt.legend(b6 = 'best')
    plt.title('Seasonal Component')
    plt.show()
    plt.plot(b16, b17 = 'Residuals')
    plt.legend(b6 = 'best')
    plt.title('Residuals')
    plt.show()
def fonk7(b29):
    b18 = acf(b29, nlags=20)
    b19 = pacf(b29, nlags=20, method='ols')
    plt.plot(b18)
    plt.axhline(b20 = 0, linestyle='--', b5='gray')
    plt.title('Autocorrelation Function (ACF)')
    plt.show()
    plt.plot(b19)
    plt.axhline(b20 = 0, linestyle='--', b5='gray')
    plt.title('Partial Autocorrelation Function (PACF)')
    plt.show()
def fonk8(b9, b29):
    b21 = ARIMA(b9, order=(2, 1, 0))
    b22 = b21.fit()
    plt.plot(b29)
    plt.plot(b22.fittedvalues, b5 = 'red')
    plt.title('AR Model: Residual Sum of Squares (RSS): %.4f' % sum((b22.fittedvalues - b29) ** 2))
    plt.show()
def fonk9(b9, b29):
    b21 = ARIMA(b9, order=(0, 1, 2))
    b23 = b21.fit()
    plt.plot(b29)
    plt.plot(b23.fittedvalues, b5 = 'red')
    plt.title('MA Model: Residual Sum of Squares (RSS): %.4f' % sum((b23.fittedvalues - b29) ** 2))
    plt.show()
def fonk10(b9, b29):
    b21 = ARIMA(b9, order=(2, 1, 2))
    b24 = b21.fit()
    plt.plot(b29)
    plt.plot(b24.fittedvalues, b5 = 'red')
    plt.title('ARIMA Model: RSS (Root Squared Sum): %.4f' % sum((b24.fittedvalues - b29) ** 2))
    plt.show()
    return b24
def fonk11(b28, predictions_ARIMA_log):
    b25 = np.exp(predictions_ARIMA_log)
    b26 = []
    for i in range(len(b28)):
        print("Actual:", b28[i], "Predicted:", b25[len(b28) - i - 1])
        b26.append(100 - (abs(b28[i] - b25[len(b28) - i - 1]) / b28[i]) * 100)
    print("Average Accuracy:", sum(b26) / len(b28))
    plt.plot(b28, b17 = 'Original')
    plt.plot(b25, b17 = 'Predicted', b5='red')
    plt.legend()
    plt.title('RMSE and Predictions')
    plt.show()
def fonk12():
    b27 = fonk1()
    b28 = convert_to_timeseries(b27)
    fonk2(b28)
    fonk3(b28)
    b9 = fonk4(b28)
    b10 = fonk5(b9)
    b29 = b9 - b9.shift()
    b29.dropna(b12 = True)
    fonk3(b29)
    fonk6(b9)
    fonk7(b29)
    fonk8(b9, b29)
    fonk9(b9, b29