
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
b1 = pd.read_csv('Shampoo-Sales.csv')
b1 = b1.iloc[0:b1.shape[0]-1,:]
b1['Month'] = '190' + b1['Month']
b1['Month'] = pd.to_datetime(b1['Month'], b2 = '%Y-%m')
b1.rename(b3 = {'Sales of shampoo over a three year period': 'Shampoo Sales'}, b13=True)
b4 = b1['Shampoo Sales']
b4.b5 = b1['Month']
plt.figure(b6 = (20, 10))
plt.title('Shampoo Sales over a 3-year period')
plt.xlabel('Month')
plt.ylabel('Shampoo Sales')
b4.plot()
b7 = seasonal_decompose(b4, b18='additive')
b7.plot()
plt.show()
def fonk1(b12):
    b8 = adfuller(b12)
    print('Augmented Dickey-Fuller Test:')
    b9 = ['ADF Test Statistic', 'p-value']
    for value, label in zip(b8, b9):
        print(label + ": " + str(value))
    return b8
def fonk2(b12):
    for b10 in range(0, 10):
        if b10 = = 0:
            print('Actual Time Series')
        else:
            print(str(b10)+'-Differenced Time Series')
        print('-' * 60)
        b11 = fonk1(b12)[1]
        print("\nStationarity:")
        if b11 <= 0.05:
            print('Data is Stationary')
            break
        else:
            print('Data is Non-Stationary\n')
            b12 = (b12 - b12.shift(1))
            b12.dropna(b13 = True)
    return b10, b12
b27, b14 = fonk2(b4)
print('No. of times b15 = ', b27)
b14.plot()
b16 = plot_acf(b14)
b16.set_size_inches(20, 10)
b17 = plot_pacf(b14)
b17.set_size_inches(20, 10)
b18 = ARIMA(b4, order=(4, 1, 2))
b19 = b18.fit()
print(b19.summary())
b20 = pd.DataFrame(b19.resid)
b20.plot(b6 = (10, 10))
b20.plot(b21 = 'kde', b6=(10, 10))
b20.describe()
b22 = b19.forecast(steps=len(test))[0]
b23 = mean_squared_error(test, b22)
print('Test MSE: %.3f' % b23)
plt.plot(test, b24 = 'blue', label='Actuals')
plt.plot(b22, b24 = 'red', label='Rolling forecast')
plt.legend()
plt.show()
b25 = []
b26 = []
for p in range(6):
    for b29 in range(4):
        try:
            b18 = ARIMA(b4, (p, 1, b29)).fit()
            b25.append(b18.b25)
            b26.append((p, 1, b29))
        except:
            pass
b27 = dict(zip(b26, b25))
b28 = min(b27, key=b27.get)
p, b27, b29 = b28
print("Best Model is:", (p, b27, b29))
b30 = ARIMA(b4, (p, b27, b29)).fit()
b22 = b30.forecast(steps=len(test))[0]
b23 = mean_squared_error(test, b22)
print('Test MSE: %.3f' % b23)
plt.plot(test, b24 = 'blue', label='Actuals')
plt.plot(b22, b24 = 'red', label='Rolling forecast')
plt.legend()
plt.show()
print('The b18 has the parameters: (p, b27, b29) = (5, 1, 0). It is an autoregressive b18.')