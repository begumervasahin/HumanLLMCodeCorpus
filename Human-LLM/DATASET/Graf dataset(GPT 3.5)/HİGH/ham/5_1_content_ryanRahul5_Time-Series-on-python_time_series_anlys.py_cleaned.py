
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
b1 = pd.read_csv('C:\Users\Dell\Desktop\Pairs Trading\FuturePrices.csv')
print b1.ix[:10]
print b1.head()
print b1.dtypes
b2 = b1.ix[:,['Date','YESBANK']]
print b2.head()
b3 = b1['YESBANK']
b3.head(10)
plt.plot(b3)
b1 = pd.read_csv('C:\Users\Dell\Desktop\Pairs Trading\FuturePrices.csv', parse_dates = 'Date', index_col = 'Date')
b3 = b1['YESBANK']
b3.head(5)
b3['2010-01-07']
b3['2011-08-21': '2011-08-25']
plt.plot(b3)
from statsmodels.tsa.stattools import adfuller
def fonk1(timeseries):
    b4 = pd.rolling_mean(timeseries, window = 8)
    b5 = pd.rolling_std(timeseries, window = 8)
    b6 = plt.plot(timeseries, b15 = 'red', b25 = 'original series')
    b7 = plt.plot(b4, b15='black', b25 = 'rolling b7')
    b8 = plt.plot(b5, b15 = 'blue', b25 = 'rolling b8')
    plt.legend(b9 = 'best')
    plt.title('R_mean vs R_std')
    plt.show(b10 = False)
    print 'Dickey-Fuller test:'
    b11 = adfuller(timeseries, autolag = 'AIC')
    b12 = pd.Series(b11[0:4], index = ['t-stat','p-val', '
    for key,value in b11[4].items():
        b12['Critical Value (%s)'%key] = value
    print b12
fonk1(b3)
b13 = np.log(b3)
plt.plot(b13)
b14 = pd.rolling_mean(b13,8)
plt.plot(b13)
plt.plot(b14, b15 = 'red')
b16 = b13 - b14
b16.head(8)
b16.dropna(b17 = True)
fonk1(b16)
b18 = pd.ewma(b13, halflife=8)
plt.plot(b13)
plt.plot(b18, b15 = 'red')
b19 = b13 - b18
fonk1(b19)
b20 = b13 - b13.shift()
plt.plot(b20)
b20.dropna(b17 = True)
fonk1(b20)
from statsmodels.tsa.b23 import seasonal_decompose
b21 = seasonal_decompose(b13, freq = 100)
b22 = b21.b22
b23 = b21.b23
b24 = b21.resid
plt.subplot(411)
plt.plot(b13, b25 = 'Original')
plt.legend(b9 = 'best')
plt.subplot(412)
plt.plot(b22, b25 = 'Trend')
plt.legend(b9 = 'best')
plt.subplot(413)
plt.plot(b23,b25 = 'Seasonality')
plt.legend(b9 = 'best')
plt.subplot(414)
plt.plot(b24, b25 = 'Residuals')
plt.legend(b9 = 'best')
plt.tight_layout()
b26 = b24
b26.dropna(b17 = True)
fonk1(b26)
from statsmodels.tsa.stattools import acf, pacf
b27 = acf(b20, nlags=20)
b28 = pacf(b20, nlags=20, method='ols')
plt.subplot(121)
plt.plot(b27)
plt.axhline(b29 = 0,linestyle='--',b15='gray')
plt.axhline(b29 = -1.96/np.sqrt(len(b20)),linestyle='--',b15='gray')
plt.axhline(b29 = 1.96/np.sqrt(len(b20)),linestyle='--',b15='gray')
plt.title('Autocorrelation Function')
plt.subplot(122)
plt.plot(b28)
plt.axhline(b29 = 0,linestyle='--',b15='gray')
plt.axhline(b29 = -1.96/np.sqrt(len(b20)),linestyle='--',b15='gray')
plt.axhline(b29 = 1.96/np.sqrt(len(b20)),linestyle='--',b15='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()
from statsmodels.tsa.arima_model import ARIMA
b30 = ARIMA(b13, order=(2, 1, 0))
b31 = b30.fit(disp=-1)
plt.plot(b20)
plt.plot(b31.fittedvalues, b15 = 'red')
plt.title('RSS: %.4f'% sum((b31.fittedvalues-b20)**2))
b30 = ARIMA(b13, order=(0, 1, 2))
b32 = b30.fit(disp=-1)
plt.plot(b20)
plt.plot(b32.fittedvalues, b15 = 'red')
plt.title('RSS: %.4f'% sum((b32.fittedvalues-b20)**2))
b30 = ARIMA(b13, order=(2, 1, 2))
b33 = b30.fit(disp=-1)
plt.plot(b20)
plt.plot(b33.fittedvalues, b15 = 'red')
plt.title('RSS: %.4f'% sum((b33.fittedvalues-b20)**2))
b34 = pd.Series(b33.fittedvalues, copy=True)
print b34.head()
b35 = b34.cumsum()
print b35.head()
b36 = pd.Series(b13.ix[0], index=b13.index)
b36 = b36.add(b35,fill_value=0)
b36.head()
b37 = np.exp(b36)
plt.plot(b3)
plt.plot(b37)
plt.title('RMSE: %.4f'% np.sqrt(sum((b37-b3)**2)/len(b3)))