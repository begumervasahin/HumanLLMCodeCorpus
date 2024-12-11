
import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
plt.b13.use('fivethirtyeight')
plt.figure(b1 = (10, 6))
plt.grid(True)
def fonk1(timeseries):
    b2 = timeseries.rolling(12).mean()
    b3 = timeseries.rolling(12).std()
    plt.plot(timeseries, b4 = 'blue', b21='Original')
    plt.plot(b2, b4 = 'red', b21='Rolling Mean')
    plt.plot(b3, b4 = 'black', b21='Rolling Std')
    plt.legend(b5 = 'best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.show(b6 = False)
    print("Results of Dickey-Fuller Test:")
    b7 = adfuller(timeseries, autolag='AIC')
    b8 = pd.Series(b7[0:4], index=['Test Statistics', 'p-value', 'No. of lags used', 'Number of observations used'])
    for key, values in b7[4].items():
        b8[f'critical value ({key})'] = values
    print(b8)
b9 = lambda dates: pd.to_datetime(dates, format='%Y-%m-%d')
b10 = '/Users/nageshsinghchauhan/Downloads/ML/time_series/stock-market/aaba.us.txt'
b11 = pd.read_csv(b10, sep=',', index_col='Date', parse_dates=['Date'], date_parser=b9).fillna(0)
plt.xlabel('Dates')
plt.ylabel('Close Prices')
plt.plot(b11['Close'])
plt.title('Altaba Inc. Closing Price')
plt.show()
b12 = b11['Close']
b12.plot(b13 = 'k.')
plt.title('Scatter plot of Closing Price')
plt.show()
b12.plot(b14 = 'kde')
fonk1(b12)
b15 = seasonal_decompose(b12, b22='multiplicative', freq=30)
b16 = b15.plot()
b16.set_size_inches(16, 9)
plt.figure(b1 = (10, 6))
b17 = np.log(b12)
b18 = b17.rolling(12).mean()
b19 = b17.rolling(12).std()
plt.legend(b5 = 'best')
plt.title('Moving Average')
plt.plot(b19, b4 = "black", b21="Standard Deviation")
plt.plot(b18, b4 = "red", b21="Mean")
plt.legend()
plt.show()
train_data, b20 = b17[3:int(len(b17) * 0.9)], b17[int(len(b17) * 0.9):]
plt.figure(b1 = (10, 6))
plt.grid(True)
plt.xlabel('Dates')
plt.ylabel('Closing Prices')
plt.plot(b17, 'green', b21 = 'Train b11')
plt.plot(b20, 'blue', b21 = 'Test b11')
plt.legend()
b22 = ARIMA(train_data, order=(3, 1, 2))
b23 = b22.fit(disp=-1)
print(b23.summary())
fc, se, b24 = b23.forecast(544, alpha=0.05)
b25 = pd.Series(fc, index=b20.index)
b26 = pd.Series(b24[:, 0], index=b20.index)
b27 = pd.Series(b24[:, 1], index=b20.index)
plt.figure(b1 = (10, 5), dpi=100)
plt.plot(train_data, b21 = 'Training')
plt.plot(b20, b4 = 'blue', b21='Actual Stock Price')
plt.plot(b25, b4 = 'orange', b21='Predicted Stock Price')
plt.fill_between(b26.index, b26, b27, b4 = 'k', alpha=.10)
plt.title('Altaba Inc. Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Altaba Inc. Stock Price')
plt.legend(b5 = 'upper left', fontsize=8)
plt.show()
b28 = mean_squared_error(b20, fc)
b29 = mean_absolute_error(b20, fc)
b30 = math.sqrt(b28)
b31 = np.mean(np.abs(fc - b20) / np.abs(b20))
print(f'MSE: {b28:.4f}')
print(f'MAE: {b29:.4f}')
print(f'RMSE: {b30:.4f}')
print(f'MAPE: {b31:.4f}')