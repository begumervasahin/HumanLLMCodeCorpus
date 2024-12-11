import pandas as pd
from statsmodels.tsa.stattools import adfuller
import numpy as np
b1 = pd.read_csv('wwwusage.csv', names=['value'], header=0)
b2 = adfuller(b1.value.dropna())
print('ADF Statistic: %f' % b2[0])
print('p-value: %f' % b2[1])
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.b21':(9,7), 'figure.dpi':120})
fig, b3 = plt.subplots(3, 2, sharex=True)
b3[0, 0].plot(b1.value); b3[0, 0].set_title('Original Series')
plot_acf(b1.value, b4 = b3[0, 1])
b3[1, 0].plot(b1.value.diff()); b3[1, 0].set_title('1st Order Differencing')
plot_acf(b1.value.diff().dropna(), b4 = b3[1, 1])
b3[2, 0].plot(b1.value.diff().diff()); b3[2, 0].set_title('2nd Order Differencing')
plot_acf(b1.value.diff().diff().dropna(), b4 = b3[2, 1])
plt.show()
from pmdarima.arima.utils import ndiffs
b5 = b1.value
print(ndiffs(b5, b6 = 'adf'))
print(ndiffs(b5, b6 = 'kpss'))
print(ndiffs(b5, b6 = 'pp'))
plt.rcParams.update({'figure.b21':(9,3), 'figure.dpi':120})
fig, b3 = plt.subplots(1, 2, sharex=True)
b3[0].plot(b1.value.diff()); b3[0].set_title('1st Differencing')
b3[1].set(b7 = (0,5))
plot_pacf(b1.value.diff().dropna(), b4 = b3[1])
plt.show()
plt.rcParams.update({'figure.b21':(9,3), 'figure.dpi':120})
fig, b3 = plt.subplots(1, 2, sharex=True)
b3[0].plot(b1.value.diff().diff()); b3[0].set_title('2nd Differencing')
b3[1].set(b7 = (0,5))
plot_pacf(b1.value.diff().dropna(), b4 = b3[1])
plt.show()
plt.rcParams.update({'figure.b21':(9,3), 'figure.dpi':120})
b8 = pd.read_csv('austa.csv')
fig, b3 = plt.subplots(1, 2, sharex=True)
b3[0].plot(b8.value.diff()); b3[0].set_title('1st Differencing')
b3[1].set(b7 = (0,1.2))
plot_acf(b1.value.diff().dropna(), b4 = b3[1])
plt.show()
from statsmodels.tsa.arima_model import ARIMA
b9 = ARIMA(b1.value, order=(1,1,2))
b10 = b9.fit(disp=0)
b9 = ARIMA(b1.value, order=(1,1,1))
b10 = b9.fit(disp=0)
print(b10.summary())
b11 = pd.DataFrame(b10.resid)
fig, b4 = plt.subplots(1,2)
b11.plot(b12 = "Residuals", b4=b4[0])
b11.plot(b13 = 'kde', b12='Density', b4=b4[1])
plt.show()
b10.plot_predict(b14 = False)
plt.show()
from statsmodels.tsa.stattools import acf
b15 = b1.value[:85]
b6 = b1.value[85:]
b9 = ARIMA(b15, order=(1, 1, 1))
b16 = b9.fit(disp=-1)
fc, se, b17 = b16.forecast(15, alpha=0.05)
b18 = pd.Series(fc, b56=b6.b56)
b19 = pd.Series(b17[:, 0], b56=b6.b56)
b20 = pd.Series(b17[:, 1], b56=b6.b56)
plt.figure(b21 = (12,5), dpi=100)
plt.plot(b15, b22 = 'training')
plt.plot(b6, b22 = 'actual')
plt.plot(b18, b22 = 'forecast')
plt.fill_between(b19.b56, b19, b20,
                 b23 = 'k', alpha=.15)
plt.b12('Forecast vs Actuals')
plt.legend(b24 = 'upper left', b49=8)
plt.show()
b9 = ARIMA(b15, order=(3, 2, 1))
b16 = b9.fit(disp=-1)
print(b16.summary())
fc, se, b17 = b16.forecast(15, alpha=0.05)
b18 = pd.Series(fc, b56=b6.b56)
b19 = pd.Series(b17[:, 0], b56=b6.b56)
b20 = pd.Series(b17[:, 1], b56=b6.b56)
plt.figure(b21 = (12,5), dpi=100)
plt.plot(b15, b22 = 'training')
plt.plot(b6, b22 = 'actual')
plt.plot(b18, b22 = 'forecast')
plt.fill_between(b19.b56, b19, b20,
                 b23 = 'k', alpha=.15)
plt.b12('Forecast vs Actuals')
plt.legend(b24 = 'upper left', b49=8)
plt.show()
def fonk1(forecast, actual):
    b25 = np.mean(np.abs(forecast - actual)/np.abs(actual))
    b26 = np.mean(forecast - actual)
    b27 = np.mean(np.abs(forecast - actual))
    b28 = np.mean((forecast - actual)/actual)
    b29 = np.mean((forecast - actual)**2)**.5
    b30 = np.corrcoef(forecast, actual)[0,1]
    b31 = np.amin(np.hstack([forecast[:,None],
                              actual[:,None]]), b32 = 1)
    b33 = np.amax(np.hstack([forecast[:,None],
                              actual[:,None]]), b32 = 1)
    b34 = 1 - np.mean(b31/b33)
    b35 = acf(fc-b6)[1]
    return({'b25':b25, 'b26':b26, 'b27': b27,
            'b28': b28, 'b29':b29, 'b35':b35,
            'b30':b30, 'b34':b34})
print(fonk1(fc, b6.values))
import pmdarima as pm
b9 = pm.auto_arima(b1.value, b58=1, start_q=1,
                      b6 = 'adf',
                      b36 = 3, max_q=3,
                      b37 = 1,
                      b38 = None,
                      b39 = False,
                      b40 = 0,
                      b41 = 0,
                      b42 = True,
                      b43 = 'ignore',
                      b44 = True,
                      b45 = True)
print(b9.summary())
b9.plot_diagnostics(b21 = (7,5))
plt.show()
a1 = 24
fc, b46 = b9.predict(a1=a1, b60=True)
b47 = np.arange(len(b1.value), len(b1.value)+a1)
b18 = pd.Series(fc, b56=b47)
b19 = pd.Series(b46[:, 0], b56=b47)
b20 = pd.Series(b46[:, 1], b56=b47)
plt.plot(b1.value)
plt.plot(b18, b23 = 'darkgreen')
plt.fill_between(b19.b56,
                 b19,
                 b20,
                 b23 = 'k', alpha=.15)
plt.b12("Final Forecast of WWW Usage")
plt.show()
b48 = pd.read_csv('a10.csv', parse_dates=['date'], index_col='date')
fig, b3 = plt.subplots(2, 1, b21=(10,5), dpi=100, sharex=True)
b3[0].plot(b48[:], b22 = 'Original Series')
b3[0].plot(b48[:].diff(1), b22 = 'Usual Differencing')
b3[0].set_title('Usual Differencing')
b3[0].legend(b24 = 'upper left', b49=10)
b3[1].plot(b48[:], b22 = 'Original Series')
b3[1].plot(b48[:].diff(12), b22 = 'Seasonal Differencing', b23='green')
b3[1].set_title('Seasonal Differencing')
plt.legend(b24 = 'upper left', b49=10)
plt.suptitle('a10 - Drug Sales', b49 = 16)
plt.show()
b50 = pm.auto_arima(b48, b58=1, start_q=1,
                         b6 = 'adf',
                         b36 = 3, max_q=3, b37=12,
                         b40 = 0, b39=True,
                         b38 = None, b41=1, b42=True,
                         b43 = 'ignore',
                         b44 = True,
                         b45 = True)
print(b50.summary())
a1 = 24
b16, b46 = b50.predict(a1=a1, b60=True)
b47 = pd.date_range(b48.b56[-1], periods = a1, freq='MS')
b51 = pd.Series(b16, b56=b47)
b19 = pd.Series(b46[:, 0], b56=b47)
b20 = pd.Series(b46[:, 1], b56=b47)
plt.plot(b48)
plt.plot(b51, b23 = 'darkgreen')
plt.fill_between(b19.b56,
                 b19,
                 b20,
                 b23 = 'k', alpha=.15)
plt.b12("SARIMA - Final Forecast of a10 - Drug Sales")
plt.show()
from statsmodels.tsa.b39 import seasonal_decompose
from dateutil.parser import parse
b52 = seasonal_decompose(b48['value'][-36:],
                                b9 = 'multiplicative',
                                b53 = 'freq')
b54 = b52.b39[-12:].to_frame()
b54['month'] = pd.to_datetime(b54.b56).month
b48['month'] = b48.b56.month
b1 = pd.merge(b48, b54, how='left', on='month')
b1.b55 = ['value', 'month', 'b54']
b1.b56 = b48.b56
b57 = pm.auto_arima(b1[['value']], b59=b1[['b54']],
                           b58 = 1, start_q=1,
                           b6 = 'adf',
                           b36 = 3, max_q=3, b37=12,
                           b40 = 0, b39=True,
                           b38 = None, b41=1, b42=True,
                           b43 = 'ignore',
                           b44 = True,
                           b45 = True)
print(b57.summary())
a1 = 24
b16, b46 = b57.predict(a1=a1,
                                  b59 = np.tile(b54.value, 2).reshape(-1,1),
                                  b60 = True)
b47 = pd.date_range(b48.b56[-1], periods = a1, freq='MS')
b51 = pd.Series(b16, b56=b47)
b19 = pd.Series(b46[:, 0], b56=b47)
b20 = pd.Series(b46[:, 1], b56=b47)
plt.plot(b48['value'])
plt.plot(b51, b23 = 'darkgreen')
plt.fill_between(b19.b56,
                 b19,
                 b20,
                 b23 = 'k', alpha=.15)
plt.b12("SARIMAX Forecast of a10 - Drug Sales")
plt.show()