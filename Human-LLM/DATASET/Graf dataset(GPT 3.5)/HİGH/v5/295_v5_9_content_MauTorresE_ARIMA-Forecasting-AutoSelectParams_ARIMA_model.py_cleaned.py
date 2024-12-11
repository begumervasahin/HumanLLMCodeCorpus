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
def fonk1(b1 = '', js=None):
    if b1 != '':
        os.chdir(b1)
        b2 = [f for f in listdir(b1) if isfile(join(b1, f))]
        b3 = []
        for file in b2:
            with open(file) as json_data:
                b3.extend(json.load(json_data))
    elif js is not None:
        b3 = js
    else:
        raise ValueError("No b3 provided.")
    fechas, b4 = [], []
    for b28 in b3:
        fechas.append(b28['b29'])
        b4.append(b28['valor'])
    return fechas, b4
def fonk2(fechas, b4):
    b5 = [datetime.datetime.fromtimestamp(date/1000.0).strftime('%Y-%m-%d-%H') for date in fechas]
    b6 = pd.to_datetime(b5)
    b7 = pd.Series(b4, index=b6)
    b7 = b7[~((b7-b7.mean()).abs() > 3*b7.std())]
    b7 = b7[b7 != 0]
    return b7
def fonk3(b7):
    b8 = int(len(b7) * 0.9)
    b9 = b7.iloc[:b8]
    b10 = b7.iloc[b8:]
    return b9, b10
def fonk4(timeseries, b11 = False):
    b12 = timeseries.rolling(window=12).mean()
    b13 = timeseries.rolling(window=12).std()
    b14 = adfuller(timeseries, autolag='AIC')
    b15 = pd.Series(b14[0:4], index=['Test Statistic', 'p-value', 'Lags Used', 'Number of Observations Used'])
    if b11:
        plt.b11(timeseries, b16 = 'blue', label='Original')
        plt.b11(b12, b16 = 'red', label='Rolling Mean')
        plt.b11(b13, b16 = 'black', label='Rolling Std')
        plt.legend(b17 = 'best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show()
        print('Results of Dickey-Fuller Test:')
        print(b15)
    return b15
def fonk5(timeseries):
    b18 = range(6)
    b19 = range(3)
    b20 = range(6)
    best_score, b21 = float("inf"), None
    for p in b18:
        for d in b19:
            for q in b20:
                b22 = (p, d, q)
                try:
                    b23 = ARIMA(timeseries, b22=b22)
                    b24 = b23.fit(disp=0)
                    b25 = np.sqrt(np.mean((b24.fittedvalues - timeseries[1:])**2))
                    if b25 < best_score:
                        best_score, b21 = b25, b22
                except:
                    continue
    return b21
def fonk6(timeseries, b22):
    b23 = ARIMA(timeseries, b22=b22)
    b24 = b23.fit(disp=0)
    return b24.forecast(b26 = len(timeseries)),
def fonk7(b31, b10):
    b25 = np.sqrt(np.mean((b31 - b10)**2))
    b27 = 100 - b25.mean()
    return b25.mean(), b27
def fonk8(b31, b10, b25):
    b3 = []
    for i in range(len(b31)):
        b28 = ObjDict()
        b28.b29 = str(b10.index[i])
        b28.b30 = b31[i]
        b28.b25 = b25[i]
        b3.append(b28)
    return json.dumps(b3)
def fonk9(b1 = '', js=None):
    fechas, b4 = fonk1(b1, js)
    b7 = fonk2(fechas, b4)
    b9, b10 = fonk3(b7)
    fonk4(b9, b11 = True)
    b22 = fonk5(b9)
    b24 = fonk6(b9, b22)
    b31 = b24.forecast(b26=len(b10))[0]
    b25, b27 = fonk7(b31, b10)
    b32 = fonk8(b31, b10, b25)
    return b32, b25, b27
