import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
import arima
def fonk1(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
def fonk2(predictions, b15, b1 = True):
    b2 = b15.inverse_transform(predictions)[:, 0]
    return b2.b1((len(b2), 1)) if b1 else b2
def fonk3(true_values, predicted_values, b3 = ""):
    b4 = mean_squared_error(true_values, predicted_values)
    b5 = math.sqrt(b4)
    b6 = mean_absolute_error(true_values, predicted_values)
    b7 = fonk1(true_values, predicted_values)
    print(f'{b3}Test MAE: {b6:.3f} MSE: {b4:.3f} RMSE: {b5:.3f} MAPE: {b7:.3f}')
def fonk4(true_values, predicted_values, b8 = "Real Flow", label_pred="Predictions"):
    plt.plot(true_values, '-', b9 = b8)
    plt.plot(predicted_values, '--', b10 = 'red', b9=label_pred)
    plt.legend(b11 = 'upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicles/period)")
    plt.ylim(0, 800)
    plt.show(b12 = (12, 6))
a1 = 10
a2 = 1
b13 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], engine='python', header=0, index_col=0)
b14 = b13.b14.astype('float32')
b15 = MinMaxScaler(feature_range=(0, 1))
b16 = b15.fit_transform(b14)
b17 = series_to_supervised(b16, a1, 1)
b14 = b17.b14
b18 = arima.start + arima.size - a1
b19 = b14[b18:b18 + arima.test_size, :]
b21, b20 = b19[:, :-1], b19[:, -1]
b21 = b21.b1((b21.shape[0], 1, b21.shape[1]))
b22 = load_model('../model/lstm-15min.h5')
b23 = b22.predict(b21)
b24 = fonk2(np.concatenate((b23, b21[:, 1:]), axis=1), b15)
b25 = fonk2(np.concatenate((b20.b1((len(b20), 1)), b21[:, 1:]), axis=1), b15)
fonk3(b25[arima.test_start:], b24[arima.test_start:], b3 = "LSTM ")
fonk4(b25[arima.test_start:], b24[arima.test_start:], b8 = "Real Flow", label_pred="LSTM Predictions")
b26 = [(b24[i] + arima.predictions[i]) / 2 for i in range(len(b24))]
fonk3(b25[arima.test_start:], b26[arima.test_start:], b3 = "EW Combined ")
fonk4(b25[arima.test_start:], b26[arima.test_start:], b8 = "Real Flow", label_pred="Combined Predictions")
b27 = []
b28 = []
a3 = 1
a4 = 1
b29 = []
for i in range(len(b24)):
    if len(b27) > 0:
        b30 = math.sqrt(np.sum(b27[-a2:]) / a2)
        b31 = math.sqrt(np.sum(b28[-a2:]) / a2)
        a3 = (1 - b30 / (b30 + b31)) * 2
        a4 = 2 - a3
    b27.append((b24[i] - b25[i]) ** 2)
    b28.append((arima.predictions[i] - b25[i]) ** 2)
    b29.append((a3 * b24[i] + a4 * arima.predictions[i]) / 2)
fonk3(b25[arima.test_start:], b29[arima.test_start:], b3 = "Dynamic Combined ")
fonk4(b25[arima.test_start:], b29[arima.test_start:], b8 = "Real Flow", label_pred="Dynamic Combined Predictions")