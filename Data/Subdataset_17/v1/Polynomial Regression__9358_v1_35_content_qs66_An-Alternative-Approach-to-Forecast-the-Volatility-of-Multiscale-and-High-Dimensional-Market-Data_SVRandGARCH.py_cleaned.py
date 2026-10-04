import numpy as np
import pandas as pd
from sklearn.svm import SVR
import matplotlib.pyplot as plt
data = pd.read_csv('DEXCHUS.csv')
data = data[data['DEXCHUS'] != '.']
data['DEXCHUS'] = data['DEXCHUS'].astype(float)
data['returns'] = 100 * data['DEXCHUS'].pct_change()
data['log_ret'] = np.log(data['DEXCHUS']) - np.log(data['DEXCHUS'].shift(1))
data = data[data['log_ret'] != 0]
data['vol_squared'] = data['log_ret']**2
data['log_vol_squared'] = np.log(data['vol_squared'])
data = data[1:].reset_index(drop=True)
plt.figure()
data['DEXCHUS'].plot(label='DEXCHUS')
data['returns'].plot(label='Returns')
data['vol_squared'].plot(label='Vol Squared')
plt.legend()
plt.show()
n = 50
X = np.zeros((data.shape[0] - n, n))
for i in range(n, data.shape[0]):
    X[i - n] = data['log_ret'][i - n:i][::-1]
y = data['log_vol_squared'][n:].values
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=250)
y_rbf = svr_rbf.fit(X, y).predict(X)
predicted_vol_rbf = np.exp(y_rbf)
svr_linear = SVR(kernel='linear', C=1e3, gamma=250)
y_linear = svr_linear.fit(X, y).predict(X)
predicted_vol_linear = np.exp(y_linear)
svr_poly = SVR(kernel='poly', C=1e3, gamma=250)
y_poly = svr_poly.fit(X, y).predict(X)
predicted_vol_poly = np.exp(y_poly)
real_vol = data['vol_squared'][n:].values
xaxis = range(data.shape[0] - n)
plt.figure()
plt.style.use('ggplot')
plt.plot(xaxis, real_vol, color='r', label='Real Vol')
plt.plot(xaxis, predicted_vol_rbf, color='b', label='SVR RBF')
plt.plot(xaxis, predicted_vol_linear, color='g', label='SVR Linear')
plt.plot(xaxis, predicted_vol_poly, color='orange', label='SVR Poly')
plt.title('SVR Volatility Forecasting')
plt.legend()
plt.show()
def SVR_with_moving_windows(n):
    X = np.zeros((data.shape[0] - n, n))
    for i in range(n, data.shape[0]):
        X[i - n] = data['log_ret'][i - n:i][::-1]
    y = data['log_vol_squared'][n:].values
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=250)
    y_rbf = svr_rbf.fit(X, y).predict(X)
    predicted_vol_rbf = np.exp(y_rbf)
    real_vol = data['vol_squared'][n:].values
    xaxis = range(len(real_vol) - n)
    plt.figure()
    plt.style.use('ggplot')
    plt.plot(xaxis, real_vol[-len(xaxis):], color='r', label='Real Vol')
    plt.plot(xaxis, predicted_vol_rbf[-len(xaxis):], color='b', label='SVR RBF')
    plt.title(f'SVR Volatility Forecasting window length: {n} days')
    plt.legend()
    plt.show()
for i in range(10, 60, 10):
    SVR_with_moving_windows(i)