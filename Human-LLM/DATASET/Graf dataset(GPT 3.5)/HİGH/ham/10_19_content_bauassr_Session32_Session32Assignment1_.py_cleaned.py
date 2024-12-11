import numpy as np
import pandas as pd
from pandas import read_csv
from pandas import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
get_ipython().run_line_magic('matplotlib', 'inline')
b1 = pd.read_csv('Shampoo-Sales.csv')
b1.head()
b1.tail()
b1 = b1.iloc[0:b1.shape[0]-1,:]
b1.tail()
b1['b2'] = '190' + b1['b2']
b1.head()
b1.b2 = pd.to_datetime(b1.b2,format ='%Y-%m')
b1.head()
b1.rename(b3 = {'Sales of shampoo over a three year period': 'Shampoo Sales'},axis =1,b21 = True)
b1.head()
b4 = b1['Shampoo Sales']
b4.head()
b4.b5 = b1.b2
b4.head()
b4.describe(b6 = 'all')
b4.b5
plt.figure(b7 = (20,10))
plt.b10('Shampoo Sales over a 3-year period')
plt.xlabel('b2')
plt.ylabel('Shampoo Sales')
b4.plot()
sales_cycle, b8 = sm.tsa.filters.hpfilter(b4)
sales_cycle.head()
b8.head()
b9 = pd.DataFrame(data = b4.b49, b5 = b4.b5,columns = ['Sales'])
b9.head()
b9['Trend'] = b8
b9['Cycle'] = sales_cycle
b9.head()
b9.plot(b10 = 'Shampoo Sales, Sales Trend and Sales Cycle over a 3-year period',b7 = (20,10))
b4.b5 = pd.to_datetime(b4.b5)
b11 = pd.DataFrame({'Actual Series':b4, 'EWMA Series':b4.ewm(span = 3).mean()})
b11.plot(b7 = (20,10))
b4.rolling(3).mean().plot(b12 = '3 month rolling mean', b7 = (20,10))
b4.rolling(3).std().plot(b12 = '3 month rolling standard deviation', b7 = (20,10))
b4.plot(b12 = 'Actual data')
plt.legend()
from statsmodels.tsa.seasonal import seasonal_decompose
b13 = seasonal_decompose(b4, b26 = 'additive')
b14 = b13.plot()
b14.set_size_inches(20,10)
b15 = pd.DataFrame({'Trend': b13.trend, 'Seasonality': b13.seasonal,
                              'Residual': b13.resid,'Observed':b13.observed})
b15.plot(b7 = (20,10))
from statsmodels.tsa.stattools import adfuller
def fonk1(b20):
    b16 = adfuller(b20)
    print('Augmented Dickey-Fuller Test:')
    b17 = ['ADF Test Statistic','a1-value','
    for value,b12 in zip(b16, b17):
        print(b12 + ": " + str(value))
    return b16
def fonk2(b20):
    for b18 in range(0,10):
        if(b18 = =0):
            print('Actual Time Series')
        else:
            print(str(b18)+'-Differenced Time Series')
        print('-' * 60)
        b19 = fonk1(b20)[1]
        print("\nStationarity:")
        if(b19 <= 0.05):
            print('Data is Stationary')
            break
        else:
            print('Data is Non-Stationary\n')
            b20 = (b20 - b20.shift(1))
            b20.dropna(b21 = True)
    return b18, b20
a3,b22 = fonk2(b4)
print('No.of times b23 = ', a3)
b22.plot()
sm.stats.durbin_watson(b4)
sm.stats.durbin_watson(b22)
from pandas.tools.plotting import autocorrelation_plot
autocorrelation_plot(b4)
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
b24 = plot_acf(b22)
b24.set_size_inches(20,10)
b25 = plot_pacf(b22)
b25.set_size_inches(20,10)
from statsmodels.tsa.arima_model import ARIMA
b26 = ARIMA(b4,order =(4,1,2))
b27 = b26.fit()
print(b27.summary())
b28 = pd.DataFrame(b27.resid)
b28.plot(b7 = (10,10))
b28.plot(b29 = 'kde',b7=(10,10) )
b28.describe()
b27.b45
b30 = b27.plot_predict()
from sklearn.metrics import mean_squared_error
b31 = b4.b49
b32 = int(len(b31) * 0.66)
train, b33 = b31[0:b32], b31[b32:len(b31)]
b34 = [b46 for b46 in train]
b35 = list()
for t in range(len(b33)):
    b26 = ARIMA(train, order=(4,1,2))
    b36 = b26.fit(disp=0)
    b37 = b36.forecast()
    b38 = b37[0]
    b35.append(b38)
    b39 = b33[t]
    b34.append(b39)
    print('b40 = %f, expected=%f' % (b38, b39))
b41 = mean_squared_error(b33, b35)
print('Test MSE: %.3f' % b41)
print ("Model b45 score",b36.b45, "\nModel bic score", b36.bic)
plt.plot(b33,b42 = 'blue', b12='Actuals')
plt.plot(b35, b42 = 'red', b12='Rolling forecast' )
plt.legend()
plt.show()
b43 = b31
a1 = 0
a2 = 0
a3 = 1
b44 = []
b45 = []
for a1 in range(6):
    for a2 in range(4):
            try:
                b26 = ARIMA(b43, (a1,a3,a2)).fit()
                b46 = b26.b45
                b47 = (a1,a3,a2)
                print (b47, b46)
                b45.append(b46)
                b44.append(b47)
            except:
                pass
b48 = b44
b49 = b45
a3 = dict(zip(b48, b49))
b50 = min(a3, key=a3.get)
for b18 in range(3):
    a1 = b50[0]
    a3 = b50[1]
    a2 = b50[2]
print ("Best Model is :", (a1,a3,a2))
b51 = ARIMA(b43, (a1,a3,a2)).fit()
b31 = b4.b49
b32 = int(len(b31) * 0.66)
train, b33 = b31[0:b32], b31[b32:len(b31)]
b34 = [b46 for b46 in train]
b35 = list()
for t in range(len(b33)):
    b26 = ARIMA(b34, order=(5,1,0))
    b36 = b26.fit(disp=-1)
    b37 = b36.forecast()
    b38 = b37[0]
    b35.append(b38)
    b39 = b33[t]
    b34.append(b39)
    print('b40 = %f, expected=%f' % (b38, b39))
b41 = mean_squared_error(b33, b35)
print('Test MSE: %.3f' % b41)
plt.plot(b33,b42 = 'blue', b12='Actuals')
plt.plot(b35, b42 = 'red', b12='Rolling forecast' )
plt.legend()
plt.show()
print('The b26 has the parameters: (a1,a3,a2) = (5,1,0). Its an autoregressive b26')