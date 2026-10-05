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
def test_stationarity(timeseries, plot=False):
    rolling_mean = pd.Series(timeseries).rolling(window=12).mean()
    rolling_std = pd.Series(timeseries).rolling(window=12).std()
    if plot:
        plt.figure(figsize=(12, 8))
        plt.plot(timeseries, color='blue', label='Original')
        plt.plot(rolling_mean, color='red', label='Rolling Mean')
        plt.plot(rolling_std, color='black', label='Rolling Std')
        plt.legend(loc='best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show()
        print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', 'Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    if plot:
        print(dfoutput)
    else:
        return dfoutput
def fit_models(mypath='', js=None):
    if mypath != '':
        os.chdir(mypath)
        lista_archivos = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        lista_dat = []
        for dat in lista_archivos:
            with open(dat) as json_data:
                lista_dat.append(json.load(json_data))
        fechas = []
        valores = []
        for i in range(0, len(lista_dat)):
            for j in lista_dat[0]:
                fechas.append(j['fecha'])
                valores.append(j['valor'])
    elif js != None:
        fechas = []
        valores = []
        for i in js:
            fechas.append(i['fecha'])
            valores.append(i['valor'])
    fechas_format = [datetime.datetime.fromtimestamp(date / 1000.0).strftime('%Y-%m-%d-%H') for date in fechas]
    dia_semana = [time.strptime(time.ctime(date / 1000)).tm_wday + 1 for date in fechas]
    fechas_pandas = pd.to_datetime(fechas_format)
    dframe = pd.Series(valores, index=fechas_pandas)
    dframe = dframe[~((dframe - dframe.mean()).abs() > 3 * dframe.std())]
    dframe = dframe[(dframe != 0)]
    features_train = dframe[0:int(len(dframe) * .9)]
    features_test = dframe[int(len(dframe) * .9) + 1:len(dframe)]
    test_stationarity(features_train, plot=True)
    acc_list = []
    for d in range(0, 3):
        for p in range(0, 6):
            for q in range(0, 6):
                try:
                    model_diff = ARIMA(features_train, order=(p, d, q))
                    results_ARIMA_diff = model_diff.fit(disp=-1)
                    error = np.sqrt((results_ARIMA_diff.fittedvalues - features_train[1:]) ** 2)
                    error_prom = error.mean()
                    accuracy = 100 - error_prom
                    acc_list.append([p, d, q, accuracy])
                except:
                    pass
    params = sorted(acc_list, key=lambda x: x[3])[-1]
    p, d, q = params[0], params[1], params[2]
    model_diff = ARIMA(features_train, order=(p, d, q))
    results_ARIMA_diff = model_diff.fit(disp=-1)
    predictions_ARIMA = results_ARIMA_diff.predict(start=features_train.index[1], end=features_test.index[-1], dynamic=True)
    error = np.sqrt((predictions_ARIMA - features_test) ** 2)
    error_prom = error.mean()
    accuracy = 100 - error_prom
    data = []
    for i in range(0, len(error)):
        entry = ObjDict()
        entry.fecha = str(predictions_ARIMA.index[i])
        entry.prediccion = predictions_ARIMA[i]
        entry.error = error[i]
        data.append(entry)
    return json.dumps(data), error_prom, accuracy
