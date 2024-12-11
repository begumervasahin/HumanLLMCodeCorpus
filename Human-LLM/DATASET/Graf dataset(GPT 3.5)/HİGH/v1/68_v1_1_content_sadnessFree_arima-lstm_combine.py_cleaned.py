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
a1 = 10
b1 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], engine='python', header=0, index_col=0)
b2 = b1.b2.astype('float32')
b3 = MinMaxScaler(feature_range=(0, 1))
b4 = b3.fit_transform(b2)
b5 = series_to_supervised(b4, a1, 1)
b2 = b5.b2
b6 = arima.start + arima.size - a1
b7 = b2[b6:b6 + arima.test_size, :]
b9, b8 = b7[:, :-1], b7[:, -1]
b9 = b9.reshape((b9.shape[0], 1, b9.shape[1]))
b10 = load_model('../model/lstm-15min.h5')
b11 = b10.predict(b9)
b9 = b9.reshape((b9.shape[0], b9.shape[2]))
b12 = np.concatenate((b11, b9[:, 1:]), axis=1)
b12 = b3.inverse_transform(b12)
b12 = b12[:, 0]
b8 = b8.reshape((len(b8), 1))
b13 = np.concatenate((b8, b9[:, 1:]), axis=1)
b13 = b3.inverse_transform(b13)
b13 = b13[:, 0]
b14 = mean_squared_error(b13[arima.test_start:], b12[arima.test_start:])
b15 = math.sqrt(b14)
b16 = mean_absolute_error(b13[arima.test_start:], b12[arima.test_start:])
b17 = fonk1(b13[arima.test_start:], b12[arima.test_start:])
print('LSTM Test MAE: %.3f MSE: %.3f RMSE: %.3f MAPE: %.3f' % (b16, b14, b15, b17))
plt.plot(b13[arima.test_start:], '-', b18 = "real flow")
plt.plot(b12[arima.test_start:], '--', b19 = 'red', b18="LSTM")
plt.legend(b20 = 'upper right')
plt.xlabel("period (15-minute intervals)")
plt.ylabel("volume (vehicle/period)")
plt.ylim(0, 800)
plt.show(b21 = (12, 6))
b22 = [(b12[i] + arima.predictions[i]) / 2 for i in range(len(b12))]
b14 = mean_squared_error(b13[arima.test_start:], b22[arima.test_start:])
b15 = math.sqrt(b14)
b16 = mean_absolute_error(b13[arima.test_start:], b22[arima.test_start:])
b17 = fonk1(b13[arima.test_start:], b22[arima.test_start:])
print('EW b22 Test MAE: %.3f MSE: %.3f RMSE: %.3f MAPE: %.3f' % (b16, b14, b15, b17))
plt.figure()
plt.plot(b13[arima.test_start:], '-', b18 = "real flow")
plt.plot(b22[arima.test_start:], '--', b19 = 'red', b18="b22")
plt.legend(b20 = 'upper right')
plt.xlabel("period (15-minute intervals)")
plt.ylabel("volume (vehicle/period)")
plt.ylim(0, 800)
plt.show(b21 = (12, 6))
a2 = 1
b23 = []
b24 = []
a3 = 1
a4 = 1
b25 = []
for i in range(len(b12)):
    if len(b23) > 0:
        b26 = math.pow(np.sum(b23[-a2:]), 1 / 2) / math.pow(a2, 1 / 2)
        b27 = math.pow(np.sum(b24[-a2:]), 1 / 2) / math.pow(a2, 1 / 2)
        a3 = (1 - b26 / (b26 + b27)) * 2
        a4 = 2 - a3
    b23.append(math.pow(b12[i] - b13[i], 2))
    b24.append(math.pow(arima.predictions[i] - b13[i], 2))
    b25.append((a3 * b12[i] + a4 * arima.predictions[i]) / 2)
b14 = mean_squared_error(b13[arima.test_start:], b25[arima.test_start:])
b15 = math.sqrt(b14)
b16 = mean_absolute_error(b13[arima.test_start:], b25[arima.test_start:])
b17 = fonk1(b13[arima.test_start:], b25[arima.test_start:])
print('Dyn b22 Test MAE: %.3f MSE: %.3f RMSE: %.3f MAPE: %.3f' % (b16, b14, b15, b17))
plt.figure()
plt.plot(b13[arima.test_start:], '-', b18 = "real flow")
plt.plot(b25[arima.test_start:], '--', b19 = 'red', b18="b22")
plt.legend(b20 = 'upper right')
plt.xlabel("period (15-minute intervals)")
plt.ylabel("volume (vehicle/period)")
plt.ylim(0, 800)
plt.show(b21 = (12, 6))