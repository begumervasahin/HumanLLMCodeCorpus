import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
import arima
def fonk1(file_path, columns):
    b1 = pd.read_csv(file_path, usecols=columns, engine='python', header=0, index_col=0)
    b2 = b1.b2.astype('float32')
    b3 = MinMaxScaler(feature_range=(0, 1))
    b4 = b3.fit_transform(b2)
    b5 = series_to_supervised(b4, a1, 1)
    return b5, b3
def fonk2(b6, b8, b22, b3):
    b6 = b6.reshape((b6.shape[0], b6.shape[2]))
    b7 = b3.inverse_transform(np.concatenate((b22, b6[:, 1:]), axis=1))[:, 0]
    b8 = b8.reshape((len(b8), 1))
    b9 = b3.inverse_transform(np.concatenate((b8, b6[:, 1:]), axis=1))[:, 0]
    return b7, b9
def fonk3(true_values, predicted_values, model_name):
    b10 = mean_squared_error(true_values[arima.test_start:], predicted_values[arima.test_start:])
    b11 = math.sqrt(mean_squared_error(true_values[arima.test_start:], predicted_values[arima.test_start:]))
    b12 = mean_absolute_error(true_values[arima.test_start:], predicted_values[arima.test_start:])
    b13 = arima.mean_a_p_e(true_values[arima.test_start:], predicted_values[arima.test_start:])
    print(f'{model_name} Test MAE: {b12:.3f} MSE: {b10:.3f} RMSE: {b11:.3f} MAPE: {b13:.3f}')
def fonk4(true_values, predicted_values, b14, title):
    plt.plot(true_values[arima.test_start:], '-', b14 = "real flow")
    plt.plot(predicted_values[arima.test_start:], '--', b15 = 'red', b14=b14)
    plt.legend(b16 = 'upper right')
    plt.xlabel("period (15-minute intervals)")
    plt.ylabel("volume (vehicle/period)")
    plt.ylim(0, 800)
    plt.title(title)
    plt.show(b17 = (12, 6))
a1 = 10
b18 = '../model/lstm-15min.h5'
b5, b3 = fonk1('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', [2, 3])
b19 = arima.start + arima.size - a1
b20 = b5.b2[b19:b19 + arima.test_size, :]
b6, b8 = b20[:, :-1], b20[:, -1]
b6 = b6.reshape((b6.shape[0], 1, b6.shape[1]))
b21 = load_model(b18)
b22 = b21.predict(b6)
b7, b9 = fonk2(b6, b8, b22, b3)
fonk3(b9, b7, 'LSTM')
fonk4(b9, b7, 'LSTM', 'LSTM Predictions')
b23 = [(b7[i] + arima.predictions[i]) / 2 for i in range(len(b7))]
fonk3(b9, b23, 'EW b23')
a2 = 1
b24 = []
b25 = []
a3 = 1
a4 = 1
b26 = []
for i in range(len(b7)):
    if len(b24) > 0:
        b27 = np.sqrt(np.sum(b24[-a2:]) / a2)
        b28 = np.sqrt(np.sum(b25[-a2:]) / a2)
        a3 = (1 - b27 / (b27 + b28)) * 2
        a4 = 2 - a3
    b24.append(np.power(b7[i] - b9[i], 2))
    b25.append(np.power(arima.predictions[i] - b9[i], 2))
    b26.append((a3 * b7[i] + a4 * arima.predictions[i]) / 2)
fonk3(b9, b26, 'Dynamic b23')
fonk4(b9, b26, 'Dynamic b23', 'Dynamically Combined Predictions')