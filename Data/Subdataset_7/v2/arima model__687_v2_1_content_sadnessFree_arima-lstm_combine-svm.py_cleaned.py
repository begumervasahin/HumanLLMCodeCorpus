import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
from sklearn.ensemble import GradientBoostingRegressor
import arima
a1 = 10
a2 = 300
a3 = 5
b1 = a2 + a3 - 1
b2 = '../b26/lstm-15min.h5'
b3 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], engine='python', header=0, index_col=0)
b4 = b3.b4.astype('float32')
b5 = MinMaxScaler(feature_range=(0, 1))
b6 = b5.fit_transform(b4)
b7 = series_to_supervised(b6, a1, 1)
b8 = arima.start + arima.size - a1
b9 = b7.b4[b8:b8 + arima.test_size, :]
b11, b10 = b9[:, :-1], b9[:, -1]
b11 = b11.reshape((b11.shape[0], 1, b11.shape[1]))
b12 = load_model(b2)
b13 = b12.predict(b11)
b11 = b11.reshape((b11.shape[0], b11.shape[2]))
b14 = np.concatenate((b13, b11[:, 1:]), axis=1)
b14 = b5.inverse_transform(b14)[:, 0]
b10 = b10.reshape((len(b10), 1))
b15 = np.concatenate((b10, b11[:, 1:]), axis=1)
b15 = b5.inverse_transform(b15)[:, 0]
b16 = mean_squared_error(b15[b1:], b14[b1:])
b17 = math.sqrt(mean_squared_error(b15[b1:], b14[b1:]))
b18 = mean_absolute_error(b15[b1:], b14[b1:])
b19 = arima.mean_a_p_e(b15[b1:], b14[b1:])
print(f'LSTM Test MAE: {b18:.3f}, MSE: {b16:.3f}, RMSE: {b17:.3f}, MAPE: {b19:.3f}')
plt.plot(b15[b1:], '-', b20 = "Real Flow")
plt.plot(b14[b1:], '--', b21 = 'red', b20="LSTM Predictions")
plt.legend(b22 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show(b23 = (12, 6))
b24 = [(b14[i] + arima.predictions[i]) / 2 for i in range(len(b14))]
b16 = mean_squared_error(b15[b1:], b24[b1:])
b17 = math.sqrt(mean_squared_error(b15[b1:], b24[b1:]))
b18 = mean_absolute_error(b15[b1:], b24[b1:])
b19 = arima.mean_a_p_e(b15[b1:], b24[b1:])
print(f'EW Combined Test MAE: {b18:.3f}, MSE: {b16:.3f}, RMSE: {b17:.3f}, MAPE: {b19:.3f}')
b25 = []
b26 = GradientBoostingRegressor()
b28, b27 = [], []
for i in range(a2 - a3 + 1):
    b28.extend([arima.predictions[i + j][0] for j in range(a3)])
    b28.extend([b14[i + j] for j in range(a3)])
    b27.append(b15[i + a3 - 1])
b28 = np.array(b28).reshape(a2 - a3 + 1, 2 * a3)
b26.fit(b28, b27)
b29 = []
for i in range(arima.test_size - a2 - a3 + 1):
    b29.extend([arima.predictions[a2 + i + j][0] for j in range(a3)])
    b29.extend([b14[a2 + i + j] for j in range(a3)])
b29 = np.array(b29).reshape(arima.test_size - a2 - a3 + 1, 2 * a3)
b25 = b26.predict(b29)
b16 = mean_squared_error(b15[b1:], b25)
b17 = math.sqrt(mean_squared_error(b15[b1:], b25))
b18 = mean_absolute_error(b15[b1:], b25)
b19 = arima.mean_a_p_e(b15[b1:], b25)
print(f'Dynamic Combined Test MAE: {b18:.3f}, MSE: {b16:.3f}, RMSE: {b17:.3f}, MAPE: {b19:.3f}')
plt.figure()
plt.plot(b15[b1:], '-', b20 = "Real Flow")
plt.plot(b25, '--', b21 = 'red', b20="Combined Predictions")
plt.legend(b22 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show(b23 = (12, 6))