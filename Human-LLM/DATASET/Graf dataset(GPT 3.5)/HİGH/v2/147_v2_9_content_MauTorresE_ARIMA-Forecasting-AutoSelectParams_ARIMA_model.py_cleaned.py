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
def fonk1(timeseries, b1 = False):
    b2 = pd.Series(timeseries).rolling(window=12).mean()
    b3 = pd.Series(timeseries).rolling(window=12).std()
    if b1:
        plt.figure(b4 = (12, 8))
        plt.b1(timeseries, b5 = 'blue', label='Original')
        plt.b1(b2, b5 = 'red', label='Rolling Mean')
        plt.b1(b3, b5 = 'black', label='Rolling Std')
        plt.legend(b6 = 'best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show()
        print('Results of Dickey-Fuller Test:')
    b7 = adfuller(timeseries, autolag='AIC')
    b8 = pd.Series(b7[0:4], index=['Test Statistic', 'p-value', 'Lags Used', 'Number of Observations Used'])
    for key, value in b7[4].items():
        b8['Critical Value (%s)' % key] = value
    if b1:
        print(b8)
    else:
        return b8
def fonk2(b9 = '', js=None):
    if b9 != '':
        os.chdir(b9)
        b10 = [f for f in listdir(b9) if isfile(join(b9, f))]
        b11 = []
        for dat in b10:
            with open(dat) as json_data:
                b11.append(json.load(json_data))
        b12 = []
        b13 = []
        for i in range(0, len(b11)):
            for j in b11[0]:
                b12.append(j['b31'])
                b13.append(j['valor'])
    elif js != None:
        b12 = []
        b13 = []
        for i in js:
            b12.append(i['b31'])
            b13.append(i['valor'])
    b14 = [datetime.datetime.fromtimestamp(date / 1000.0).strftime('%Y-%m-%d-%H') for date in b12]
    b15 = [time.strptime(time.ctime(date / 1000)).tm_wday + 1 for date in b12]
    b16 = pd.to_datetime(b14)
    b17 = pd.Series(b13, index=b16)
    b17 = b17[~((b17 - b17.mean()).abs() > 3 * b17.std())]
    b17 = b17[(b17 != 0)]
    b18 = b17[0:int(len(b17) * .9)]
    b19 = b17[int(len(b17) * .9) + 1:len(b17)]
    fonk1(b18, b1 = True)
    b20 = []
    for d in range(0, 3):
        for p in range(0, 6):
            for b27 in range(0, 6):
                try:
                    b21 = ARIMA(b18, order=(p, d, b27))
                    b22 = b21.fit(disp=-1)
                    b23 = np.sqrt((b22.fittedvalues - b18[1:]) ** 2)
                    b24 = b23.mean()
                    b25 = 100 - b24
                    b20.append([p, d, b27, b25])
                except:
                    pass
    b26 = sorted(b20, key=lambda x: x[3])[-1]
    p, d, b27 = b26[0], b26[1], b26[2]
    b21 = ARIMA(b18, order=(p, d, b27))
    b22 = b21.fit(disp=-1)
    b28 = b22.predict(start=b18.index[1], end=b19.index[-1], dynamic=True)
    b23 = np.sqrt((b28 - b19) ** 2)
    b24 = b23.mean()
    b25 = 100 - b24
    b29 = []
    for i in range(0, len(b23)):
        b30 = ObjDict()
        b30.b31 = str(b28.index[i])
        b30.b32 = b28[i]
        b30.b23 = b23[i]
        b29.append(b30)
    return json.dumps(b29), b24, b25
