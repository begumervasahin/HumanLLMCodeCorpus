
import os
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.b5.use('fivethirtyeight')
from pylab import rcParams
rcParams['figure.b3'] = 10, 6
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
import numpy as np
b1 = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
b2 = pd.read_csv('/Users/nageshsinghchauhan/Downloads/ML/time_series/stock-market/aaba.us.txt',sep=',', index_col='Date', parse_dates=['Date'], date_parser=b1).fillna(0)
plt.figure(b3 = (10,6))
plt.grid(True)
plt.xlabel('Dates')
plt.ylabel('Close Prices')
plt.plot(b2['Close'])
plt.title('Altaba Inc. closing price')
plt.show()
b4 = b2['Close']
b4.plot(b5 = 'k.')
plt.title('Scatter plot of closing price')
plt.show()
b4.plot(b6 = 'kde')
def fonk1(timeseries):
    b7 = timeseries.rolling(12).mean()
    b8 = timeseries.rolling(12).std()
    plt.plot(timeseries, b9 = 'blue',b20='Original')
    plt.plot(b7, b9 = 'red', b20='Rolling Mean')
    plt.plot(b8, b9 = 'black', b20 = 'Rolling Std')
    plt.legend(b10 = 'best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.show(b11 = False)
    print("Results of dickey fuller test")
    b12 = adfuller(timeseries,autolag='AIC')
    b13 = pd.Series(b12[0:4],index=['Test Statistics','p-value','No. of lags used','Number of observations used'])
    for key,values in b12[4].items():
        b13['critical value (%s)'%key] =  values
    print(b13)
fonk1(b4)
b14 = seasonal_decompose(b4, b21='multiplicative', freq = 30)
b15 = plt.figure()
b15 = b14.plot()
b15.set_size_inches(16, 9)
from pylab import rcParams
rcParams['figure.b3'] = 10, 6
b16 = np.log(b4)
b17 = b16.rolling(12).mean()
b18 = b16.rolling(12).std()
plt.legend(b10 = 'best')
plt.title('Moving Average')
plt.plot(b18, b9 = "black", b20 = "Standard Deviation")
plt.plot(b17, b9 = "red", b20 = "Mean")
plt.legend()
plt.show()
train_data, b19 = b16[3:int(len(b16)*0.9)], b16[int(len(b16)*0.9):]
plt.figure(b3 = (10,6))
plt.grid(True)
plt.xlabel('Dates')
plt.ylabel('Closing Prices')
plt.plot(b16, 'green', b20 = 'Train b2')
plt.plot(b19, 'blue', b20 = 'Test b2')
plt.legend()
b21 = ARIMA(train_data, order=(3, 1, 2))
b22 = b21.fit(disp=-1)
print(b22.summary())
fc, se, b23 = b22.forecast(544, alpha=0.05)
b24 = pd.Series(fc, index=b19.index)
b25 = pd.Series(b23[:, 0], index=b19.index)
b26 = pd.Series(b23[:, 1], index=b19.index)
plt.figure(b3 = (10,5), dpi=100)
plt.plot(train_data, b20 = 'training')
plt.plot(b19, b9 = 'blue', b20='Actual Stock Price')
plt.plot(b24, b9 = 'orange',b20='Predicted Stock Price')
plt.fill_between(b25.index, b25, b26,
                 b9 = 'k', alpha=.10)
plt.title('Altaba Inc. Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Altaba Inc. Stock Price')
plt.legend(b10 = 'upper left', fontsize=8)
plt.show()
b27 = mean_squared_error(b19, fc)
print('MSE: '+str(b27))
b28 = mean_absolute_error(b19, fc)
print('MAE: '+str(b28))
b29 = math.sqrt(mean_squared_error(b19, fc))
print('RMSE: '+str(b29))
b30 = np.mean(np.abs(fc - b19)/np.abs(b19))
print('MAPE: '+str(b30))
