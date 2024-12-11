import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
plt.b13.use('fivethirtyeight')
rcParams['figure.b11'] = 10, 6
def fonk1(timeseries):
    b1 = timeseries.rolling(12).mean()
    b2 = timeseries.rolling(12).std()
    plt.plot(timeseries, b3 = 'blue', b21='Original')
    plt.plot(b1, b3 = 'red', b21='Rolling Mean')
    plt.plot(b2, b3 = 'black', b21='Rolling Std')
    plt.legend(b4 = 'best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.show(b5 = False)
    print("Results of Dickey-Fuller Test:")
    b6 = adfuller(timeseries, autolag='AIC')
    b7 = pd.Series(b6[0:4], index=['Test Statistics', 'p-value', 'No. of lags used', 'Number of observations used'])
    for key, values in b6[4].items():
        b7['critical value (%s)' % key] = values
    print(b7)
b8 = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
b9 = pd.read_csv('/Users/nageshsinghchauhan/Downloads/ML/time_series/stock-market/aaba.us.txt',
                   b10 = ',', index_col='Date', parse_dates=['Date'], date_parser=b8).fillna(0)
plt.figure(b11 = (10, 6))
plt.grid(True)
plt.xlabel('Dates')
plt.ylabel('Close Prices')
plt.plot(b9['Close'])
plt.title('Altaba Inc. closing price')
plt.show()
b12 = b9['Close']
b12.plot(b13 = 'k.')
plt.title('Scatter plot of closing price')
plt.show()
b12.plot(b14 = 'kde')
fonk1(b12)
b15 = seasonal_decompose(b12, b22='multiplicative', freq=30)
b16 = plt.figure()
b16 = b15.plot()
b16.set_size_inches(16, 9)
rcParams['figure.b11'] = 10, 6
b17 = np.log(b12)
b18 = b17.rolling(12).mean()
b19 = b17.rolling(12).std()
plt.legend(b4 = 'best')
plt.title('Moving Average')
plt.plot(b19, b3 = "black", b21="Standard Deviation")
plt.plot(b18, b3 = "red", b21="Mean")
plt.legend()
plt.show()
train_data, b20 = b17[3:int(len(b17) * 0.9)], b17[int(len(b17) * 0.9):]
plt.figure(b11 = (10, 6))
plt.grid(True)
plt.xlabel('Dates')
plt.ylabel('Closing Prices')
plt.plot(b17, 'green', b21 = 'Train b9')
plt.plot(b20, 'blue', b21 = 'Test b9')
plt.legend()
b22 = ARIMA(train_data, order=(3, 1, 2))
b23 = b22.fit(disp=-1)
print(b23.summary())
fc, se, b24 = b23.forecast(544, alpha=0.05)
b25 = pd.Series(fc, index=b20.index)
b26 = pd.Series(b24[:, 0], index=b20.index)
b27 = pd.Series(b24[:, 1], index=b20.index)
plt.figure(b11 = (10, 5), dpi=100)
plt.plot(train_data, b21 = 'training')
plt.plot(b20, b3 = 'blue', b21='Actual Stock Price')
plt.plot(b25, b3 = 'orange', b21='Predicted Stock Price')
plt.fill_between(b26.index, b26, b27, b3 = 'k', alpha=.10)
plt.title('Altaba Inc. Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Altaba Inc. Stock Price')
plt.legend(b4 = 'upper left', fontsize=8)
plt.show()
b28 = mean_squared_error(b20, fc)
print('MSE: ' + str(b28))
b29 = mean_absolute_error(b20, fc)
print('MAE: ' + str(b29))
b30 = math.sqrt(mean_squared_error(b20, fc))
print('RMSE: ' + str(b30))
b31 = np.mean(np.abs(fc - b20) / np.abs(b20))
print('MAPE: ' + str(b31))