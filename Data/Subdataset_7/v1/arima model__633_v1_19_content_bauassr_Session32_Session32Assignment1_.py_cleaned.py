import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
b1 = pd.read_csv('Shampoo-Sales.csv')
b1 = b1.iloc[:-1]
b1['Month'] = '190' + b1['Month']
b1['Month'] = pd.to_datetime(b1['Month'], b2 = '%Y-%m')
b1.rename(b3 = {'Sales of shampoo over a three year period': 'Shampoo Sales'}, b17=True)
b4 = b1.set_index('Month')['Shampoo Sales']
plt.figure(b5 = (20, 10))
plt.b8('Shampoo Sales over a 3-year period')
plt.xlabel('Month')
plt.ylabel('Shampoo Sales')
b4.plot()
plt.show()
sales_cycle, b6 = sm.tsa.filters.hpfilter(b4)
b7 = pd.DataFrame({'Sales': b4.b43, 'Trend': b6, 'Cycle': sales_cycle}, index=b4.index)
b7.plot(b8 = 'Shampoo Sales, Sales Trend and Sales Cycle over a 3-year period', b5=(20, 10))
plt.show()
b9 = pd.DataFrame({'Actual Series': b4, 'EWMA Series': b4.ewm(span=3).mean()})
b9.plot(b5 = (20, 10))
plt.show()
plt.figure(b5 = (20, 10))
b4.rolling(3).mean().plot(b10 = '3 month rolling mean')
b4.rolling(3).std().plot(b10 = '3 month rolling standard deviation')
b4.plot(b10 = 'Actual data')
plt.legend()
plt.show()
b11 = sm.tsa.seasonal_decompose(b4, b20='additive')
b11.plot()
plt.gcf().set_size_inches(20, 10)
plt.show()
def fonk1(b16):
    b12 = sm.tsa.adfuller(b16)
    print('Augmented Dickey-Fuller Test:')
    b13 = ['ADF Test Statistic', 'a1-value']
    for value, b10 in zip(b12, b13):
        print(b10 + ": " + str(value))
fonk1(b4)
def fonk2(b16):
    for b14 in range(0, 10):
        if b14 = = 0:
            print('Actual Time Series')
        else:
            print(str(b14) + '-Differenced Time Series')
        print('-' * 60)
        b15 = fonk1(b16)[1]
        print("\nStationarity:")
        if b15 <= 0.05:
            print('Data is Stationary')
            break
        else:
            print('Data is Non-Stationary\n')
            b16 = (b16 - b16.shift(1))
            b16.dropna(b17 = True)
    return b14, b16
a3, b18 = fonk2(b4)
print('No.of times b19 = ', a3)
b18.plot()
plt.show()
sm.graphics.tsa.plot_acf(b18)
plt.show()
sm.graphics.tsa.plot_pacf(b18)
plt.show()
b20 = ARIMA(b4, order=(4, 1, 2))
b21 = b20.fit()
print(b21.summary())
b22 = pd.DataFrame(b21.resid)
b22.plot(b5 = (10, 10))
plt.show()
b22.plot(b23 = 'kde', b5=(10, 10))
plt.show()
print(b22.describe())
b24 = b21.plot_predict()
plt.show()
b25 = b4.b43
b26 = int(len(b25) * 0.66)
train, b27 = b25[0:b26], b25[b26:len(b25)]
b28 = [b40 for b40 in train]
b29 = list()
for t in range(len(b27)):
    b20 = ARIMA(b28, order=(4, 1, 2))
    b30 = b20.fit(disp=0)
    b31 = b30.forecast()
    b32 = b31[0]
    b29.append(b32)
    b33 = b27[t]
    b28.append(b33)
    print('b34 = %f, expected=%f' % (b32, b33))
b35 = mean_squared_error(b27, b29)
print('Test MSE: %.3f' % b35)
plt.plot(b27, b36 = 'blue', b10='Actuals')
plt.plot(b29, b36 = 'red', b10='Rolling forecast')
plt.legend()
plt.show()
b37 = b25
a1 = 0
a2 = 0
a3 = 1
b38 = []
b39 = []
for a1 in range(6):
    for a2 in range(4):
        try:
            b20 = ARIMA(b37, (a1, a3, a2)).fit()
            b40 = b20.b39
            b41 = (a1, a3, a2)
            print(b41, b40)
            b39.append(b40)
            b38.append(b41)
        except:
            pass
b42 = b38
b43 = b39
a3 = dict(zip(b42, b43))
b44 = min(a3, key=a3.get)
for b14 in range(3):
    a1 = b44[0]
    a3 = b44[1]
    a2 = b44[2]
print("Best Model is :", (a1, a3, a2))
b45 = ARIMA(b37, (a1, a3, a2)).fit()
b25 = b4.b43
b26 = int(len(b25) * 0.66)
train, b27 = b25[0:b26], b25[b26:len(b25)]
b28 = [b40 for b40 in train]
b29 = list()
for t in range(len(b27)):
    b20 = ARIMA(b28, order=(5, 1, 0))
    b30 = b20.fit(disp=-1)
    b31 = b30.forecast()
    b32 = b31[0]
    b29.append(b32)
    b33 = b27[t]
    b28.append(b33)
    print('b34 = %f, expected=%f' % (b32, b33))
b35 = mean_squared_error(b27, b29)
print('Test MSE: %.3f' % b35)
plt.plot(b27, b36 = 'blue', b10='Actuals')
plt.plot(b29, b36 = 'red', b10='Rolling forecast')
plt.legend()
plt.show()
print('The b20 has the parameters: (a1,a3,a2) = (5,1,0). It is an autoregressive b20')