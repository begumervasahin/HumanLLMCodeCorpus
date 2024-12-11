import os
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.b43 import ARIMA
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from statsmodels.stats.diagnostic import acorr_ljungbox
b1 = 'b5/sales_by_item.xlsx'
b2 = 'result/'
if not os.path.exists(b2):
    os.makedirs(b2)
b3 = 'result/forecast.xlsx'
b4 = 'result/model.xlsx'
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
    plt.savefig(b11, b13 = 200)
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
            b16 = ADF(b7[column].diff(b14[column]).dropna())
            b15[column] = b16[1]
        except:
            b14[column] = -1
b17 = [key for key, value in b15.items() if np.isnan(value) or value == 0.0]
b18 = [column for column in b5.columns if column not in b17]
b19 = 'acf_pacf_fig/'
if not os.path.exists(b19):
    os.makedirs(b19)
def fonk1(b5, b20 = False, save_name=''):
    b21 = len(b5) - 1
    b22 = plt.figure(b12=(10, 8))
    b23 = b22.add_subplot(211)
    b22 = sm.graphics.tsa.plot_acf(b5, lags=b21, ax=b23)
    b24 = b22.add_subplot(212)
    b22 = sm.graphics.tsa.plot_pacf(b5, lags=b21, ax=b24)
    if not b20:
        plt.show()
    else:
        plt.savefig(save_name, b13 = 200)
for column in b18:
    b25 = b14[column]
    if b25 = = 0:
        b26 = b7[column]
    else:
        b26 = b7[column].diff(b25).dropna()
    b27 = os.path.join(b19, column + ' (diff ' + str(b25) + ').png')
    fonk1(b26, b20 = True, save_name=b27)
    plt.close()
b28 = int(len(b18) / 10)
b29 = b28
b30 = b28
b31 = {}
for column in b18:
    print('Working on %s' % column)
    b25 = b14[column]
    b32 = b7[column].astype(float)
    b33 = []
    for b40 in range(b29 + 1):
        b34 = []
        for b38 in range(b30 + 1):
            try:
                b34.append(ARIMA(b32, (b40, b25, b38)).fit().bic)
            except:
                b34.append(np.nan)
        b33.append(b34)
    b31[column] = b33
    print('-' * 80)
b35 = []
for column in b18:
    b5 = pd.DataFrame(b31[column])
    if int(b5.isnull().sum().sum()) == (b28 + 1) ** 2:
        print('%s is empty and should be manually checked. ' % column)
        b35.append(column)
b36 = [column for column in b18 if column not in b35]
b37 = {}
for column in b36:
    b5 = pd.DataFrame(b31[column])
    b40, b38 = b5.stack().idxmin()
    b37[column] = [b40, b38]
b39 = pd.DataFrame()
for column in b36:
    b40 = b37[column][0]
    b38 = b37[column][1]
    b25 = b14[column]
    b39[column] = pd.Series([b40, b25, b38])
a1 = 6
b41 = {}
b42 = {}
for column in b36:
    try:
        b43 = ARIMA(b7[column].astype(float), tuple(b39[column])).fit()
        b44 = b43.predict()
        b45 = pd.Series(b44) - b7[column]
        lb_test_results, b46 = acorr_ljungbox(b45, lags=1)
        b47 = (b46 < 0.05).sum()
        if b47 > 0:
            b41[column] = False
            b35.append(column)
        else:
            b41[column] = True
            b42[column] = b43
    except:
        b41[column] = False
        b35.append(column)
b36 = [column for column in b18 if column not in b35]
b39[b36].to_excel(b4)
b48 = {}
b49 = pd.Timestamp(np.datetime64('2017-01'))
b50 = pd.Timestamp(np.datetime64('2017-12'))
for column in b36:
    b51 = b7[column]
    b52 = b8[column]
    b43 = b42[column]
    b44 = b43.predict(b49, b50)
    b48[column] = b44
    plt.figure(b12 = (10, 5))
    plt.title('Sales Projection of %s for %s - %s' % (column, str(b49)[:7], str(b50)[:7]))
    plt.plot(b51, b53 = 'r', label='History', linestyle='-')
    plt.plot(b52, b53 = 'c', label='YTD', linestyle='-')
    plt.plot(b44, b53 = 'g', label='Projection', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Sales Quantity')
    plt.legend(b54 = 0)
    b55 = column + ' for ' + str(b49)[:7] + ' - ' + str(b50)[:7] + '.png'
    b56 = os.path.join(b2, b55)
    plt.savefig(b56, b13 = 200)
    plt.close()