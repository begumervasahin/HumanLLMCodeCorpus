import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.b18 import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
def fonk1(timeseries):
    b1 = timeseries.rolling(window=8).mean()
    b2 = timeseries.rolling(window=8).std()
    plt.plot(timeseries, b3 = 'red', b20='Original series')
    plt.plot(b1, b3 = 'black', b20='Rolling mean')
    plt.plot(b2, b3 = 'blue', b20='Rolling std')
    plt.legend(b4 = 'best')
    plt.title('Rolling mean vs Rolling std')
    plt.show()
    b5 = adfuller(timeseries, autolag='AIC')
    b6 = pd.Series(b5[0:4], index=['Test Statistic', 'p-value', 'Lags Used', 'Observations Used'])
    for key, value in b5[4].items():
        b6['Critical Value (%s)' % key] = value
    print(b6)
def fonk2():
    b7 = pd.read_csv('C:\Users\Dell\Desktop\Pairs Trading\FuturePrices.csv', parse_dates=['Date'], index_col='Date')
    b8 = b7['YESBANK']
    plt.plot(b8)
    plt.title('Original Time Series')
    plt.show()
    fonk1(b8)
    b9 = np.log(b8)
    b10 = b9.rolling(window=8).mean()
    b11 = b9 - b10
    b11.dropna(b12 = True)
    fonk1(b11)
    b13 = b9.ewm(halflife=8).mean()
    b14 = b9 - b13
    fonk1(b14)
    b15 = b9 - b9.shift()
    b15.dropna(b12 = True)
    fonk1(b15)
    b16 = seasonal_decompose(b9, freq=100)
    b17 = b16.b17
    b18 = b16.b18
    b19 = b16.resid
    plt.subplot(411)
    plt.plot(b9, b20 = 'Original')
    plt.legend(b4 = 'best')
    plt.subplot(412)
    plt.plot(b17, b20 = 'Trend')
    plt.legend(b4 = 'best')
    plt.subplot(413)
    plt.plot(b18, b20 = 'Seasonality')
    plt.legend(b4 = 'best')
    plt.subplot(414)
    plt.plot(b19, b20 = 'Residuals')
    plt.legend(b4 = 'best')
    plt.tight_layout()
    plt.show()
    b21 = acf(b15, nlags=20)
    b22 = pacf(b15, nlags=20, method='ols')
    plt.subplot(121)
    plt.plot(b21)
    plt.axhline(b23 = 0, linestyle='--', b3='gray')
    plt.axhline(b23 = -1.96/np.sqrt(len(b15)), linestyle='--', b3='gray')
    plt.axhline(b23 = 1.96/np.sqrt(len(b15)), linestyle='--', b3='gray')
    plt.title('Autocorrelation Function')
    plt.subplot(122)
    plt.plot(b22)
    plt.axhline(b23 = 0, linestyle='--', b3='gray')
    plt.axhline(b23 = -1.96/np.sqrt(len(b15)), linestyle='--', b3='gray')
    plt.axhline(b23 = 1.96/np.sqrt(len(b15)), linestyle='--', b3='gray')
    plt.title('Partial Autocorrelation Function')
    plt.tight_layout()
    plt.show()
    b24 = ARIMA(b9, order=(2, 1, 0))
    b25 = b24.fit(disp=-1)
    plt.plot(b15)
    plt.plot(b25.fittedvalues, b3 = 'red')
    plt.title('ARIMA Model - RSS: %.4f' % sum((b25.fittedvalues - b15)**2))
    plt.show()
    b26 = pd.Series(b25.fittedvalues, copy=True)
    b27 = b26.cumsum()
    b28 = pd.Series(b9.iloc[0], index=b9.index)
    b28 = b28.add(b27, fill_value=0)
    b29 = np.exp(b28)
    plt.plot(b8)
    plt.plot(b29)
    plt.title('ARIMA Predictions - RMSE: %.4f' % np.sqrt(sum((b29 - b8)**2) / len(b8)))
    plt.show()
if b30 = = "__main__":
    fonk2()