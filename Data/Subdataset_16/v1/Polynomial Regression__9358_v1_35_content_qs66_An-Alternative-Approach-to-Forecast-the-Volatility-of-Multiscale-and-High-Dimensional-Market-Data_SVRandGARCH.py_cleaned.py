import numpy as np
import pandas as pd
from sklearn.svm import SVR
import matplotlib.pyplot as plt
b1 = pd.read_csv('DEXCHUS.csv')
b1 = b1[b1['DEXCHUS'] != '.']
b1['DEXCHUS'] = b1['DEXCHUS'].astype(float)
b1['returns'] = 100 * b1['DEXCHUS'].pct_change()
b1['log_ret'] = np.log(b1['DEXCHUS']) - np.log(b1['DEXCHUS'].shift(1))
b1 = b1[b1['log_ret'] != 0]
b1['vol_squared'] = b1['log_ret']**2
b1['log_vol_squared'] = np.log(b1['vol_squared'])
b1 = b1[1:].reset_index(drop=True)
plt.figure()
b1['DEXCHUS'].plot(b2 = 'DEXCHUS')
b1['returns'].plot(b2 = 'Returns')
b1['vol_squared'].plot(b2 = 'Vol Squared')
plt.legend()
plt.show()
a1 = 50
b3 = np.zeros((b1.shape[0] - a1, a1))
for i in range(a1, b1.shape[0]):
    b3[i - a1] = b1['log_ret'][i - a1:i][::-1]
b4 = b1['log_vol_squared'][a1:].values
b5 = SVR(kernel='rbf', C=1e3, gamma=250)
b6 = b5.fit(b3, b4).predict(b3)
b7 = np.exp(b6)
b8 = SVR(kernel='linear', C=1e3, gamma=250)
b9 = b8.fit(b3, b4).predict(b3)
b10 = np.exp(b9)
b11 = SVR(kernel='poly', C=1e3, gamma=250)
b12 = b11.fit(b3, b4).predict(b3)
b13 = np.exp(b12)
b14 = b1['vol_squared'][a1:].values
b15 = range(b1.shape[0] - a1)
plt.figure()
plt.style.use('ggplot')
plt.plot(b15, b14, b16 = 'r', b2='Real Vol')
plt.plot(b15, b7, b16 = 'b', b2='SVR RBF')
plt.plot(b15, b10, b16 = 'g', b2='SVR Linear')
plt.plot(b15, b13, b16 = 'orange', b2='SVR Poly')
plt.title('SVR Volatility Forecasting')
plt.legend()
plt.show()
def fonk1(a1):
    b3 = np.zeros((b1.shape[0] - a1, a1))
    for i in range(a1, b1.shape[0]):
        b3[i - a1] = b1['log_ret'][i - a1:i][::-1]
    b4 = b1['log_vol_squared'][a1:].values
    b5 = SVR(kernel='rbf', C=1e3, gamma=250)
    b6 = b5.fit(b3, b4).predict(b3)
    b7 = np.exp(b6)
    b14 = b1['vol_squared'][a1:].values
    b15 = range(len(b14) - a1)
    plt.figure()
    plt.style.use('ggplot')
    plt.plot(b15, b14[-len(b15):], b16 = 'r', b2='Real Vol')
    plt.plot(b15, b7[-len(b15):], b16 = 'b', b2='SVR RBF')
    plt.title(f'SVR Volatility Forecasting window length: {a1} days')
    plt.legend()
    plt.show()
for i in range(10, 60, 10):
    fonk1(i)