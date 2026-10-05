
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
plt.b6.use('fivethirtyeight')
rcParams['figure.b4'] = 10, 6
warnings.filterwarnings('ignore')
b1 = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
b2 = pd.read_csv('/Users/nageshsinghchauhan/Downloads/ML/time_series/stock-market/aaba.us.txt',
                   b3 = ',', index_col='Date', parse_dates=['Date'], b1=b1).fillna(0)
plt.figure(b4 = (10, 6))
plt.grid(True)
plt.xlabel('Dates')
plt.ylabel('Close Prices')
plt.plot(b2['Close'])
plt.title('Altaba Inc. closing price')
plt.show()
b5 = b2['Close']
b5.plot(b6 = 'k.')
plt.title('Scatter plot of closing price')
plt.show()
b5.plot(b7 = 'kde')
def fonk1(timeseries):
    b8 = timeseries.rolling(12).mean()
    b9 = timeseries.rolling(12).std()
    plt.plot(timeseries, b10 = 'blue', b21='Original')
    plt.plot(b8, b10 = 'red', b21='Rolling Mean')
    plt.plot(b9, b10 = 'black', b21='Rolling Std')
    plt.legend(b11 = 'best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.show(b12 = False)
    print("Results of Dickey-Fuller test")
    b13 = adfuller(timeseries, autolag='AIC')
    b14 = pd.Series(b13[0:4], index=['Test Statistics', 'p-value', 'No. of lags used', 'Number of observations used'])
    for key, values in b13[4].items():
        b14['critical value (%s)' % key] = values
    print(b14)
fonk1(b5)
b15 = seasonal_decompose(b5, b22='multiplicative', freq=30)
b16 = b15.plot()
b16.set_size_inches(16, 9)
from pylab import rcParams
rcParams['figure.b4'] = 10, 6
b17 = np.log(b5)
b18 = b17.rolling(12).mean()
b19 = b17.rolling(12).std()
plt.legend(b11 = 'best')
plt.title('Moving Average')
plt.plot(b19, b10 = "black", b21="Standard Deviation")
plt.plot(b18, b10 = "red", b21="Mean")
plt.legend()
plt.show()
train_data, b20 = b17[3:int(len(b17) * 0.9)], b17[int(len(b17) * 0.9):]
plt.figure(b4 = (10, 6))
plt.grid(True)
plt.xlabel('Dates')
plt.ylabel('Closing Prices')
plt.plot(b17, 'green', b21 = 'Train b2')
plt.plot(b20, 'blue', b21 = 'Test b2')
plt.legend()
b22 = ARIMA(train_data, order=(3, 1, 2))
b23 = b22.fit(disp=-1)
print(b23.summary())
fc, se, b24 = b23.forecast(544, alpha=0.05)
b25 = pd.Series(fc, index=b20.index)
b26 = pd.Series(b24[:, 0], index=b20.index)
b27 = pd.Series(b24[:, 1], index=b20.index)
plt.figure(b4 = (10, 5), dpi=100)
plt.plot(train_data, b21 = 'training')
plt.plot(b20, b10 = 'blue', b21='Actual Stock Price')
plt.plot(b25, b10 = 'orange', b21='Predicted Stock Price')
plt.fill_between(b26.index, b26, b27, b10 = 'k', alpha=.10)
plt.title('Altaba Inc. Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Altaba Inc. Stock Price')
plt.legend(b11 = 'upper left', fontsize=8)
plt.show()
b28 = mean_squared_error(b20, fc)
print('MSE: ' + str(b28))
b29 = mean_absolute_error(b20, fc)
print('MAE: ' + str(b29))
b30 = math.sqrt(mean_squared_error(b20, fc))
print('RMSE: ' + str(b30))
b31 = np.mean(np.abs(fc - b20) / np.abs(b20))
print('MAPE: ' + str(b31))
