import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
import arima
a1 = 10
b1 = '../model/lstm-15min.h5'
b2 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], engine='python',
                        b3 = 0, index_col=0)
b4 = b2.b4.astype('float32')
b5 = MinMaxScaler(feature_range=(0, 1))
b6 = b5.fit_transform(b4)
b7 = series_to_supervised(b6, a1, 1)
b8 = arima.start + arima.size - a1
b9 = b7.b4[b8:b8 + arima.test_size, :]
b11, b10 = b9[:, :-1], b9[:, -1]
b11 = b11.reshape((b11.shape[0], 1, b11.shape[1]))
b12 = load_model(b1)
b13 = b12.predict(b11)
b11 = b11.reshape((b11.shape[0], b11.shape[2]))
b14 = b5.inverse_transform(np.concatenate((b13, b11[:, 1:]), axis=1))[:, 0]
b10 = b10.reshape((len(b10), 1))
b15 = b5.inverse_transform(np.concatenate((b10, b11[:, 1:]), axis=1))[:, 0]
b16 = mean_squared_error(b15[arima.test_start:], b14[arima.test_start:])
b17 = math.sqrt(mean_squared_error(b15[arima.test_start:], b14[arima.test_start:]))
b18 = mean_absolute_error(b15[arima.test_start:], b14[arima.test_start:])
b19 = arima.mean_a_p_e(b15[arima.test_start:], b14[arima.test_start:])
print('LSTM Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b18, b16, b17, b19))
plt.plot(b15[arima.test_start:], '-', b20 = "real flow")
plt.plot(b14[arima.test_start:], '--', b21 = 'red', b20="LSTM")
plt.legend(b22 = 'upper right')
plt.xlabel("period (15-minute intervals)")
plt.ylabel("volume (vehicle/period)")
plt.ylim(0, 800)
plt.show(b23 = (12, 6))
b24 = [(b14[i] + arima.predictions[i]) / 2 for i in range(len(b14))]
b16 = mean_squared_error(b15[arima.test_start:], b24[arima.test_start:])
b17 = math.sqrt(mean_squared_error(b15[arima.test_start:], b24[arima.test_start:]))
b18 = mean_absolute_error(b15[arima.test_start:], b24[arima.test_start:])
b19 = arima.mean_a_p_e(b15[arima.test_start:], b24[arima.test_start:])
print('EW b24 Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b18, b16, b17, b19))
a2 = 1
b25 = []
b26 = []
a3 = 1
a4 = 1
b27 = []
for i in range(len(b14)):
    if len(b25) > 0:
        b28 = np.sqrt(np.sum(b25[-a2:]) / a2)
        b29 = np.sqrt(np.sum(b26[-a2:]) / a2)
        a3 = (1 - b28 / (b28 + b29)) * 2
        a4 = 2 - a3
    b25.append(np.power(b14[i] - b15[i], 2))
    b26.append(np.power(arima.predictions[i] - b15[i], 2))
    b27.append((a3 * b14[i] + a4 * arima.predictions[i]) / 2)
b16 = mean_squared_error(b15[arima.test_start:], b27[arima.test_start:])
b17 = math.sqrt(mean_squared_error(b15[arima.test_start:], b27[arima.test_start:]))
b18 = mean_absolute_error(b15[arima.test_start:], b27[arima.test_start:])
b19 = arima.mean_a_p_e(b15[arima.test_start:], b27[arima.test_start:])
print('dyn b24 Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b18, b16, b17, b19))
plt.figure()
plt.plot(b15[arima.test_start:], '-', b20 = "real flow")
plt.plot(b27[arima.test_start:], '--', b21 = 'red', b20="b24")
plt.legend(b22 = 'upper right')
plt.xlabel("period (15-minute intervals)")
plt.ylabel("volume (vehicle/period)")
plt.ylim(0, 800)
plt.show(b23 = (12, 6))