import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.b14 import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
def fonk1(file_path):
    b1 = pd.read_csv(file_path, parse_dates=['YEAR'])
    b1['YEAR'] = pd.date_range(b2 = '1901', end='2017', freq='AS')
    b3 = b1.set_index(['YEAR'])
    return b3
def fonk2(data):
    b4 = data.rolling(window=1).mean()
    b5 = data.rolling(window=1).std()
    plt.plot(data, b6 = 'blue', b16='Original')
    plt.plot(b4, b6 = 'red', b16='Rolling Mean')
    plt.plot(b5, b6 = 'black', b16='Rolling Std')
    plt.legend(b7 = 'best')
    plt.title('Rolling mean vs Standard deviation')
    plt.show(b8 = False)
def fonk3(data):
    print('Results of Dickey-Fuller Test:')
    b9 = adfuller(data['ANNUAL'], autolag='AIC')
    b10 = pd.Series(b9[0:4], index=['Test Statistics', 'p-value'])
    for key, value in b9[4].items():
        b10['Critical value (%s)' % key] = value
    print(b10)
def fonk4(data):
    plt.xlabel("Date")
    plt.ylabel("Rainfall")
    plt.plot(data)
    b11 = np.log(data)
    plt.plot(b11)
    return b11
def fonk5(data):
    b12 = seasonal_decompose(data)
    b13 = b12.b13
    b14 = b12.b14
    b15 = b12.resid
    plt.subplot(411)
    plt.plot(data, b16 = 'Original')
    plt.legend(b7 = 'best')
    plt.subplot(412)
    plt.plot(b13, b16 = 'Trend')
    plt.legend(b7 = 'best')
    plt.subplot(413)
    plt.plot(b14, b16 = 'Seasonality')
    plt.legend(b7 = 'best')
    plt.subplot(414)
    plt.plot(b15, b16 = 'Residual')
    plt.legend(b7 = 'best')
    plt.tight_layout()
    return b15.dropna()
def fonk6(data):
    b17 = acf(data, nlags=20)
    b18 = pacf(data, nlags=20, method='ols')
    plt.subplot(121)
    plt.plot(b17)
    plt.axhline(b19 = 0, linestyle='--', b6='gray')
    plt.axhline(b19 = -1.96 / np.sqrt(len(data)), linestyle='--', b6='gray')
    plt.axhline(b19 = 1.96 / np.sqrt(len(data)), linestyle='--', b6='gray')
    plt.title('Autocorrelation Function')
    plt.subplot(122)
    plt.plot(b18)
    plt.axhline(b19 = 0, linestyle='--', b6='gray')
    plt.axhline(b19 = -1.96 / np.sqrt(len(data)), linestyle='--', b6='gray')
    plt.axhline(b19 = 1.96 / np.sqrt(len(data)), linestyle='--', b6='gray')
    plt.title('Partial Autocorrelation Function')
    plt.tight_layout()
def fonk7(data):
    b20 = ARIMA(data, order=(1, 1, 1))
    b21 = b20.fit(disp=-1)
    plt.plot(data)
    plt.plot(b21.fittedvalues, b6 = 'red')
    plt.title('RSS: %.4f' % sum((b21.fittedvalues - data['ANNUAL']) ** 2))
    return b21.b24(b22 = 90)
def fonk8():
    b3 = fonk1('annual.csv')
    fonk2(b3)
    fonk3(b3)
    b11 = fonk4(b3)
    b23 = fonk5(b11)
    fonk6(b23)
    b24 = fonk7(b23)
    print("Forecast:", b24)
if b25 = = "__main__":
    fonk8()