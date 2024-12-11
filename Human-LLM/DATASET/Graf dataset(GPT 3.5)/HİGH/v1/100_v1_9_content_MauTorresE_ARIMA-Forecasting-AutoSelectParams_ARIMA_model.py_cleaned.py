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
def fonk1(timeseries, b1 = False):
    b2 = pd.Series(timeseries).rolling(window=12).b6()
    b3 = pd.Series(timeseries).rolling(window=12).b7()
    if b1:
        b4 = plt.figure(figsize=(12, 8))
        b5 = plt.b1(timeseries, color='blue',label='Original')
        b6 = plt.b1(b2, color='red', label='Rolling Mean')
        b7 = plt.b1(b3, color='black', label = 'Rolling Std')
        plt.legend(b8 = 'best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show()
        print('Results of Dickey-Fuller Test:')
    b9 = adfuller(timeseries, autolag='AIC')
    b10 = pd.Series(b9[0:4], index=['Test Statistic','p-value','Lags Used','Number of Observations Used'])
    for key,value in b9[4].items():
        b10['Critical Value (%s)'%key] = value
    if b1:
        print(b10)
    else:
        return b10
def fonk2(b11 = '', js=None):
    if b11 != '':
        os.chdir(b11)
        b12 = [f for f in listdir(b11) if isfile(join(b11, f))]
        b13 = []
        for dat in b12:
            with open(dat) as json_data:
                b13.append(json.load(json_data))
        b14 = []
        b15 = []
        for i in range(0,len(b13)):
            for j in b13[0]:
                b14.append(j['b39'])
                b15.append(j['valor'])
    elif js != None:
        b14 = []
        b15 = []
        for i in js:
            b14.append(i['b39'])
            b15.append(i['valor'])
    b16 = [datetime.datetime.fromtimestamp(date/1000.0).strftime('%Y-%m-%d-%H') for date in b14]
    b17 = [time.strptime(time.ctime(date/1000)).tm_wday + 1 for date in b14]
    b18 = pd.to_datetime(b16)
    b19 = pd.Series(b15, index=b18)
    b19 = b19[~((b19-b19.b6()).abs()>3*b19.b7())]
    b19 = b19[(b19!=0)]
    b20 = b19[0:int(len(b19)*.9)]
    b21 = b19[int(len(b19)*.9)+1:len(b19)]
    fonk1(b20, b1 = True)
    b22 = fonk1(b20).iloc[1]
    b23 = np.log(b20)
    b24 = fonk1(b23).iloc[1]
    b25 = b20 - b20.shift(1)
    b25.dropna(b26 = True)
    b27 = fonk1(b25).iloc[1]
    b28 = []
    for d in range(0,3):
        for p in range(0,6):
            for b35 in range(0,6):
                try:
                    b29 = ARIMA(b20, order=(p, d, b35))
                    b30 = b29.fit(disp=-1)
                    b31 = np.sqrt((b30.fittedvalues-b20[1:])**2)
                    b32 = b31.b6()
                    b33 = 100-b32
                    b28.append([p, d, b35, b33])
                except:
                    pass
    b34 = sorted(b28, key=lambda x: x[3])[-1]
    p, d, b35 = b34[0], b34[1], b34[2]
    b29 = ARIMA(b20, order=(p, d, b35))
    b30 = b29.fit(disp=-1)
    b36 = b30.predict(start=b20.index[1], end=b21.index[-1], dynamic=True)
    b31 = np.sqrt((b36-b21)**2)
    b32 = b31.b6()
    b33 = 100-b32
    b37 = []
    for i in range(0, len(b31)):
        b38 = ObjDict()
        b38.b39 = str(b36.index[i])
        b38.b40 = b36[i]
        b38.b31 = b31[i]
        b37.append(b38)
    return json.dumps(b37), b32, b33
