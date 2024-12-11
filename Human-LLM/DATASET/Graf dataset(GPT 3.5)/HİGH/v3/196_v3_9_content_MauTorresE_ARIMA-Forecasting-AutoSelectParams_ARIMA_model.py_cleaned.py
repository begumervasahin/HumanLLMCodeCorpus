import os
import time
import datetime
import numpy as np
import pandas as pd
import json
from os import listdir
from os.path import isfile, join
from objdict import ObjDict
import pyflux as pf
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
def fonk1(timeseries, b1 = 12):
    b2 = timeseries.rolling(b1=b1).mean()
    b3 = timeseries.rolling(b1=b1).std()
    return b2, b3
def fonk2(timeseries, b2, b3):
    plt.figure(b4 = (12, 8))
    plt.b32(timeseries, b5 = 'blue', label='Original')
    plt.b32(b2, b5 = 'red', label='Rolling Mean')
    plt.b32(b3, b5 = 'black', label='Rolling Std')
    plt.legend(b6 = 'best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
def fonk3(timeseries):
    b7 = adfuller(timeseries, autolag='AIC')
    b8 = pd.Series(b7[0:4], index=['Test Statistic', 'p-value', 'Lags Used', 'Number of Observations Used'])
    for key, value in b7[4].items():
        b8['Critical Value (%s)' % key] = value
    return b8
def fonk4(b28, b29):
    b9 = [datetime.datetime.fromtimestamp(date / 1000.0).strftime('%Y-%m-%d-%H') for date in b28]
    b10 = pd.to_datetime(b9)
    b11 = pd.Series(b29, index=b10)
    b11 = b11[~((b11 - b11.mean()).abs() > 3 * b11.std())]
    b11 = b11[(b11 != 0)]
    return b11
def fonk5(b30):
    b12 = []
    for d in range(0, 3):
        for p in range(0, 6):
            for b19 in range(0, 6):
                try:
                    b13 = ARIMA(b30, order=(p, d, b19))
                    b14 = b13.fit(disp=-1)
                    b15 = np.sqrt((b14.fittedvalues - b30[1:]) ** 2)
                    b16 = b15.mean()
                    b17 = 100 - b16
                    b12.append([p, d, b19, b17])
                except:
                    pass
    b18 = sorted(b12, key=lambda x: x[3])[-1]
    return b18
def fonk6(b30, b18):
    p, d, b19 = b18[0], b18[1], b18[2]
    b13 = ARIMA(b30, order=(p, d, b19))
    b14 = b13.fit(disp=-1)
    return b14
def fonk7(b14, b30, b31):
    b20 = b14.predict(start=b30.index[1], end=b31.index[-1], dynamic=True)
    b15 = np.sqrt((b20 - b31) ** 2)
    b16 = b15.mean()
    b17 = 100 - b16
    return b20, b15, b16, b17
def fonk8(b20, b31, b15):
    b21 = []
    for i in range(0, len(b15)):
        b22 = ObjDict()
        b22.b23 = str(b20.index[i])
        b22.b24 = b20[i]
        b22.b15 = b15[i]
        b21.append(b22)
    return json.dumps(b21)
def fonk9(b25 = '', js=None):
    if b25:
        os.chdir(b25)
        b26 = [f for f in listdir(b25) if isfile(join(b25, f))]
        b27 = []
        for dat in b26:
            with open(dat) as json_data:
                b27.append(json.load(json_data))
        b28 = []
        b29 = []
        for i in range(0, len(b27)):
            for j in b27[0]:
                b28.append(j['b23'])
                b29.append(j['valor'])
    elif js:
        b28 = [i['b23'] for i in js]
        b29 = [i['valor'] for i in js]
    b11 = fonk4(b28, b29)
    b30 = b11[0:int(len(b11) * .9)]
    b31 = b11[int(len(b11) * .9) + 1:len(b11)]
    test_stationarity(b30, b32 = True)
    b2, b3 = fonk1(b30)
    fonk2(b30, b2, b3)
    b33 = fonk3(b30)
    print(b33)
    b18 = fonk5(b30)
    b14 = fonk6(b30, b18)
    b20, b15, b16, b17 = fonk7(b14, b30, b31)
    return fonk8(b20, b31, b15), b16, b17
