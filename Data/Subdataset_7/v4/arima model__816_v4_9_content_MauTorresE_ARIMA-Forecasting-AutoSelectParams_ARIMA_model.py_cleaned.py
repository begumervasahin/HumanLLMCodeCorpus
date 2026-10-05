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
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.arima_model import ARIMA
def fonk1(b1 = '', js=None):
    if b1 != '':
        os.chdir(b1)
        b2 = [f for f in listdir(b1) if isfile(join(b1, f))]
        b3 = []
        for dat in b2:
            with open(dat) as json_data:
                b3.append(json.load(json_data))
        fechas, b4 = [], []
        for j in b3[0]:
            fechas.append(j['b8'])
            b4.append(j['valor'])
    elif js != None:
        fechas, b4 = [], []
        for i in js:
            fechas.append(i['b8'])
            b4.append(i['valor'])
    b5 = [fechas[x:x+1] for x in range(0, len(fechas), 1)]
    b6 = [datetime.datetime.fromtimestamp(date/1000.0).strftime('%Y-%m-%d-%H') for date in fechas]
    ano, mes, dia, b7 = [], [], [], []
    for date in b6:
        b8 = date.split('-')
        ano.append(int(b8[0]))
        mes.append(int(b8[1]))
        dia.append(int(b8[2]))
        b7.append(int(b8[3]))
    b9 = [time.strptime(time.ctime(date/1000)).tm_wday + 1 for date in fechas]
    b10 = pd.to_datetime(b6)
    b11 = pd.Series(b4, index=b10)
    b11 = b11[~((b11-b11.mean()).abs() > 3*b11.std())]
    b11 = b11[(b11 != 0)]
    b12 = b11[0:int(len(b11)*0.9)]
    b13 = b11[int(len(b11)*0.9)+1:len(b11)]
    def fonk2(timeseries, b14 = False):
        b15 = pd.Series(timeseries).rolling(window=12).mean()
        b16 = pd.Series(timeseries).rolling(window=12).std()
        b17 = adfuller(timeseries, autolag='AIC')
        b18 = pd.Series(b17[0:4], index=['Test Statistic', 'p-value', 'Lags Used', 'Number of Observations Used'])
        if b14:
            plt.b14(timeseries, b19 = 'blue', label='Original')
            plt.b14(b15, b19 = 'red', label='Rolling Mean')
            plt.b14(b16, b19 = 'black', label='Rolling Std')
            plt.legend(b20 = 'best')
            plt.title('Rolling Mean & Standard Deviation')
            plt.show()
            print('Results of Dickey-Fuller Test:')
            print(b18)
        else:
            return b18
    def fonk3(timeseries):
        b21 = range(0, 6)
        b22 = range(0, 3)
        b23 = range(0, 6)
        best_score, b24 = float("inf"), None
        for p in b21:
            for d in b22:
                for q in b23:
                    b25 = (p, d, q)
                    try:
                        b26 = ARIMA(timeseries, b25=b25)
                        b27 = b26.fit(disp=0)
                        b28 = np.sqrt(np.mean((b27.fittedvalues - timeseries[1:])**2))
                        if b28 < best_score:
                            best_score, b24 = b28, b25
                    except:
                        continue
        return b24
    fonk2(b12, b14 = True)
    b25 = fonk3(b12)
    b26 = ARIMA(b12, b25=b25)
    b27 = b26.fit(disp=0)
    b29 = b27.forecast(steps=len(b13))[0]
    b28 = np.sqrt(np.mean((b29 - b13)**2))
    b30 = 100 - b28.mean()
    b31 = []
    for i in range(len(b29)):
        b32 = ObjDict()
        b32.b8 = str(b13.index[i])
        b32.b33 = b29[i]
        b32.b28 = b28[i]
        b31.append(b32)
    return json.dumps(b31), b28.mean(), b30
