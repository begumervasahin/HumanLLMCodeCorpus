import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
from sklearn.metrics import mean_squared_error, mean_absolute_error
from keras.models import load_model
from sklearn import linear_model
plt.rcParams['font.family'] = 'SimHei'
def fonk1(b19):
    b1 = pd.read_csv(b19, usecols=[2, 3], engine='python', header=0, index_col=0)
    b2 = b1.b2.astype('float32')
    b3 = MinMaxScaler(feature_range=(0, 1))
    b4 = b3.fit_transform(b2)
    return b3, b4
def fonk2(b20, a1):
    b5 = series_to_supervised(b20, a1, 1)
    b2 = b5.b2
    return b2
def fonk3(model, test_X):
    b6 = model.predict(test_X.reshape((test_X.shape[0], 1, test_X.shape[1])))
    return b6
def fonk4(b8, test_X, b7, b3, start_idx):
    b7 = b3.inverse_transform(np.concatenate((b6, test_X[:, 1:]), axis=1))[:, 0]
    b8 = b8.reshape((len(b8), 1))
    b9 = b3.inverse_transform(np.concatenate((b8, test_X[:, 1:]), axis=1))[:, 0]
    b10 = mean_squared_error(b9[start_idx:], b7[start_idx:])
    b11 = math.sqrt(mean_squared_error(b9[start_idx:], b7[start_idx:]))
    b12 = mean_absolute_error(b9[start_idx:], b7[start_idx:])
    b13 = arima.mean_a_p_e(b9[start_idx:], b7[start_idx:])
    return b9, b7, b10, b11, b12, b13
def fonk5(b9, b7, b14 = 'real flow', label_predicted='LSTM'):
    plt.plot(b9, '-', b15 = b14)
    plt.plot(b7, '--', b16 = 'red', b15=label_predicted)
    plt.legend(b17 = 'upper right')
    plt.xlabel("period(15-minute intervals)")
    plt.ylabel("volume(vehicle/period)")
    plt.ylim(0, 800)
    plt.show(b18 = (12, 6))
def fonk6():
    a1 = 10
    a2 = 300
    a3 = 7
    b19 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    b3, b20 = fonk1(b19)
    b21 = fonk2(b20, a1)
    b22 = load_model('../model/lstm-15min.h5')
    b23 = arima.start + arima.size - a1
    b24 = b21[b23:b23 + arima.test_size, :]
    test_X, b8 = b24[:, :-1], b24[:, -1]
    b6 = fonk3(b22, test_X)
    b9, b7, b10, b11, b12, b13 = fonk4(b8, test_X, b6, b3, test_start)
    print(f'LSTM Test MAE: {b12:.3f} MSE: {b10:.3f} RMSE: {b11:.3f} MAPE: {b13:.3f}')
    fonk5(b9, b7, b14 = 'real flow', label_predicted='LSTM')
if b25 = = "__main__":
    fonk6()