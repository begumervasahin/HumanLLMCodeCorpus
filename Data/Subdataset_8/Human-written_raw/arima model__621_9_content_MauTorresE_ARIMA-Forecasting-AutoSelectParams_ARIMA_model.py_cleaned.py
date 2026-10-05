
def fit_models(mypath='', js=None):
    '''
    Takes a file path with a file in json format, or a string with json structure
    Returns json (fecha, prediccion, error), error_prom, accuracy
    '''
    import os
    import time
    import datetime
    import numpy as np
    import pandas as pd
    import json
    from os import listdir
    from os.path import isfile, join
    from objdict import ObjDict
    if mypath != '':
        os.chdir(mypath)
        lista_archivos = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        lista_dat = []
        for dat in lista_archivos:
            with open(dat) as json_data:
                lista_dat.append(json.load(json_data))
        for i in range(0,len(lista_dat)):
            fechas = []
            valores = []
            for j in lista_dat[0]:
                fechas.append(j['fecha'])
                valores.append(j['valor'])
    elif js != None:
        fechas = []
        valores = []
        for i in js:
            fechas.append(i['fecha'])
            valores.append(i['valor'])
    fechas_list = [fechas[x:x+1] for x in xrange(0, len(fechas), 1)]
    fechas_format = []
    for date in fechas:
        fechas_format.append(datetime.datetime.fromtimestamp(date/1000.0).strftime('%Y-%m-%d-%H'))
    ano,mes,dia,hora = [],[],[],[]
    for date in fechas_format:
        fecha = date.split('-')
        ano.append(int(fecha[0]))
        mes.append(int(fecha[1]))
        dia.append(int(fecha[2]))
        hora.append(int(fecha[3]))
    dia_semana = []
    for date in fechas:
        if time.ctime(date/1000).split()[0] == 'Mon':
            dia_semana.append(1)
        elif time.ctime(date/1000).split()[0] == 'Tue':
            dia_semana.append(2)
        elif time.ctime(date/1000).split()[0] == 'Wed':
            dia_semana.append(3)
        elif time.ctime(date/1000).split()[0] == 'Thu':
            dia_semana.append(4)
        elif time.ctime(date/1000).split()[0] == 'Fri':
            dia_semana.append(5)
        elif time.ctime(date/1000).split()[0] == 'Sat':
            dia_semana.append(6)
        elif time.ctime(date/1000).split()[0] == 'Sun':
            dia_semana.append(7)
        else:
            print 'Error'
    fechas_pandas = pd.to_datetime(fechas_format)
    dframe = pd.Series(valores, index=fechas_pandas)
    import pyflux as pf
    from datetime import datetime
    import matplotlib.pyplot as plt
    dframe = dframe[~((dframe-dframe.mean()).abs()>3*dframe.std())]
    dframe= dframe[(dframe!=0)]
    features_train = dframe[0:int(len(dframe)*.9)]
    features_test = dframe[int(len(dframe)*.9)+1:len(dframe)]
    from statsmodels.tsa.stattools import adfuller
    def test_stationarity(timeseries, plot=False):
        rolmean = pd.rolling_mean(timeseries, window=12)
        rolstd = pd.rolling_std(timeseries, window=12)
        if plot:
            fig = plt.figure(figsize=(12, 8))
            orig = plt.plot(timeseries, color='blue',label='Original')
            mean = plt.plot(rolmean, color='red', label='Rolling Mean')
            std = plt.plot(rolstd, color='black', label = 'Rolling Std')
            plt.legend(loc='best')
            plt.title('Rolling Mean & Standard Deviation')
            plt.show()
            print 'Results of Dickey-Fuller Test:'
        dftest = adfuller(timeseries, autolag='AIC')
        dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value',
        '
        for key,value in dftest[4].items():
            dfoutput['Critical Value (%s)'%key] = value
        if plot:
            print dfoutput
        else:
            return dfoutput
    '''
    print 'Dickey-Fuller test for original data'
    test_stationarity(features_train, plot=True)
    '''
    p_value = test_stationarity(features_train).iloc[1]
    features_train_log = np.log(features_train)
    p_value_log = test_stationarity(features_train_log).iloc[1]
    features_train_diff = features_train - features_train.shift(1)
    features_train_diff.dropna(inplace=True)
    p_value_diff = test_stationarity(features_train_diff).iloc[1]
    features_train_diff2 = features_train_diff - features_train_diff.shift(1)
    features_train_diff2.dropna(inplace=True)
    p_value_diff2 = test_stationarity(features_train_diff2).iloc[1]
    train_log_diff = features_train_log - features_train_log.shift(1)
    train_log_diff.dropna(inplace=True)
    p_value_log_diff = test_stationarity(train_log_diff).iloc[1]
    train_log_diff2 = train_log_diff - train_log_diff.shift(1)
    train_log_diff2.dropna(inplace=True)
    p_value_log_diff2 = test_stationarity(train_log_diff2).iloc[1]
    p_value_list = [p_value, p_value_log, p_value_diff,
                    p_value_log_diff, p_value_diff2, p_value_log_diff2]
    winner_index = p_value_list.index(min(p_value_list))
    if winner_index == 0:
        winner = features_train
    if winner_index == 1:
        winner = features_train_log
    if winner_index == 2:
        winner = features_train_diff
    if winner_index == 3:
        winner = train_log_diff
    if winner_index == 4:
        winner = features_train_diff2
    if winner_index == 5:
        winner = train_log_diff2
    '''
    Number of AR (Auto-Regressive) terms (p): AR terms are just lags
        of dependent variable.
        For instance if p is 5, the predictors for x(t) will be x(t-1)â¦.x(t-5).
    Number of MA (Moving Average) terms (q): MA terms are lagged forecast errors
        in prediction equation.
        For instance if q is 5, the predictors for x(t) will be e(t-1)â¦.e(t-5)
        where e(i) is the difference
        between the moving average at ith instant and actual value.
    Number of Differences (d): These are the number of nonseasonal differences,
        i.e. in this case we took
        the first order difference. So either we can pass that variable and
        put d=0 or pass the original variable
        and put d=1. Both will generate same results.
    '''
    from statsmodels.tsa.stattools import acf, pacf
    lag_acf = acf(winner, nlags=20)
    lag_pacf = pacf(winner, nlags=20, method='ols')
    top_line = 1.96/np.sqrt(len(winner))
    '''
    q=0
    for i in lag_acf:
       if i > top_line:
           q+=1
       else:
           break
    p=0
    for i in lag_pacf:
       if i > top_line:
           p+=1
       else:
           break
    '''
    '''
    plt.subplot(121)
    plt.plot(lag_acf)
    plt.axhline(y=0,linestyle='--',color='gray')
    plt.axhline(y=-1.96/np.sqrt(len(winner)),linestyle='--',color='gray')
    plt.axhline(y=1.96/np.sqrt(len(winner)),linestyle='--',color='gray')
    plt.title('Autocorrelation Function')
    plt.subplot(122)
    plt.plot(lag_pacf)
    plt.axhline(y=0,linestyle='--',color='gray')
    plt.axhline(y=-1.96/np.sqrt(len(winner)),linestyle='--',color='gray')
    plt.axhline(y=1.96/np.sqrt(len(winner)),linestyle='--',color='gray')
    plt.title('Partial Autocorrelation Function')
    plt.tight_layout()
    plt.show()
    '''
    '''
    print('Enter the value of q, corresponding to the ACF graph')
    q = raw_input()
    print('Enter the value of p, corresponding to the PACF graph')
    p = raw_input()
    q = int(q)
    p = int(p)
    '''
    '''
    p â The lag value where the PACF chart crosses the upper confidence interval for the first time.
        In this case p=2.
    q â The lag value where the ACF chart crosses the upper confidence interval for the first time.
        In this case q=6.
    '''
    from statsmodels.tsa.arima_model import ARIMA
    acc_list = []
    for d in range(0,3):
        for p in range(0,6):
            for q in range(0,6):
                try:
                    model_diff = ARIMA(winner, order=(p, d, q))
                    results_ARIMA_diff = model_diff.fit(disp=-1)
                    error = np.sqrt((results_ARIMA_diff.fittedvalues-winner[1:])**2)
                    error_prom = error.mean()
                    accuracy = 100-error_prom
                    acc_list.append([p, d, q, accuracy])
                except:
                    next
    from operator import itemgetter
    params = sorted(acc_list, key=itemgetter(3))[len(acc_list)-1]
    p = params[0]
    d = params[1]
    q = params[2]
    model_diff = ARIMA(winner, order=(p, d, q))
    results_ARIMA_diff = model_diff.fit(disp=-1)
    '''
    plt.plot(winner)
    plt.plot(results_ARIMA_diff.fittedvalues, color='red')
    plt.title('RSS: %.4f'% sum((results_ARIMA_diff.fittedvalues-winner[2:])**2))
    plt.show()
    error = np.sqrt((results_ARIMA_diff.fittedvalues-winner)**2)
    error_prom = error.mean()
    accuracy = 100-error_prom
    '''
    if winner_index == 0:
        predictions_ARIMA = pd.Series(results_ARIMA_diff.fittedvalues, copy=True)
        pred_ARIMA_diff_corrected = predictions_ARIMA
    if winner_index == 1:
        predictions_ARIMA_diff = pd.Series(results_ARIMA_diff.fittedvalues, copy=True)
        pred_ARIMA_diff_corrected = np.exp(predictions_ARIMA_diff)
    if winner_index == 2:
        predictions_ARIMA_diff = pd.Series(results_ARIMA_diff.fittedvalues, copy=True)
        pred_ARIMA_diff_corrected = predictions_ARIMA_diff + features_train.shift(1)
        pred_ARIMA_diff_corrected = pred_ARIMA_diff_corrected[1:]
    if winner_index == 3:
        predictions_ARIMA_diff = pd.Series(results_ARIMA_diff.fittedvalues, copy=True)
        pred_ARIMA_diff_corrected = np.exp(predictions_ARIMA_diff)
        pred_ARIMA_diff_corrected = predictions_ARIMA_diff + features_train.shift(1)
        pred_ARIMA_diff_corrected = pred_ARIMA_diff_corrected[1:]
    if winner_index == 4:
        predictions_ARIMA_diff = pd.Series(results_ARIMA_diff.fittedvalues, copy=True)
        pred_ARIMA_diff_corrected = predictions_ARIMA_diff + features_train.shift(1)
        pred_ARIMA_diff_corrected = pred_ARIMA_diff_corrected[2:]
        pred_ARIMA_diff_corrected = pred_ARIMA_diff_corrected.shift(-2)
        pred_ARIMA_diff_corrected = pred_ARIMA_diff_corrected[:len(pred_ARIMA_diff_corrected)-2]
    if winner_index == 5:
        predictions_ARIMA_diff = pd.Series(results_ARIMA_diff.fittedvalues, copy=True)
        pred_ARIMA_diff_corrected = np.exp(predictions_ARIMA_diff)
        pred_ARIMA_diff_corrected = predictions_ARIMA_diff + features_train.shift(1)
        pred_ARIMA_diff_corrected = pred_ARIMA_diff_corrected[2:]
        pred_ARIMA_diff_corrected = pred_ARIMA_diff_corrected.shift(-1)
        pred_ARIMA_diff_corrected = pred_ARIMA_diff_corrected[:len(pred_ARIMA_diff_corrected)-1]
    '''
    plt.plot(features_train)
    plt.plot(pred_ARIMA_diff_corrected, color='red')
    '''
    '''
    plt.plot(pred_ARIMA_diff_corrected.head(100), color='red')
    plt.plot(features_train.head(100))
    '''
    '''
    plt.plot(pred_ARIMA_diff_corrected.tail(100), color='red')
    plt.plot(features_train.tail(100))
    '''
    '''
    print('Percentage of Errors')
    in_sample_error = np.sqrt((pred_ARIMA_diff_corrected-features_train)**2)
    in_sample_error_prom = error.mean()
    in_sample_accuracy = 100-error_prom
    plt.plot(in_sample_error)
    plt.title('Promedio Error: %.4f'% in_sample_error_prom + '; Precision: %.4f'% in_sample_accuracy)
    plt.show()
    '''
    if winner_index == 0:
        out_of_sample_predictions_ARIMA = results_ARIMA_diff.predict(start=features_train.tail(1).index[0], end = len(features_train)+len(features_test-2), dynamic=True)
    if winner_index == 1:
        out_of_sample_predictions_ARIMA = results_ARIMA_diff.predict(start=features_train.tail(1).index[0], end = len(features_train)+len(features_test-2), dynamic=True)
        out_of_sample_predictions_ARIMA = np.exp(out_of_sample_predictions_ARIMA)
    if winner_index == 2:
        out_of_sample_predictions_ARIMA = results_ARIMA_diff.predict(start=features_train.tail(1).index[0], end = len(features_train)+len(features_test-2), dynamic=True)
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA[2:len(out_of_sample_predictions_ARIMA)-2]
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA + features_train.tail(len(features_test)).values
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA.shift(-2)
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA[:len(out_of_sample_predictions_ARIMA)-2]
    if winner_index == 3:
        out_of_sample_predictions_ARIMA = results_ARIMA_diff.predict(start=features_train.tail(1).index[0], end = len(features_train)+len(features_test-2), dynamic=True)
        out_of_sample_predictions_ARIMA = np.exp(out_of_sample_predictions_ARIMA)
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA[2:len(out_of_sample_predictions_ARIMA)-2]
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA + features_train.tail(len(features_test)).values
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA.shift(-2)
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA[:len(out_of_sample_predictions_ARIMA)-2]
    if winner_index == 4:
        out_of_sample_predictions_ARIMA = results_ARIMA_diff.predict(start=features_train.tail(1).index[0], end = len(features_train)+len(features_test-2), dynamic=True)
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA[2:len(out_of_sample_predictions_ARIMA)-2]
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA + features_train.tail(len(features_test)).values
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA.shift(-5)
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA[:len(out_of_sample_predictions_ARIMA)-4]
        out_of_sample_predictions_ARIMA.index = features_test.head(len(out_of_sample_predictions_ARIMA)).index
    if winner_index == 5:
        out_of_sample_predictions_ARIMA = results_ARIMA_diff.predict(start=features_train.tail(1).index[0], end = len(features_train)+len(features_test-2), dynamic=True)
        out_of_sample_predictions_ARIMA = np.exp(out_of_sample_predictions_ARIMA)
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA[2:len(out_of_sample_predictions_ARIMA)-2]
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA + features_train.tail(len(features_test)).values
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA.shift(-4)
        out_of_sample_predictions_ARIMA = out_of_sample_predictions_ARIMA[:len(out_of_sample_predictions_ARIMA)-4]
    '''
    print('Out of sample prediction')
    plt.plot(features_test, color='green')
    plt.plot(out_of_sample_predictions_ARIMA, color='red')
    '''
    error = np.sqrt((out_of_sample_predictions_ARIMA-features_test)**2).head(len(out_of_sample_predictions_ARIMA))
    error_prom = error.mean()
    accuracy = 100-error_prom
    '''
    plt.plot(error)
    plt.title('Promedio Error: %.4f'% error_prom + '; Precision: %.4f'% accuracy)
    plt.show()
    '''
    '''
    print('Out of sample prediction First 50')
    plt.plot(features_test.head(50), color='green')
    plt.plot(out_of_sample_predictions_ARIMA.head(50), color='red')
    error_50 = np.sqrt((out_of_sample_predictions_ARIMA.head(50)-features_test.head(50))**2).head(len(out_of_sample_predictions_ARIMA.head(50)))
    error_prom_50 = error_50.mean()
    accuracy_50 = 100-error_prom_50
    plt.plot(error_50)
    plt.title('Promedio Error: %.4f'% error_prom_50 + '; Precision: %.4f'% accuracy_50)
    plt.show()
    '''
    data = []
    for i in range(0, len(error)):
        entry = ObjDict()
        entry.fecha = str(out_of_sample_predictions_ARIMA.index[i])
        entry.prediccion = out_of_sample_predictions_ARIMA[i]
        entry.error = error[i]
        data.append(entry)
    return json.dumps(data), error_prom, accuracy