import numpy as np
import pandas as pd
from sklearn.svm import SVR
import matplotlib.pyplot as plt
def fonk1(filepath):
    b1 = pd.read_csv(filepath)
    b1 = b1[b1['DEXCHUS'] != '.']
    b1['DEXCHUS'] = b1['DEXCHUS'].astype(float)
    b1['returns'] = 100 * b1['DEXCHUS'].pct_change()
    b1['log_ret'] = np.log(b1['DEXCHUS']) - np.log(b1['DEXCHUS'].shift(1))
    b1 = b1[b1['log_ret'] != 0]
    b1['vol_squared'] = b1['log_ret']**2
    b1['log_vol_squared'] = np.log(b1['vol_squared'])
    b1 = b1[1:].reset_index(drop=True)
    return b1
def fonk2(b1):
    plt.figure()
    b1['DEXCHUS'].plot(b2 = 'DEXCHUS')
    b1['returns'].plot(b2 = 'Returns')
    b1['vol_squared'].plot(b2 = 'Vol Squared')
    plt.legend()
    plt.show()
def fonk3(b1, a1):
    b3 = np.zeros((b1.shape[0] - a1, a1))
    for i in range(a1, b1.shape[0]):
        b3[i - a1] = b1['log_ret'][i - a1:i][::-1]
    b4 = b1['log_vol_squared'][a1:].values
    return b3, b4
def fonk4(b3, b4, b5 = 'rbf', C=1e3, gamma=250):
    b6 = SVR(b5=b5, C=C, gamma=gamma)
    b7 = b6.fit(b3, b4).predict(b3)
    b8 = np.exp(b7)
    return b8
def fonk5(b12, b11, b13, b14, n):
    b9 = range(len(b12))
    plt.figure()
    plt.style.use('ggplot')
    plt.plot(b9, b12, b10 = 'r', b2='Real Vol')
    plt.plot(b9, b11, b10 = 'b', b2='SVR RBF')
    plt.plot(b9, b13, b10 = 'g', b2='SVR Linear')
    plt.plot(b9, b14, b10 = 'orange', b2='SVR Poly')
    plt.title('SVR Volatility Forecasting')
    plt.legend()
    plt.show()
def fonk6(b1, a1):
    b3, b4 = fonk3(b1, a1)
    b11 = fonk4(b3, b4, b5='rbf')
    b12 = b1['vol_squared'][a1:].values
    b9 = range(len(b12) - a1)
    plt.figure()
    plt.style.use('ggplot')
    plt.plot(b9, b12[-len(b9):], b10 = 'r', b2='Real Vol')
    plt.plot(b9, b11[-len(b9):], b10 = 'b', b2='SVR RBF')
    plt.title(f'SVR Volatility Forecasting window length: {a1} days')
    plt.legend()
    plt.show()
def fonk7():
    b1 = fonk1('DEXCHUS.csv')
    fonk2(b1)
    a1 = 50
    b3, b4 = fonk3(b1, a1)
    b11 = fonk4(b3, b4, b5='rbf')
    b13 = fonk4(b3, b4, b5='linear')
    b14 = fonk4(b3, b4, b5='poly')
    b12 = b1['vol_squared'][a1:].values
    fonk5(b12, b11, b13, b14, a1)
    for a1 in range(10, 60, 10):
        fonk6(b1, a1)
if b15 = = "__main__":
    fonk7()