import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
from sklearn.ensemble import GradientBoostingRegressor
a1 = 10
a2 = 300
a3 = 5
b1 = a2 + a3 - 1
b2 = '../b27/lstm-15min.h5'
b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b4 = pd.read_csv(b3, usecols=[2, 3], engine='python', header=0, index_col=0)
b5 = b4.b5.astype('float32')
b6 = MinMaxScaler(feature_range=(0, 1))
b7 = b6.fit_transform(b5)
b8 = series_to_supervised(b7, a1, 1)
b9 = arima.start + arima.size - a1
b10 = b8.b5[b9:b9 + arima.test_size, :]
b12, b11 = b10[:, :-1], b10[:, -1]
b12 = b12.reshape((b12.shape[0], 1, b12.shape[1]))
b13 = load_model(b2)
b14 = b13.predict(b12)
b12 = b12.reshape((b12.shape[0], b12.shape[2]))
b15 = b6.inverse_transform(np.concatenate((b14, b12[:, 1:]), axis=1))[:, 0]
b11 = b11.reshape((len(b11), 1))
b16 = b6.inverse_transform(np.concatenate((b11, b12[:, 1:]), axis=1))[:, 0]
b17 = mean_squared_error(b16[b1:], b15[b1:])
b18 = math.sqrt(mean_squared_error(b16[b1:], b15[b1:]))
b19 = mean_absolute_error(b16[b1:], b15[b1:])
b20 = arima.mean_a_p_e(b16[b1:], b15[b1:])
print('LSTM Test MAE: %.3f MSE: %.3f RMSE: %.3f MAPE: %.3f' % (b19, b17, b18, b20))
plt.plot(b16[b1:], '-', b21 = "Real Flow")
plt.plot(b15[b1:], '--', b22 = 'red', b21="LSTM Predictions")
plt.legend(b23 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show(b24 = (12, 6))
b25 = [(b15[i] + arima.predictions[i]) / 2 for i in range(len(b15))]
b17 = mean_squared_error(b16[b1:], b25[b1:])
b18 = math.sqrt(mean_squared_error(b16[b1:], b25[b1:]))
b19 = mean_absolute_error(b16[b1:], b25[b1:])
b20 = arima.mean_a_p_e(b16[b1:], b25[b1:])
print('EW Combined Test MAE: %.3f MSE: %.3f RMSE: %.3f MAPE: %.3f' % (b19, b17, b18, b20))
b26 = list()
b27 = GradientBoostingRegressor()
b28 = []
b29 = []
for i in range(a2 - a3 + 1):
    for j in range(a3):
        b28.append(arima.predictions[i + j][0])
    for j in range(a3):
        b28.append(b15[i + j])
    b29.append(b16[i + a3 - 1])
b28 = np.array(b28).reshape(a2 - a3 + 1, 2 * a3)
b27.fit(b28, b29)
b30 = []
for i in range(arima.test_size - a2 - a3 + 1):
    for j in range(a3):
        b30.append(arima.predictions[a2 + i + j][0])
    for j in range(a3):
        b30.append(b15[a2 + i + j])
b30 = np.array(b30).reshape(arima.test_size - a2 - a3 + 1, 2 * a3)
b26 = b27.pre