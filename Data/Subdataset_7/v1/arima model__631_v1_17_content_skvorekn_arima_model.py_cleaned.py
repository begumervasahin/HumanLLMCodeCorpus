import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, acf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.b7 import ARIMA
import pmdarima as pm
b1 = pd.read_csv('wwwusage.csv', names=['value'], header=0)
b2 = adfuller(b1.value.dropna())
print('ADF Statistic: %f' % b2[0])
print('p-value: %f' % b2[1])
plt.rcParams.update({'figure.b17':(9,7), 'figure.dpi':120})
fig, b3 = plt.subplots(3, 2, sharex=True)
b3[0, 0].plot(b1.value)
b3[0, 0].set_title('Original Series')
plot_acf(b1.value, b4 = b3[0, 1])
for i, diff_order in enumerate([1, 2]):
    b5 = b1.value.diff(diff_order)
    b3[i+1, 0].plot(b5)
    b3[i+1, 0].set_title(f'{diff_order}st Order Differencing')
    plot_acf(b5.dropna(), b4 = b3[i+1, 1])
plt.show()
print("ADF Test for differencing:")
print(ndiffs(b1.value, b6 = 'adf'))
print("KPSS Test for differencing:")
print(ndiffs(b1.value, b6 = 'kpss'))
print("PP Test for differencing:")
print(ndiffs(b1.value, b6 = 'pp'))
plt.rcParams.update({'figure.b17':(9,3), 'figure.dpi':120})
fig, b3 = plt.subplots(1, 2, sharex=True)
b5 = b1.value.diff()
b3[0].plot(b5)
b3[0].set_title('1st Differencing')
plot_pacf(b5.dropna(), b4 = b3[1])
plt.show()
plt.rcParams.update({'figure.b17':(9,3), 'figure.dpi':120})
fig, b3 = plt.subplots(1, 2, sharex=True)
b5 = b1.value.diff().diff()
b3[0].plot(b5)
b3[0].set_title('2nd Differencing')
plot_pacf(b5.dropna(), b4 = b3[1])
plt.show()
b7 = ARIMA(b1.value, order=(1,1,2))
b8 = b7.fit(disp=0)
print(b8.summary())
b9 = pd.DataFrame(b8.resid)
fig, b4 = plt.subplots(1,2)
b9.plot(b10 = "Residuals", b4=b4[0])
b9.plot(b11 = 'kde', b10='Density', b4=b4[1])
plt.show()
b7 = ARIMA(b1.value[:85], order=(1, 1, 1))
b12 = b7.fit(disp=-1)
fc, se, b13 = b12.forecast(15, alpha=0.05)
b14 = pd.Series(fc, b50=b1.value[85:].b50)
b15 = pd.Series(b13[:, 0], b50=b1.value[85:].b50)
b16 = pd.Series(b13[:, 1], b50=b1.value[85:].b50)
plt.figure(b17 = (12,5), dpi=100)
plt.plot(b1.value[:85], b18 = 'training')
plt.plot(b1.value[85:], b18 = 'actual')
plt.plot(b14, b18 = 'forecast')
plt.fill_between(b15.b50, b15, b16,
                 b19 = 'k', alpha=.15)
plt.b10('Forecast vs Actuals')
plt.legend(b20 = 'upper left', fontsize=8)
plt.show()
def fonk1(forecast, actual):
    b21 = np.mean(np.abs(forecast - actual)/np.abs(actual))
    b22 = np.mean(forecast - actual)
    b23 = np.mean(np.abs(forecast - actual))
    b24 = np.mean((forecast - actual)/actual)
    b25 = np.mean((forecast - actual)**2)**.5
    b26 = np.corrcoef(forecast, actual)[0,1]
    b27 = np.amin(np.hstack([forecast[:,None],
                              actual[:,None]]), b28 = 1)
    b29 = np.amax(np.hstack([forecast[:,None],
                              actual[:,None]]), b28 = 1)
    b30 = 1 - np.mean(b27/b29)
    b31 = acf(fc-b6)[1]
    return({'b21':b21, 'b22':b22, 'b23': b23,
            'b24': b24, 'b25':b25, 'b31':b31,
            'b26':b26, 'b30':b30})
print(fonk1(fc, b1.value[85:].values))
b32 = pm.auto_arima(b1.value, b52=1, start_q=1,
                      b6 = 'adf',
                      b33 = 3, max_q=3,
                      b34 = 1,
                      b35 = None,
                      b36 = False,
                      b37 = 0,
                      b38 = 0,
                      b39 = True,
                      b40 = 'ignore',
                      b41 = True,
                      b42 = True)
print(b32.summary())
b32.plot_diagnostics(b17 = (7,5))
plt.show()
a1 = 24
fc, b43 = b32.predict(a1=a1, b54=True)
b44 = np.arange(len(b1.value), len(b1.value)+a1)
b14 = pd.Series(fc, b50=b44)
b15 = pd.Series(b43[:, 0], b50=b44)
b16 = pd.Series(b43[:, 1], b50=b44)
plt.plot(b1.value)
plt.plot(b14, b19 = 'darkgreen')
plt.fill_between(b15.b50,
                 b15,
                 b16,
                 b19 = 'k', alpha=.15)
plt.b10("Final Forecast of WWW Usage")
plt.show()
b45 = pd.read_csv('a10.csv', parse_dates=['date'], index_col='date')
b46 = seasonal_decompose(b45['value'][-36:],
                                b7 = 'multiplicative',
                                b47 = 'freq')
b48 = b46.b36[-12:].to_frame()
b48['month'] = pd.to_datetime(b48.b50).month
b45['month'] = b45.b50.month
b1 = pd.merge(b45, b48, how='left', on='month')
b1.b49 = ['value', 'month', 'b48']
b1.b50 = b45.b50
b51 = pm.auto_arima(b1[['value']], b53=b1[['b48']],
                           b52 = 1, start_q=1,
                           b6 = 'adf',
                           b33 = 3, max_q=3, b34=12,
                           b37 = 0, b36=True,
                           b35 = None, b38=1, b39=True,
                           b40 = 'ignore',
                           b41 = True,
                           b42 = True)
print(b51.summary())
a1 = 24
b12, b43 = b51.predict(a1=a1,
                                  b53 = np.tile(b48.value, 2).reshape(-1,1),
                                  b54 = True)
b44 = pd.date_range(b45.b50[-1], periods = a1, freq='MS')
b55 = pd.Series(b12, b50=b44)
b15 = pd.Series(b43[:, 0], b50=b44)
b16 = pd.Series(b43[:, 1], b50=b44)
plt.plot(b45['value'])
plt.plot(b55, b19 = 'darkgreen')
plt.fill_between(b15.b50,
                 b15,
                 b16,
                 b19 = 'k', alpha=.15)
plt.b10("SARIMAX Forecast of a10 - Drug Sales")
plt.show()