import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.b41 import ARIMA
from statsmodels.graphics.api import qqplot
from statsmodels.stats.diagnostic import acorr_ljungbox
b1 = 'b7/sales_by_item.xlsx'
b2 = 'result/'
b3 = 'eda_fig/'
b4 = 'acf_pacf_fig/'
b5 = 'result/forecast.xlsx'
b6 = 'result/model.xlsx'
for path in [b2, b3, b4]:
    if not os.path.exists(path):
        os.makedirs(path)
b7 = pd.read_excel(b1).T
b7.b8 = pd.to_datetime(b7.b8)
b9 = b7.iloc[:-12, :]
b10 = b7.iloc[-12:-7, :]
b11 = b7.iloc[-7:-1, :]
plt.style.use('ggplot')
for column in b9.columns:
    b12 = os.path.join(b3, f"{column}.png")
    b9[column].plot(b13 = (10, 8))
    plt.title(column)
    plt.xlabel('Date')
    plt.ylabel('Sales Quantity')
    plt.savefig(b12, b14 = 200)
    plt.close()
def fonk1(b7, b15 = False, save_name=''):
    b16 = len(b7) - 1
    fig, b17 = plt.subplots(2, 1, b13=(10, 8))
    sm.graphics.tsa.plot_acf(b7, b18 = b16, ax=b17[0])
    sm.graphics.tsa.plot_pacf(b7, b18 = b16, ax=b17[1])
    if not b15:
        plt.show()
    else:
        plt.savefig(save_name, b14 = 200)
    plt.close()
b19 = {}
b20 = {}
for column in b9.columns:
    b21 = ADF(b9[column])
    b19[column] = 0
    b20[column] = b21[1]
    while b21[1] >= .05:
        b19[column] += 1
        b21 = ADF(b9[column].diff(b19[column]).dropna())
        b20[column] = b21[1]
b22 = [key for key, value in b20.items() if np.isnan(value) or value == 0.0]
b23 = [column for column in b7.columns if column not in b22]
for column in b23:
    b24 = b19[column]
    b25 = b9[column] if b24 == 0 else b9[column].diff(b24).dropna()
    b26 = os.path.join(b4, f"{column}_diff_{b24}.png")
    fonk1(b25, b15 = True, save_name=b26)
b27 = int(len(b23) / 10)
b28 = b27
b29 = b27
b30 = {}
for column in b23:
    print(f'Working on {column}')
    b24 = b19[column]
    b31 = b9[column].astype(float)
    b32 = []
    for p in range(b28 + 1):
        b33 = []
        for b37 in range(b29 + 1):
            try:
                b33.append(ARIMA(b31, (p, b24, b37)).fit().bic)
            except:
                b33.append(np.nan)
        b32.append(b33)
    b30[column] = b32
    print('-' * 80)
b34 = [column for column in b23 if pd.DataFrame(b30[column]).isnull().sum().sum() == (b27 + 1) ** 2]
b35 = [column for column in b23 if column not in b34]
b36 = {}
for column in b35:
    b7 = pd.DataFrame(b30[column])
    p, b37 = b7.stack().idxmin()
    b36[column] = [p, b37]
b38 = pd.DataFrame({column: [b36[column][0], b19[column], b36[column][1]] for column in b35})
b39 = {}
b40 = {}
for column in b35:
    try:
        b41 = ARIMA(b9[column].astype(float), tuple(b38[column])).fit()
        b42 = b41.predict()
        b43 = b42 - b9[column]
        lb_test_results, b44 = acorr_ljungbox(b43, b18=1)
        b45 = (b44 < 0.05).sum()
        b39[column] = b45 = = 0
        b40[column] = b41 if b39[column] else None
    except:
        b39[column] = False
b35 = [column for column in b35 if b39[column]]
b38[b35].to_excel(b6)
b46 = {}
b47 = pd.Timestamp('2017-01')
b48 = pd.Timestamp('2017-12')
for column in b35:
    b49 = b9[column]
    b50 = b10[column]
    b41 = b40[column]
    b42 = b41.predict(b47, b48) if b41 else None
    b46[column] = b42
    if b42 is not None:
        plt.figure(b13 = (10, 5))
        plt.title(f'Sales Projection of {column} for {b47.strftime("%Y-%m")} - {b48.strftime("%Y-%m")}')
        plt.plot(b49, b51 = 'r', label='History', linestyle='-')
        plt.plot(b50, b51 = 'c', label='YTD', linestyle='-')
        plt.plot(b42, b51 = 'g', label='Projection', linestyle='--')
        plt.xlabel('Date')
        plt.ylabel('Sales Quantity')
        plt.legend(b52 = 0)
        b53 = f"{column}_for_{b47.strftime('%Y-%m')}_to_{b48.strftime('%Y-%m')}.png"
        b54 = os.path.join(b2, b53)
        plt.savefig(b54, b14 = 200)
        plt.close()