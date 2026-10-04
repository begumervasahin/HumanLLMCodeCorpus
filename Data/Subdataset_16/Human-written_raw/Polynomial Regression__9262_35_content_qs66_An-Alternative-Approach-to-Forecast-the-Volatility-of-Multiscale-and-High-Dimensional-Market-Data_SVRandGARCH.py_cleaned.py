
import numpy as np
import pandas as pd
from sklearn.svm import SVR
import matplotlib.pyplot as plt
b1 = pd.read_csv('b2.csv')
b1 = b1[b1['b2'] != '.']
b1.b2 = b1.b2.astype(float)
b1['b3'] = 100 * b1.b2.pct_change().dropna()
b1['log_ret'] = np.log(b1.b2) - np.log(b1.b2.shift(1))
b1 = b1[b1.log_ret!=0]
b1['vol_squared'] = b1['log_ret']**2
b1['log_vol_squared'] = np.log(b1['log_ret']**2)
b1 = b1[1:]
b1 = b1.reset_index(drop=True)
b1.b2.plot()
b1.b3.plot()
b1.vol_squared.plot()
'''
b3 = b1.b3.dropna().as_matrix()
from arch.univariate import arch_model
b4 = arch_model(b3)
b5 = b4.fit()
b5.summary()
b6 = b5.plot()
'''
a1 = 50
b7 = np.zeros((b1.shape[0]-a1,a1))
for i in range(a1,b1.shape[0]):
    for j in range(a1):
        b7[i-a1][j] = b1.log_ret[i-j-1]
b8 = np.zeros(b1.shape[0]-a1)
for i in range(b1.shape[0]-a1):
    b8[i] = b1.log_vol_squared[i+a1]
b9 = SVR(kernel='rbf',C=1e3,gamma=250)
b10 = b9.fit(b7,b8).predict(b7)
b11 = np.exp(b10)
b12 = SVR(kernel='linear',C=1e3,gamma=250)
b13 = b12.fit(b7,b8).predict(b7)
b14 = np.exp(b13)
b15 = SVR(kernel = 'poly',C=1e3,gamma=250)
b16 = b15.fit(b7,b8).predict(b7)
b17 = np.exp(b16)
b18 = b1.vol_squared[a1:].as_matrix()
b19 = range(150-a1)
plt.style.use('ggplot')
plt.plot(b19,b18[b1.shape[0]-150:],b20 = 'r',label='b18')
plt.plot(b19,b11[b1.shape[0]-150:],b20 = 'b',label='b9')
plt.plot(b19,b14[b1.shape[0]-150:],b20 = 'g',label='b12')
plt.plot(b19,b17[b1.shape[0]-150:],b20 = 'orange',label='b15')
plt.title('SVR Volatility Forecasting')
plt.legend()
plt.show()
def fonk1(a1):
    b7 = np.zeros((b1.shape[0]-a1,a1))
    for i in range(a1,b1.shape[0]):
        for j in range(a1):
            b7[i-a1][j] = b1.log_ret[i-j-1]
    b8 = np.zeros(b1.shape[0]-a1)
    for i in range(b1.shape[0]-a1):
        b8[i] = b1.log_vol_squared[i+a1]
    b9 = SVR(kernel='rbf',C=1e3,gamma=250)
    b10 = b9.fit(b7,b8).predict(b7)
    b11 = np.exp(b10)
    b18 = b1.vol_squared[a1:].as_matrix()
    b19 = range(100)
    plt.style.use('ggplot')
    plt.plot(b19,b18[b1.shape[0]-100-a1:],b20 = 'r',label='b18')
    plt.plot(b19,b11[b1.shape[0]-100-a1:],b20 = 'b',label='b9')
    plt.title('SVR Volatility Forecasting window length: %d days'%(a1))
    plt.legend()
    plt.show()
for i in range(10,60,10):
    fonk1(i)