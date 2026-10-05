import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.b9 import ARIMA
import pmdarima as pm
b1 = pd.read_csv('wwwusage.csv', names=['value'], header=0)
def fonk1(data):
    b2 = adfuller(data.dropna())
    print('ADF Statistic: %f' % b2[0])
    print('p-value: %f' % b2[1])
def fonk2(data):
    fig, b3 = plt.subplots(3, 2, sharex=True)
    b3[0, 0].plot(data)
    b3[0, 0].set_title('Original Series')
    plot_acf(data, b4 = b3[0, 1])
    b3[1, 0].plot(data.diff())
    b3[1, 0].set_title('1st Order Differencing')
    plot_acf(data.diff().dropna(), b4 = b3[1, 1])
    b3[2, 0].plot(data.diff().diff())
    b3[2, 0].set_title('2nd Order Differencing')
    plot_acf(data.diff().diff().dropna(), b4 = b3[2, 1])
    plt.show()
def fonk3(data):
    b5 = data
    print("ADF Test Differencing:", ndiffs(b5, b6 = 'adf'))
    print("KPSS Test Differencing:", ndiffs(b5, b6 = 'kpss'))
    print("PP Test Differencing:", ndiffs(b5, b6 = 'pp'))
def fonk4(data):
    fig, b3 = plt.subplots(1, 2, sharex=True)
    b3[0].plot(data.diff())
    b3[0].set_title('1st Differencing')
    b3[1].set(b7 = (0, 5))
    plot_pacf(data.diff().dropna(), b4 = b3[1])
    plt.show()
def fonk5(data, b8 = (1, 1, 2)):
    b9 = ARIMA(data, b8=b8)
    b10 = b9.fit(disp=0)
    print(b10.summary())
    return b10
def fonk6(b10):
    b11 = pd.DataFrame(b10.resid)
    fig, b4 = plt.subplots(1, 2)
    b11.plot(b12 = "Residuals", b4=b4[0])
    b11.plot(b13 = 'kde', b12='Density', b4=b4[1])
    plt.show()
def fonk7(b37, b6, forecast, confidence_interval):
    b14 = pd.Series(forecast, index=b6.index)
    b15 = pd.Series(confidence_interval[:, 0], index=b6.index)
    b16 = pd.Series(confidence_interval[:, 1], index=b6.index)
    plt.figure(b17 = (12, 5), dpi=100)
    plt.plot(b37, b18 = 'training')
    plt.plot(b6, b18 = 'actual')
    plt.plot(b14, b18 = 'forecast')
    plt.fill_between(b15.index, b15, b16, b19 = 'k', alpha=.15)
    plt.b12('Forecast vs Actuals')
    plt.legend(b20 = 'upper left', fontsize=8)
    plt.show()
def fonk8(forecast, actual):
    b21 = np.mean(np.abs(forecast - actual) / np.abs(actual))
    b22 = np.mean(forecast - actual)
    b23 = np.mean(np.abs(forecast - actual))
    b24 = np.mean((forecast - actual) / actual)
    b25 = np.mean((forecast - actual) ** 2) ** .5
    b26 = np.corrcoef(forecast, actual)[0, 1]
    b27 = np.amin(np.hstack([forecast[:, None], actual[:, None]]), axis=1)
    b28 = np.amax(np.hstack([forecast[:, None], actual[:, None]]), axis=1)
    b29 = 1 - np.mean(b27 / b28)
    b30 = acf(fc - b6)[1]
    return {'b21': b21, 'b22': b22, 'b23': b23, 'b24': b24, 'b25': b25, 'b30': b30, 'b26': b26, 'b29': b29}
def fonk9(data):
    b9 = pm.auto_arima(data, start_p=1, start_q=1, b6='adf', max_p=3, max_q=3, m=1, d=None,
                          b31 = False, start_P=0, D=0, trace=True, error_action='ignore',
                          b32 = True, stepwise=True)
    print(b9.summary())
    return b9
def fonk10(b9):
    b9.plot_diagnostics(b17 = (7, 5))
    plt.show()
def fonk11(b9, data, b33 = 24):
    fc, b34 = b9.predict(b33=b33, return_conf_int=True)
    b35 = np.arange(len(data), len(data) + b33)
    b14 = pd.Series(fc, index=b35)
    b15 = pd.Series(b34[:, 0], index=b35)
    b16 = pd.Series(b34[:, 1], index=b35)
    plt.plot(data)
    plt.plot(b14, b19 = 'darkgreen')
    plt.fill_between(b15.index, b15, b16, b19 = 'k', alpha=.15)
    plt.b12("Final Forecast of WWW Usage")
    plt.show()
fonk1(b1.value)
fonk2(b1.value)
fonk3(b1.value)
fonk4(b1.value)
b10 = fonk5(b1.value, b8=(1, 1, 2))
fonk6(b10)
b10.plot_predict(b36 = False)
plt.show()
b37 = b1.value[:85]
b6 = b1.value[85:]
b9 = ARIMA(b37, b8=(1, 1, 1))
b38 = b9.fit(disp=-1)
fc, se, b39 = b38.forecast(15, alpha=0.05)
fonk7(b37, b6, fc, b39)
print(fonk8(fc, b6.values))
b9 = fonk9(b1.value)
fonk10(b9)
fonk11(b9, b1.value)