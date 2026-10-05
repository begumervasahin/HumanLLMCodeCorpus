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
def calculate_rolling_statistics(timeseries, window=12):
    rolling_mean = timeseries.rolling(window=window).mean()
    rolling_std = timeseries.rolling(window=window).std()
    return rolling_mean, rolling_std
def plot_rolling_statistics(timeseries, rolling_mean, rolling_std):
    plt.figure(figsize=(12, 8))
    plt.plot(timeseries, color='blue', label='Original')
    plt.plot(rolling_mean, color='red', label='Rolling Mean')
    plt.plot(rolling_std, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
def perform_dickey_fuller_test(timeseries):
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', 'Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    return dfoutput
def preprocess_data(fechas, valores):
    fechas_format = [datetime.datetime.fromtimestamp(date / 1000.0).strftime('%Y-%m-%d-%H') for date in fechas]
    fechas_pandas = pd.to_datetime(fechas_format)
    dframe = pd.Series(valores, index=fechas_pandas)
    dframe = dframe[~((dframe - dframe.mean()).abs() > 3 * dframe.std())]
    dframe = dframe[(dframe != 0)]
    return dframe
def find_best_arima_params(features_train):
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
    return params
def fit_arima_model(features_train, params):
    p, d, q = params[0], params[1], params[2]
    model_diff = ARIMA(features_train, order=(p, d, q))
    results_ARIMA_diff = model_diff.fit(disp=-1)
    return results_ARIMA_diff
def make_predictions(results_ARIMA_diff, features_train, features_test):
    predictions_ARIMA = results_ARIMA_diff.predict(start=features_train.index[1], end=features_test.index[-1], dynamic=True)
    error = np.sqrt((predictions_ARIMA - features_test) ** 2)
    error_prom = error.mean()
    accuracy = 100 - error_prom
    return predictions_ARIMA, error, error_prom, accuracy
def prepare_output(predictions_ARIMA, features_test, error):
    data = []
    for i in range(0, len(error)):
        entry = ObjDict()
        entry.fecha = str(predictions_ARIMA.index[i])
        entry.prediccion = predictions_ARIMA[i]
        entry.error = error[i]
        data.append(entry)
    return json.dumps(data)
def fit_models(mypath='', js=None):
    if mypath:
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
    elif js:
        fechas = [i['fecha'] for i in js]
        valores = [i['valor'] for i in js]
    dframe = preprocess_data(fechas, valores)
    features_train = dframe[0:int(len(dframe) * .9)]
    features_test = dframe[int(len(dframe) * .9) + 1:len(dframe)]
    test_stationarity(features_train, plot=True)
    rolling_mean, rolling_std = calculate_rolling_statistics(features_train)
    plot_rolling_statistics(features_train, rolling_mean, rolling_std)
    dftest_result = perform_dickey_fuller_test(features_train)
    print(dftest_result)
    params = find_best_arima_params(features_train)
    results_ARIMA_diff = fit_arima_model(features_train, params)
    predictions_ARIMA, error, error_prom, accuracy = make_predictions(results_ARIMA_diff, features_train, features_test)
    return prepare_output(predictions_ARIMA, features_test, error), error_prom, accuracy
