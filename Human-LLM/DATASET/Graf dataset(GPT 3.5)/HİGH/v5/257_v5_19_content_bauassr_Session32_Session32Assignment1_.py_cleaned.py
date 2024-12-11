import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.b17 import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error
b1 = pd.read_csv('Shampoo-Sales.csv')
b1 = b1.iloc[:-1, :]
b1['Month'] = '190' + b1['Month']
b1['Month'] = pd.to_datetime(b1['Month'], b2 = '%Y-%m')
b1.rename(b3 = {'Sales of shampoo over a three year period': 'Shampoo Sales'}, b12=True)
b4 = b1.set_index('Month')['Shampoo Sales']
plt.figure(b5 = (20, 10))
plt.title('Shampoo Sales over a 3-year period')
plt.xlabel('Month')
plt.ylabel('Shampoo Sales')
b4.plot()
b6 = seasonal_decompose(b4, b17='additive')
b6.plot()
plt.show()
def fonk1(b11):
    b7 = adfuller(b11)
    print('Augmented Dickey-Fuller Test:')
    b8 = ['ADF Test Statistic', 'p-value']
    for value, label in zip(b7, b8):
        print(label + ": " + str(value))
    return b7
def fonk2(b11):
    for b9 in range(10):
        if b9 = = 0:
            print('Actual Time Series')
        else:
            print(str(b9)+'-Differenced Time Series')
        print('-' * 60)
        b10 = fonk1(b11)[1]
        print("\nStationarity:")
        if b10 <= 0.05:
            print('Data is Stationary')
            break
        else:
            print('Data is Non-Stationary\n')
            b11 = (b11 - b11.shift(1))
            b11.dropna(b12 = True)
    return b9, b11
b26, b13 = fonk2(b4)
print('No. of times b14 = ', b26)
b13.plot()
b15 = plot_acf(b13)
b15.set_size_inches(20, 10)
b16 = plot_pacf(b13)
b16.set_size_inches(20, 10)
b17 = ARIMA(b4, order=(4, 1, 2))
b18 = b17.fit()
print(b18.summary())
b19 = pd.DataFrame(b18.resid)
b19.plot(b5 = (10, 10))
b19.plot(b20 = 'kde', b5=(10, 10))
b19.describe()
b21 = b18.forecast(steps=len(b4))[0]
b22 = mean_squared_error(b4, b21)
print('Test MSE: %.3f' % b22)
plt.plot(b4, b23 = 'blue', label='Actuals')
plt.plot(b21, b23 = 'red', label='Rolling forecast')
plt.legend()
plt.show()
b24 = []
b25 = []
for p in range(6):
    for b28 in range(4):
        try:
            b17 = ARIMA(b4, (p, 1, b28)).fit()
            b24.append(b17.b24)
            b25.append((p, 1, b28))
        except:
            pass
b26 = dict(zip(b25, b24))
b27 = min(b26, key=b26.get)
p, b26, b28 = b27
print("Best Model is:", (p, b26, b28))
b29 = ARIMA(b4, (p, b26, b28)).fit()
b21 = b29.forecast(steps=len(b4))[0]
b22 = mean_squared_error(b4, b21)
print('Test MSE: %.3f' % b22)
plt.plot(b4, b23 = 'blue', label='Actuals')
plt.plot(b21, b23 = 'red', label='Rolling forecast')
plt.legend()
plt.show()
print('The b17 has the parameters: (p, b26, b28) = (5, 1, 0). It is an autoregressive b17.')