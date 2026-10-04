
import numpy as np
import pandas as pd
from sklearn.svm import SVR
import matplotlib.pyplot as plt
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b1 = b1[b1['DEXCHUS'] != '.']
    b1['DEXCHUS'] = b1['DEXCHUS'].astype(float)
    b1['returns'] = 100 * b1['DEXCHUS'].pct_change().dropna()
    b1['log_ret'] = np.log(b1['DEXCHUS']) - np.log(b1['DEXCHUS'].shift(1))
    b1 = b1[b1['log_ret'] != 0]
    b1['vol_squared'] = b1['log_ret']**2
    b1['log_vol_squared'] = np.log(b1['vol_squared'])
    b1 = b1[1:].reset_index(drop=True)
    return b1
def fonk2(b1):
    plt.figure(b2 = (12, 6))
    b1['DEXCHUS'].plot(b3 = 'DEXCHUS', label='DEXCHUS')
    plt.legend()
    plt.show()
    plt.figure(b2 = (12, 6))
    b1['returns'].plot(b3 = 'Returns', label='Returns')
    plt.legend()
    plt.show()
    plt.figure(b2 = (12, 6))
    b1['vol_squared'].plot(b3 = 'Volatility Squared', label='Volatility Squared')
    plt.legend()
    plt.show()
def fonk3(b1, a1):
    b4 = np.zeros((b1.shape[0] - a1, a1))
    for i in range(a1, b1.shape[0]):
        b4[i - a1] = b1['log_ret'][i - a1:i]
    b5 = b1['log_vol_squared'][a1:]
    return b4, b5
def fonk4(b4, b5):
    b6 = {
        'rbf': SVR(b7 = 'rbf', C=1e3, gamma=250),
        'linear': SVR(b7 = 'linear', C=1e3, gamma=250),
        'poly': SVR(b7 = 'poly', C=1e3, gamma=250)
    }
    b8 = {}
    for name, model in b6.items():
        b8[name] = np.exp(model.fit(b4, b5).predict(b4))
    return b8
def fonk5(b13, b12, a1, b9 = ''):
    b10 = range(len(b13) - a1)
    plt.figure(b2 = (12, 6))
    plt.plot(b10, b13[-len(b10):], b11 = 'r', label='Real Volatility')
    plt.plot(b10, b12['rbf'][-len(b10):], b11 = 'b', label='SVR RBF')
    plt.plot(b10, b12['linear'][-len(b10):], b11 = 'g', label='SVR Linear')
    plt.plot(b10, b12['poly'][-len(b10):], b11 = 'orange', label='SVR Poly')
    plt.b3(f'SVR Volatility Forecasting {b9}')
    plt.legend()
    plt.show()
def fonk6():
    b1 = fonk1('DEXCHUS.csv')
    fonk2(b1)
    a1 = 50
    b4, b5 = fonk3(b1, a1)
    b12 = fonk4(b4, b5)
    b13 = b1['vol_squared'][a1:]
    fonk5(b13, b12, a1)
    for window in range(10, 60, 10):
        b4, b5 = fonk3(b1, window)
        b12 = fonk4(b4, b5)
        fonk5(b1['vol_squared'][window:], b12, window, f'window length: {window} days')
if b14 = = "__main__":
    fonk6()