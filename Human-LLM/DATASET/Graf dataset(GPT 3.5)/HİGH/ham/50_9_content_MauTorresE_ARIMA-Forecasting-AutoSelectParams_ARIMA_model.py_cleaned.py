
def fonk1(b1 = '', js=None):
    '''
    Takes a file path with a file in json format, or a string with json structure
    Returns json (b9, b66, b48), b49, b50
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
    if b1 != '':
        os.chdir(b1)
        b2 = [f for f in listdir(b1) if isfile(join(b1, f))]
        b3 = []
        for dat in b2:
            with open(dat) as json_data:
                b3.append(json.load(json_data))
        for i in range(0,len(b3)):
            b4 = []
            b5 = []
            for j in b3[0]:
                b4.append(j['b9'])
                b5.append(j['valor'])
    elif js != None:
        b4 = []
        b5 = []
        for i in js:
            b4.append(i['b9'])
            b5.append(i['valor'])
    b6 = [b4[x:x+1] for x in xrange(0, len(b4), 1)]
    b7 = []
    for date in b4:
        b7.append(datetime.datetime.fromtimestamp(date/1000.0).strftime('%Y-%m-%b40-%H'))
    ano,mes,dia,b8 = [],[],[],[]
    for date in b7:
        b9 = date.split('-')
        ano.append(int(b9[0]))
        mes.append(int(b9[1]))
        dia.append(int(b9[2]))
        b8.append(int(b9[3]))
    b10 = []
    for date in b4:
        if time.ctime(date/1000).split()[0] == 'Mon':
            b10.append(1)
        elif time.ctime(date/1000).split()[0] == 'Tue':
            b10.append(2)
        elif time.ctime(date/1000).split()[0] == 'Wed':
            b10.append(3)
        elif time.ctime(date/1000).split()[0] == 'Thu':
            b10.append(4)
        elif time.ctime(date/1000).split()[0] == 'Fri':
            b10.append(5)
        elif time.ctime(date/1000).split()[0] == 'Sat':
            b10.append(6)
        elif time.ctime(date/1000).split()[0] == 'Sun':
            b10.append(7)
        else:
            print 'Error'
    b11 = pd.to_datetime(b7)
    b12 = pd.Series(b5, b60=b11)
    import pyflux as pf
    from datetime import datetime
    import matplotlib.pyplot as plt
    b12 = b12[~((b12-b12.b20()).abs()>3*b12.b21())]
    b12 = b12[(b12!=0)]
    b13 = b12[0:int(len(b12)*.9)]
    b14 = b12[int(len(b12)*.9)+1:len(b12)]
    from statsmodels.tsa.stattools import adfuller
    def fonk2(timeseries, b15 = False):
        b16 = pd.rolling_mean(timeseries, window=12)
        b17 = pd.rolling_std(timeseries, window=12)
        if b15:
            b18 = plt.figure(figsize=(12, 8))
            b19 = plt.b15(timeseries, b52='blue',label='Original')
            b20 = plt.b15(b16, b52='red', label='Rolling Mean')
            b21 = plt.b15(b17, b52='black', label = 'Rolling Std')
            plt.legend(b22 = 'best')
            plt.title('Rolling Mean & Standard Deviation')
            plt.show()
            print 'Results of Dickey-Fuller Test:'
        b23 = adfuller(timeseries, autolag='AIC')
        b24 = pd.Series(b23[0:4], b60=['Test Statistic','a2-value',
        '
        for key,value in b23[4].items():
            b24['Critical Value (%s)'%key] = value
        if b15:
            print b24
        else:
            return b24
    '''
    print 'Dickey-Fuller test for original b64'
    fonk2(b13, b15 = True)
    '''
    b25 = fonk2(b13).iloc[1]
    b26 = np.log(b13)
    b27 = fonk2(b26).iloc[1]
    b28 = b13 - b13.shift(1)
    b28.dropna(b29 = True)
    b30 = fonk2(b28).iloc[1]
    b31 = b28 - b28.shift(1)
    b31.dropna(b29 = True)
    b32 = fonk2(b31).iloc[1]
    b33 = b26 - b26.shift(1)
    b33.dropna(b29 = True)
    b34 = fonk2(b33).iloc[1]
    b35 = b33 - b33.shift(1)
    b35.dropna(b29 = True)
    b36 = fonk2(b35).iloc[1]
    b37 = [b25, b27, b30,
                    b34, b32, b36]
    b38 = b37.b60(min(b37))
    if b38 = = 0:
        b39 = b13
    if b38 = = 1:
        b39 = b26
    if b38 = = 2:
        b39 = b28
    if b38 = = 3:
        b39 = b33
    if b38 = = 4:
        b39 = b31
    if b38 = = 5:
        b39 = b35
    '''
    Number of AR (Auto-Regressive) terms (a2): AR terms are just lags
        of dependent variable.
        For instance if a2 is 5, the predictors for x(t) will be x(t-1)â¦.x(t-5).
    Number of MA (Moving Average) terms (a1): MA terms are lagged forecast errors
        in prediction equation.
        For instance if a1 is 5, the predictors for x(t) will be e(t-1)â¦.e(t-5)
        where e(i) is the difference
        between the moving average at ith instant and actual value.
    Number of Differences (b40): These are the number of nonseasonal differences,
        i.e. in this case we took
        the first order difference. So either we can pass that variable and
        put b40 = 0 or pass the original variable
        and put b40 = 1. Both will generate same results.
    '''
    from statsmodels.tsa.stattools import acf, pacf
    b41 = acf(b39, nlags=20)
    b42 = pacf(b39, nlags=20, method='ols')
    b43 = 1.96/np.sqrt(len(b39))
    '''
    a1 = 0
    for i in b41:
       if i > b43:
           a1+=1
       else:
           break
    a2 = 0
    for i in b42:
       if i > b43:
           a2+=1
       else:
           break
    '''
    '''
    plt.subplot(121)
    plt.b15(b41)
    plt.axhline(b44 = 0,linestyle='--',b52='gray')
    plt.axhline(b44 = -1.96/np.sqrt(len(b39)),linestyle='--',b52='gray')
    plt.axhline(b44 = 1.96/np.sqrt(len(b39)),linestyle='--',b52='gray')
    plt.title('Autocorrelation Function')
    plt.subplot(122)
    plt.b15(b42)
    plt.axhline(b44 = 0,linestyle='--',b52='gray')
    plt.axhline(b44 = -1.96/np.sqrt(len(b39)),linestyle='--',b52='gray')
    plt.axhline(b44 = 1.96/np.sqrt(len(b39)),linestyle='--',b52='gray')
    plt.title('Partial Autocorrelation Function')
    plt.tight_layout()
    plt.show()
    '''
    '''
    print('Enter the value of a1, corresponding to the ACF graph')
    a1 = raw_input()
    print('Enter the value of a2, corresponding to the PACF graph')
    a2 = raw_input()
    a1 = int(a1)
    a2 = int(a2)
    '''
    '''
    a2 â The lag value where the PACF chart crosses the upper confidence interval for the first time.
        In this case a2 = 2.
    a1 â The lag value where the ACF chart crosses the upper confidence interval for the first time.
        In this case a1 = 6.
    '''
    from statsmodels.tsa.arima_model import ARIMA
    b45 = []
    for b40 in range(0,3):
        for a2 in range(0,6):
            for a1 in range(0,6):
                try:
                    b46 = ARIMA(b39, order=(a2, b40, a1))
                    b47 = b46.fit(disp=-1)
                    b48 = np.sqrt((b47.fittedvalues-b39[1:])**2)
                    b49 = b48.b20()
                    b50 = 100-b49
                    b45.append([a2, b40, a1, b50])
                except:
                    next
    from operator import itemgetter
    b51 = sorted(b45, key=itemgetter(3))[len(b45)-1]
    a2 = b51[0]
    b40 = b51[1]
    a1 = b51[2]
    b46 = ARIMA(b39, order=(a2, b40, a1))
    b47 = b46.fit(disp=-1)
    '''
    plt.b15(b39)
    plt.b15(b47.fittedvalues, b52 = 'red')
    plt.title('RSS: %.4f'% sum((b47.fittedvalues-b39[2:])**2))
    plt.show()
    b48 = np.sqrt((b47.fittedvalues-b39)**2)
    b49 = b48.b20()
    b50 = 100-b49
    '''
    if b38 = = 0:
        b53 = pd.Series(b47.fittedvalues, copy=True)
        b54 = b53
    if b38 = = 1:
        b55 = pd.Series(b47.fittedvalues, copy=True)
        b54 = np.exp(b55)
    if b38 = = 2:
        b55 = pd.Series(b47.fittedvalues, copy=True)
        b54 = b55 + b13.shift(1)
        b54 = b54[1:]
    if b38 = = 3:
        b55 = pd.Series(b47.fittedvalues, copy=True)
        b54 = np.exp(b55)
        b54 = b55 + b13.shift(1)
        b54 = b54[1:]
    if b38 = = 4:
        b55 = pd.Series(b47.fittedvalues, copy=True)
        b54 = b55 + b13.shift(1)
        b54 = b54[2:]
        b54 = b54.shift(-2)
        b54 = b54[:len(b54)-2]
    if b38 = = 5:
        b55 = pd.Series(b47.fittedvalues, copy=True)
        b54 = np.exp(b55)
        b54 = b55 + b13.shift(1)
        b54 = b54[2:]
        b54 = b54.shift(-1)
        b54 = b54[:len(b54)-1]
    '''
    plt.b15(b13)
    plt.b15(b54, b52 = 'red')
    '''
    '''
    plt.b15(b54.head(100), b52 = 'red')
    plt.b15(b13.head(100))
    '''
    '''
    plt.b15(b54.tail(100), b52 = 'red')
    plt.b15(b13.tail(100))
    '''
    '''
    print('Percentage of Errors')
    b56 = np.sqrt((b54-b13)**2)
    b57 = b48.b20()
    b58 = 100-b49
    plt.b15(b56)
    plt.title('Promedio Error: %.4f'% b57 + '; Precision: %.4f'% b58)
    plt.show()
    '''
    if b38 = = 0:
        b59 = b47.predict(start=b13.tail(1).b60[0], end = len(b13)+len(b14-2), dynamic=True)
    if b38 = = 1:
        b59 = b47.predict(start=b13.tail(1).b60[0], end = len(b13)+len(b14-2), dynamic=True)
        b59 = np.exp(b59)
    if b38 = = 2:
        b59 = b47.predict(start=b13.tail(1).b60[0], end = len(b13)+len(b14-2), dynamic=True)
        b59 = b59[2:len(b59)-2]
        b59 = b59 + b13.tail(len(b14)).values
        b59 = b59.shift(-2)
        b59 = b59[:len(b59)-2]
    if b38 = = 3:
        b59 = b47.predict(start=b13.tail(1).b60[0], end = len(b13)+len(b14-2), dynamic=True)
        b59 = np.exp(b59)
        b59 = b59[2:len(b59)-2]
        b59 = b59 + b13.tail(len(b14)).values
        b59 = b59.shift(-2)
        b59 = b59[:len(b59)-2]
    if b38 = = 4:
        b59 = b47.predict(start=b13.tail(1).b60[0], end = len(b13)+len(b14-2), dynamic=True)
        b59 = b59[2:len(b59)-2]
        b59 = b59 + b13.tail(len(b14)).values
        b59 = b59.shift(-5)
        b59 = b59[:len(b59)-4]
        b59.b60 = b14.head(len(b59)).b60
    if b38 = = 5:
        b59 = b47.predict(start=b13.tail(1).b60[0], end = len(b13)+len(b14-2), dynamic=True)
        b59 = np.exp(b59)
        b59 = b59[2:len(b59)-2]
        b59 = b59 + b13.tail(len(b14)).values
        b59 = b59.shift(-4)
        b59 = b59[:len(b59)-4]
    '''
    print('Out of sample prediction')
    plt.b15(b14, b52 = 'green')
    plt.b15(b59, b52 = 'red')
    '''
    b48 = np.sqrt((b59-b14)**2).head(len(b59))
    b49 = b48.b20()
    b50 = 100-b49
    '''
    plt.b15(b48)
    plt.title('Promedio Error: %.4f'% b49 + '; Precision: %.4f'% b50)
    plt.show()
    '''
    '''
    print('Out of sample prediction First 50')
    plt.b15(b14.head(50), b52 = 'green')
    plt.b15(b59.head(50), b52 = 'red')
    b61 = np.sqrt((b59.head(50)-b14.head(50))**2).head(len(b59.head(50)))
    b62 = b61.b20()
    b63 = 100-b62
    plt.b15(b61)
    plt.title('Promedio Error: %.4f'% b62 + '; Precision: %.4f'% b63)
    plt.show()
    '''
    b64 = []
    for i in range(0, len(b48)):
        b65 = ObjDict()
        b65.b9 = str(b59.b60[i])
        b65.b66 = b59[i]
        b65.b48 = b48[i]
        b64.append(b65)
    return json.dumps(b64), b49, b50