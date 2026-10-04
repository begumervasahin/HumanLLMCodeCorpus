import numpy as np
import pandas as pd
from sklearn.svm import SVR
import matplotlib.pyplot as plt
def load_and_prepare_data(filepath):
    data = pd.read_csv(filepath)
    data = data[data['DEXCHUS'] != '.']
    data['DEXCHUS'] = data['DEXCHUS'].astype(float)
    data['returns'] = 100 * data['DEXCHUS'].pct_change()
    data['log_ret'] = np.log(data['DEXCHUS']) - np.log(data['DEXCHUS'].shift(1))
    data = data[data['log_ret'] != 0]
    data['vol_squared'] = data['log_ret']**2
    data['log_vol_squared'] = np.log(data['vol_squared'])
    data = data[1:].reset_index(drop=True)
    return data
def plot_data(data):
    plt.figure()
    data['DEXCHUS'].plot(label='DEXCHUS')
    data['returns'].plot(label='Returns')
    data['vol_squared'].plot(label='Vol Squared')
    plt.legend()
    plt.show()
def prepare_svr_data(data, window_length):
    X = np.zeros((data.shape[0] - window_length, window_length))
    for i in range(window_length, data.shape[0]):
        X[i - window_length] = data['log_ret'][i - window_length:i][::-1]
    y = data['log_vol_squared'][window_length:].values
    return X, y
def fit_and_predict_svr(X, y, kernel='rbf', C=1e3, gamma=250):
    svr = SVR(kernel=kernel, C=C, gamma=gamma)
    y_pred = svr.fit(X, y).predict(X)
    predicted_vol = np.exp(y_pred)
    return predicted_vol
def plot_volatility_forecast(real_vol, predicted_vol_rbf, predicted_vol_linear, predicted_vol_poly, n):
    xaxis = range(len(real_vol))
    plt.figure()
    plt.style.use('ggplot')
    plt.plot(xaxis, real_vol, color='r', label='Real Vol')
    plt.plot(xaxis, predicted_vol_rbf, color='b', label='SVR RBF')
    plt.plot(xaxis, predicted_vol_linear, color='g', label='SVR Linear')
    plt.plot(xaxis, predicted_vol_poly, color='orange', label='SVR Poly')
    plt.title('SVR Volatility Forecasting')
    plt.legend()
    plt.show()
def svr_with_moving_windows(data, window_length):
    X, y = prepare_svr_data(data, window_length)
    predicted_vol_rbf = fit_and_predict_svr(X, y, kernel='rbf')
    real_vol = data['vol_squared'][window_length:].values
    xaxis = range(len(real_vol) - window_length)
    plt.figure()
    plt.style.use('ggplot')
    plt.plot(xaxis, real_vol[-len(xaxis):], color='r', label='Real Vol')
    plt.plot(xaxis, predicted_vol_rbf[-len(xaxis):], color='b', label='SVR RBF')
    plt.title(f'SVR Volatility Forecasting window length: {window_length} days')
    plt.legend()
    plt.show()
def main():
    data = load_and_prepare_data('DEXCHUS.csv')
    plot_data(data)
    window_length = 50
    X, y = prepare_svr_data(data, window_length)
    predicted_vol_rbf = fit_and_predict_svr(X, y, kernel='rbf')
    predicted_vol_linear = fit_and_predict_svr(X, y, kernel='linear')
    predicted_vol_poly = fit_and_predict_svr(X, y, kernel='poly')
    real_vol = data['vol_squared'][window_length:].values
    plot_volatility_forecast(real_vol, predicted_vol_rbf, predicted_vol_linear, predicted_vol_poly, window_length)
    for window_length in range(10, 60, 10):
        svr_with_moving_windows(data, window_length)
if __name__ == "__main__":
    main()