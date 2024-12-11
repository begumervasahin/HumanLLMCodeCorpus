import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.b25 import ARIMA
import pmdarima as pm
def fonk1(data):
    fig, b1 = plt.subplots(3, 2, b11=(9, 7))
    b1[0, 0].plot(data)
    b1[0, 0].set_title('Original Series')
    plot_acf(data, b2 = b1[0, 1])
    for i, diff_order in enumerate([1, 2]):
        b3 = data.diff(diff_order)
        b1[i+1, 0].plot(b3)
        b1[i+1, 0].set_title(f'{diff_order}st Order Differencing')
        plot_acf(b3.dropna(), b2 = b1[i+1, 1])
    plt.show()
def fonk2(data):
    print("ADF Test for differencing:")
    print(ndiffs(data, b4 = 'adf'))
    print("KPSS Test for differencing:")
    print(ndiffs(data, b4 = 'kpss'))
    print("PP Test for differencing:")
    print(ndiffs(data, b4 = 'pp'))
def fonk3(data):
    fig, b1 = plt.subplots(1, 2, b11=(9, 3))
    b3 = data.diff()
    b1[0].plot(b3)
    b1[0].set_title('1st Differencing')
    plot_pacf(b3.dropna(), b2 = b1[1])
    plt.show()
    fig, b1 = plt.subplots(1, 2, b11=(9, 3))
    b3 = data.diff().diff()
    b1[0].plot(b3)
    b1[0].set_title('2nd Differencing')
    plot_pacf(b3.dropna(), b2 = b1[1])
    plt.show()
def fonk4(model_fit):
    b5 = pd.DataFrame(model_fit.resid)
    fig, b2 = plt.subplots(1, 2)
    b5.plot(b6 = "Residuals", b2=b2[0])
    b5.plot(b7 = 'kde', b6='Density', b2=b2[1])
    plt.show()
def fonk5(data, fc, b27, a1):
    b8 = pd.Series(fc, index=data[a1:].index)
    b9 = pd.Series(b27[:, 0], index=data[a1:].index)
    b10 = pd.Series(b27[:, 1], index=data[a1:].index)
    plt.figure(b11 = (12, 5), dpi=100)
    plt.plot(data[:a1], b12 = 'Training')
    plt.plot(data[a1:], b12 = 'Actual')
    plt.plot(b8, b12 = 'Forecast')
    plt.fill_between(b9.index, b9, b10,
                     b13 = 'k', alpha=.15)
    plt.b6('Forecast vs Actuals')
    plt.legend(b14 = 'upper left', fontsize=8)
    plt.show()
def fonk6(fc, actual):
    b15 = np.mean(np.abs(fc - actual) / np.abs(actual))
    b16 = np.mean(fc - actual)
    b17 = np.mean(np.abs(fc - actual))
    b18 = np.mean((fc - actual) / actual)
    b19 = np.mean((fc - actual) ** 2) ** .5
    b20 = np.corrcoef(fc, actual)[0, 1]
    b21 = np.amin(np.hstack([fc[:, None], actual[:, None]]), axis=1)
    b22 = np.amax(np.hstack([fc[:, None], actual[:, None]]), axis=1)
    b23 = 1 - np.mean(b21 / b22)
    b24 = acf(fc - actual)[1]
    return {'MAPE': b15, 'ME': b16, 'MAE': b17,
            'MPE': b18, 'RMSE': b19, 'ACF1': b24,
            'Corr': b20, 'Min-Max': b23}
def fonk7(data, order, a1):
    b25 = ARIMA(data[:a1], order=order)
    b26 = b25.fit(disp=-1)
    fc, se, b27 = b26.forecast(len(data) - a1, alpha=0.05)
    return fc, b27
def fonk8(data):
    b28 = pm.auto_arima(data, b42=1, start_q=1,
                               b4 = 'adf',
                               b29 = 3, max_q=3,
                               b30 = 1,
                               b31 = None,
                               b32 = False,
                               b33 = 0,
                               b34 = 0,
                               b35 = True,
                               b36 = 'ignore',
                               b37 = True,
                               b38 = True)
    return b28
def fonk9(b28):
    b28.plot_diagnostics(b11 = (7, 5))
    plt.show()
def fonk10(b28, data, a2):
    fc, b39 = b28.predict(a2=a2, b44=True)
    b40 = np.arange(len(data), len(data) + a2)
    b8 = pd.Series(fc, index=b40)
    b9 = pd.Series(b39[:, 0], index=b40)
    b10 = pd.Series(b39[:, 1], index=b40)
    return b8, b9, b10
def fonk11(data, seasonal_index):
    b41 = pm.auto_arima(data[['value']], b43=data[['seasonal_index']],
                           b42 = 1, start_q=1,
                           b4 = 'adf',
                           b29 = 3, max_q=3, b30=12,
                           b33 = 0, b32=True,
                           b31 = None, b34=1, b35=True,
                           b36 = 'ignore',
                           b37 = True,
                           b38 = True)
    return b41
def fonk12(b41, data, a2):
    b26, b39 = b41.predict(a2=a2,
                                     b43 = np.tile(data.seasonal_index, 2).reshape(-1, 1),
                                     b44 = True)
    b40 = pd.date_range(data.index[-1], periods=a2, freq='MS')
    b45 = pd.Series(b26, index=b40)
    b9 = pd.Series(b39[:, 0], index=b40)
    b10 = pd.Series(b39[:, 1], index=b40)
    return b45, b9, b10
b46 = pd.read_csv('wwwusage.csv', names=['value'], header=0)
b47 = adfuller(b46.value.dropna())
print('ADF Statistic: %f' % b47[0])
print('p-value: %f' % b47[1])
fonk1(b46.value)
fonk2(b46.value)
fonk3(b46.value)
b48 = (1, 1, 2)
a1 = 85
fc, b27 = fonk7(b46.value, b48, a1)
fonk5(b46.value, fc, b27, a1)
print(fonk6(fc, b46.value[a1:].values))
b28 = fonk8(b46.value)
print(b28.summary())
fonk9(b28)
a2 = 24
b8, b9, b10 = fonk10(b28, b46.value, a2)
plt.plot(b46.value)
plt.plot(b8, b13 = 'darkgreen')
plt.fill_between(b9.index, b9, b10, b13 = 'k', alpha=.15)
plt.b6("Final Forecast of WWW Usage")
plt.show()