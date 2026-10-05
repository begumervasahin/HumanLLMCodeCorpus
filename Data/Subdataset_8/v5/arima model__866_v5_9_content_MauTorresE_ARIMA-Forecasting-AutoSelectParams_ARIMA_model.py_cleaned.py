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
def load_data(mypath='', js=None):
    if mypath != '':
        os.chdir(mypath)
        files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        data = []
        for file in files:
            with open(file) as json_data:
                data.extend(json.load(json_data))
    elif js is not None:
        data = js
    else:
        raise ValueError("No data provided.")
    fechas, valores = [], []
    for entry in data:
        fechas.append(entry['fecha'])
        valores.append(entry['valor'])
    return fechas, valores
def preprocess_data(fechas, valores):
    fechas_format = [datetime.datetime.fromtimestamp(date/1000.0).strftime('%Y-%m-%d-%H') for date in fechas]
    fechas_pandas = pd.to_datetime(fechas_format)
    dframe = pd.Series(valores, index=fechas_pandas)
    dframe = dframe[~((dframe-dframe.mean()).abs() > 3*dframe.std())]
    dframe = dframe[dframe != 0]
    return dframe
def split_data(dframe):
    train_size = int(len(dframe) * 0.9)
    features_train = dframe.iloc[:train_size]
    features_test = dframe.iloc[train_size:]
    return features_train, features_test
def test_stationarity(timeseries, plot=False):
    rolmean = timeseries.rolling(window=12).mean()
    rolstd = timeseries.rolling(window=12).std()
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', 'Lags Used', 'Number of Observations Used'])
    if plot:
        plt.plot(timeseries, color='blue', label='Original')
        plt.plot(rolmean, color='red', label='Rolling Mean')
        plt.plot(rolstd, color='black', label='Rolling Std')
        plt.legend(loc='best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show()
        print('Results of Dickey-Fuller Test:')
        print(dfoutput)
    return dfoutput
def find_best_arima_order(timeseries):
    p_values = range(6)
    d_values = range(3)
    q_values = range(6)
    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order = (p, d, q)
                try:
                    model = ARIMA(timeseries, order=order)
                    model_fit = model.fit(disp=0)
                    error = np.sqrt(np.mean((model_fit.fittedvalues - timeseries[1:])**2))
                    if error < best_score:
                        best_score, best_cfg = error, order
                except:
                    continue
    return best_cfg
def fit_arima_model(timeseries, order):
    model = ARIMA(timeseries, order=order)
    model_fit = model.fit(disp=0)
    return model_fit.forecast(steps=len(timeseries)),
def evaluate_model(predictions, features_test):
    error = np.sqrt(np.mean((predictions - features_test)**2))
    accuracy = 100 - error.mean()
    return error.mean(), accuracy
def prepare_results(predictions, features_test, error):
    data = []
    for i in range(len(predictions)):
        entry = ObjDict()
        entry.fecha = str(features_test.index[i])
        entry.prediccion = predictions[i]
        entry.error = error[i]
        data.append(entry)
    return json.dumps(data)
def fit_models(mypath='', js=None):
    fechas, valores = load_data(mypath, js)
    dframe = preprocess_data(fechas, valores)
    features_train, features_test = split_data(dframe)
    test_stationarity(features_train, plot=True)
    order = find_best_arima_order(features_train)
    model_fit = fit_arima_model(features_train, order)
    predictions = model_fit.forecast(steps=len(features_test))[0]
    error, accuracy = evaluate_model(predictions, features_test)
    result = prepare_results(predictions, features_test, error)
    return result, error, accuracy
