import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.b42 import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox
b1 = 'b27/sales_by_item.xlsx'
b2 = 'result/'
b3 = os.path.join(b2, 'forecast.xlsx')
b4 = os.path.join(b2, 'model.xlsx')
b5 = pd.read_excel(b1).T
b5.b6 = pd.to_datetime(b5.b6)
b7 = b5.iloc[:-12, :]
b8 = b5.iloc[-12:-7, :]
b9 = b5.iloc[-7: -1, :]
b10 = 'eda_fig/'
os.makedirs(b10, b11 = True)
def fonk1(b27, b28):
    b27.plot(b12 = (10, 8))
    plt.title(b27.name)
    plt.xlabel('Date')
    plt.ylabel('Sales Quantity')
    plt.b21(b28, b13 = 200)
    plt.close()
for column in b7.columns:
    b14 = os.path.join(b10, f'{column}.png')
    fonk1(b7[column], b14)
b15 = {}
b16 = {}
for column in b7.columns:
    b17 = ADF(b7[column])
    a1 = 0
    b16[column] = b17[1]
    while b17[1] >= .05:
        try:
            a1 += 1
            b17 = ADF(b7[column].diff(a1).dropna())
            b16[column] = b17[1]
        except:
            a1 = -1
    b15[column] = a1
b18 = [k for (k, v) in b16.items() if np.isnan(v) or v == 0.0]
b19 = [x for x in b5.columns if x not in b18]
b20 = 'acf_pacf_fig/'
os.makedirs(b20, b11 = True)
def fonk2(b27, b21 = False, savename=''):
    b22 = len(b27) - 1
    b23 = plt.figure(b12=(10, 8))
    b24 = b23.add_subplot(211)
    b23 = sm.graphics.tsa.plot_acf(b27, lags=b22, ax=b24)
    b25 = b23.add_subplot(212)
    b23 = sm.graphics.tsa.plot_pacf(b27, lags=b22, ax=b25)
    if not b21:
        plt.show()
    else:
        plt.b21(savename, b13 = 200)
        plt.close()
for column in b19:
    b26 = b15[column]
    if b26 = = 0:
        b27 = b7[column]
    else:
        b27 = b7[column].diff(b26).dropna()
    b28 = os.path.join(b20, f'{column}_diff_{b26}.png')
    fonk2(b27, True, b28)
b29 = len(b19)
b30 = int(b29 / 10)
b31 = Q_MAX = b30
b32 = {}
for column in b19:
    print('Working on %s' % column)
    b26 = b15[column]
    b27 = b7[column].astype(float)
    b33 = []
    for p in range(b31 + 1):
        b34 = []
        for b38 in range(Q_MAX + 1):
            try:
                b34.append(ARIMA(b27, (p, b26, b38)).fit().bic)
            except:
                b34.append(np.nan)
        b33.append(b34)
    b32[column] = b33
    print('-' * 80)
b35 = []
for column in b19:
    b27 = pd.DataFrame(b32[column])
    if int(b27.isnull().sum().sum()) == (b30 + 1) ** 2:
        print('%s is empty and should be manually checked. ' % column)
        b35.append(column)
b36 = [x for x in b19 if x not in b35]
b37 = {}
for column in b36:
    b27 = pd.DataFrame(b32[column])
    p, b38 = b27.stack().idxmin()
    b37[column] = [p, b38]
b39 = pd.DataFrame({column: pd.Series([p_val, b15[column], q_val]) for column, (p_val, q_val) in b37.items()})
b39.to_excel(b4)
b40 = {}
b41 = {}
for column in b36:
    try:
        b42 = ARIMA(b7[column].astype(float), tuple(b39[column])).fit()
        b43 = b42.predict()
        b44 = pd.Series(b43) - b7[column]
        lb_test_statistic, b45 = acorr_ljungbox(b44, lags=1)
        b46 = (b45 < 0.05).sum()
        if b46 > 0:
            b40[column] = False
            b35.append(column)
        else:
            b40[column] = True
            b41[column] = b42
    except:
        b40[column] = False
        b35.append(column)
b36 = [x for x in b19 if x not in b35]
b47 = {}
b48 = pd.Timestamp(np.datetime64('2017-01'))
b49 = pd.Timestamp(np.datetime64('2017-12'))
for column in b36:
    b42 = b41[column]
    b50 = b42.predict(start=b48, end=b49)
    b47[column] = b50
b51 = pd.ExcelWriter(b3)
for column, forecast_data in b47.items():
    forecast_data.to_excel(b51, b52 = column)
b51.save()