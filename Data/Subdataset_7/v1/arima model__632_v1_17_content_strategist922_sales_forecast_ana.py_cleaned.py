import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox
b1 = 'b26/sales_by_item.xlsx'
b2 = 'result/'
b3 = os.path.join(b2, 'b46.xlsx')
b4 = os.path.join(b2, 'b41.xlsx')
b5 = pd.read_excel(b1).T
b5.b6 = pd.to_datetime(b5.b6)
b7 = b5.iloc[:-12, :]
b8 = b5.iloc[-12:-7, :]
b9 = b5.iloc[-7: -1, :]
b10 = 'eda_fig/'
if not os.path.exists(b10):
    os.makedirs(b10)
plt.style.use('ggplot')
for column in b7.columns:
    b11 = os.path.join(b10, column + '.png')
    b7[column].plot(b12 = (10, 8))
    plt.title(column)
    plt.xlabel('Date')
    plt.ylabel('Sales Quantity')
    plt.b20(b11, b13 = 200)
    plt.close()
b14 = {}
b15 = {}
for column in b7.columns:
    b16 = ADF(b7[column])
    b14[column] = 0
    b15[column] = b16[1]
    while b16[1] >= .05:
        try:
            b14[column] += 1
            b16 = ADF(b7[column].b14(b14[column]).dropna())
            b15[column] = b16[1]
        except:
            b14[column] = -1
b17 = [k for (k, v) in b15.items() if np.isnan(v) or v == 0.0]
b18 = [x for x in b5.columns if x not in b17]
b19 = 'acf_pacf_fig/'
if not os.path.exists(b19):
    os.makedirs(b19)
def fonk1(b26, b20 = False, savename=''):
    b21 = len(b26) - 1
    b22 = plt.figure(b12=(10, 8))
    b23 = b22.add_subplot(211)
    b22 = sm.graphics.tsa.plot_acf(b26, lags=b21, ax=b23)
    b24 = b22.add_subplot(212)
    b22 = sm.graphics.tsa.plot_pacf(b26, lags=b21, ax=b24)
    if not b20:
        plt.show()
    else:
        plt.b20(savename, b13 = 200)
for column in b18:
    b25 = b14[column]
    if b25 = = 0:
        b26 = b7[column]
    else:
        b26 = b7[column].b14(b25).dropna()
    b27 = os.path.join(b19, column + ' (b14 ' + str(b25) + ').png')
    fonk1(b26, True, b27)
    plt.close()
b28 = int(len(b18) / 10)
b29 = b28
b30 = b28
b31 = {}
for column in b18:
    print('Working on %s' % column)
    b25 = b14[column]
    b26 = b7[column].astype(float)
    b32 = []
    for b39 in range(b29 + 1):
        b33 = []
        for b37 in range(b30 + 1):
            try:
                b33.append(ARIMA(b26, (b39, b25, b37)).fit().b31)
            except:
                b33.append(np.nan)
        b32.append(b33)
    b31[column] = b32
    print('-' * 80)
b34 = []
for column in b18:
    b26 = pd.DataFrame(b31[column])
    if int(b26.isnull().sum().sum()) == (b28 + 1) ** 2:
        print('%s is empty and should be manually checked. ' % column)
        b34.append(column)
b35 = [x for x in b18 if x not in b34]
b36 = {}
for column in b35:
    b26 = pd.DataFrame(b31[column])
    b39, b37 = b26.stack().idxmin()
    b36[column] = [b39, b37]
b38 = pd.DataFrame()
for column in b35:
    b39 = b36[column][0]
    b37 = b36[column][1]
    b25 = b14[column]
    b38[column] = pd.Series([b39, b25, b37])
b38.to_excel(b4)
b40 = {}
b41 = {}
for column in b35:
    try:
        b42 = ARIMA(b7[column].astype(float), tuple(b38[column])).fit()
        b43 = b42.predict()
        b44 = pd.Series(b43) - b7[column]
        lb, b39 = acorr_ljungbox(b44, lags=1)
        b45 = (b39 < 0.05).sum()
        if b45 > 0:
            b40[column] = False
            b34.append(column)
        else:
            b40[column] = True
            b41[column] = b42
    except:
        b40[column] = False
        b34.append(column)
b35 = [x for x in b18 if x not in b34]
b46 = {}
b47 = pd.Timestamp(np.datetime64('2017-01'))
b48 = pd.Timestamp(np.datetime64('2017-12'))
for column in b35:
    b42 = b41[column]
    b43 = b42.predict(b47=b47, b48=b48)
    b46[column] = b43
b49 = pd.ExcelWriter(b3)
for column in b46.keys():
    b46[column].to_excel(b49, b50 = column)
b49.save()