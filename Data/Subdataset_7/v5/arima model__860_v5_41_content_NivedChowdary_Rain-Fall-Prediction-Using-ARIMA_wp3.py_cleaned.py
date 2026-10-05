import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.b19 import seasonal_decompose
b1 = pd.read_csv('annual.csv', parse_dates=['YEAR'])
b1['YEAR'] = pd.date_range(b2 = '1901', end='2017', freq='AS')
b1 = b1.set_index(['YEAR'])
def fonk1(data):
    plt.figure(b3 = (10, 6))
    plt.plot(data, b4 = 'Rainfall')
    plt.xlabel("Year")
    plt.ylabel("Rainfall")
    plt.b5('Annual Rainfall')
    plt.legend()
    plt.show()
fonk1(b1)
def fonk2(ts, b5 = 'Rolling Mean & Standard Deviation', window=12):
    b6 = ts.rolling(window=window).mean()
    b7 = ts.rolling(window=window).std()
    plt.figure(b3 = (10, 6))
    plt.plot(ts, b8 = 'blue', b4='Original')
    plt.plot(b6, b8 = 'red', b4='Rolling Mean')
    plt.plot(b7, b8 = 'black', b4='Rolling Std')
    plt.legend(b9 = 'best')
    plt.b5(b5)
    plt.show(b10 = False)
def fonk3(ts):
    print('Results of Dickey-Fuller Test:')
    b11 = adfuller(ts, autolag='AIC')
    b12 = pd.Series(b11[0:4], index=['Test Statistic', 'p-value', '
    for key, value in b11[4].items():
        b12[f'Critical Value ({key})'] = value
    print(b12)
fonk2(b1['ANNUAL'])
fonk3(b1['ANNUAL'])
b13 = np.log(b1)
b14 = b13.rolling(window=12).mean()
plt.figure(b3 = (10, 6))
plt.plot(b13, b8 = 'blue', b4='Log Transformed')
plt.plot(b14, b8 = 'red', b4='Moving Average')
plt.legend(b9 = 'best')
plt.show()
b15 = b13 - b14
b15.dropna(b16 = True)
fonk2(b15, b5 = 'Log Transformed Data minus Moving Average')
fonk3(b15['ANNUAL'])
b17 = seasonal_decompose(b13)
b18 = b17.b18
b19 = b17.b19
b20 = b17.resid
plt.figure(b3 = (11, 9))
plt.subplot(411)
plt.plot(b13, b4 = 'Original')
plt.legend(b9 = 'best')
plt.subplot(412)
plt.plot(b18, b4 = 'Trend')
plt.legend(b9 = 'best')
plt.subplot(413)
plt.plot(b19, b4 = 'Seasonality')
plt.legend(b9 = 'best')
plt.subplot(414)
plt.plot(b20, b4 = 'Residuals')
plt.legend(b9 = 'best')
plt.tight_layout()
def fonk4(ts, order):
    b21 = ARIMA(ts, order=order)
    b22 = b21.fit(disp=-1)
    plt.figure(b3 = (10, 6))
    plt.plot(ts, b4 = 'Original')
    plt.plot(b22.fittedvalues, b8 = 'red', b4='Fitted Values')
    plt.b5('RSS: %.4f' % sum((b22.fittedvalues - ts) ** 2))
    plt.legend(b9 = 'best')
    plt.show()
    return b22
b23 = fonk4(b13['ANNUAL'], (1, 1, 1))
a1 = 90
b24 = b23.b24(steps=a1)[0]
plt.figure(b3 = (10, 6))
plt.plot(np.exp(b24), b4 = 'Forecast')
plt.b5('Future Rainfall Prediction')
plt.legend(b9 = 'best')
plt.show()