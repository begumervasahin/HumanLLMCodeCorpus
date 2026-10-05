import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from b29 import mean_a_p_e
from HM import hm_p
from svr import svr_test
from keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
from sklearn import linear_model
plt.rcParams['font.family'] = 'SimHei'
a1 = 10
a2 = 300
a3 = 7
b1 = pd.read_csv('/Users/daihanru/Desktop/b29-b30/DataSet/FEB15-2.csv', usecols=[2, 3], engine='python', header=0, index_col=0)
b2 = b1.b2.astype('float32')
b3 = MinMaxScaler(feature_range=(0, 1))
b4 = b3.fit_transform(b2)
b5 = series_to_supervised(b4, a1, 1)
b6 = b29.start + b29.size - a1
b7 = b5.b2[b6:b6 + b29.test_size, :]
b9, b8 = b7[:, :-1], b7[:, -1]
b9 = b9.reshape((b9.shape[0], 1, b9.shape[1]))
b10 = load_model('../b24/b30-15min.h5')
b11 = b10.predict(b9)
b9 = b9.reshape((b9.shape[0], b9.shape[2]))
b12 = b3.inverse_transform(np.concatenate((b11, b9[:, 1:]), axis=1))[:, 0]
b8 = b8.reshape((len(b8), 1))
b13 = b3.inverse_transform(np.concatenate((b8, b9[:, 1:]), axis=1))[:, 0]
b14 = mean_squared_error(b13[test_start:], b12[test_start:])
b15 = math.sqrt(mean_squared_error(b13[test_start:], b12[test_start:]))
b16 = mean_absolute_error(b13[test_start:], b12[test_start:])
b17 = b29.mean_a_p_e(b13[test_start:], b12[test_start:])
print(f'LSTM Test MAE: {b16:.3f} MSE: {b14:.3f} RMSE: {b15:.3f} MAPE: {b17:.3f}')
plt.plot(b13[test_start:], '-', b18 = "Real Flow")
plt.plot(b12[test_start:], '--', b19 = 'red', b18="LSTM")
plt.legend(b20 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show(b21 = (12, 6))
b22 = [(b12[i] + b29.predictions[i]) / 2 for i in range(len(b12))]
b14 = mean_squared_error(b13[test_start:], b22[test_start:])
b15 = math.sqrt(mean_squared_error(b13[test_start:], b22[test_start:]))
b16 = mean_absolute_error(b13[test_start:], b22[test_start:])
b17 = b29.mean_a_p_e(b13[test_start:], b22[test_start:])
print(f'EW Combined Test MAE: {b16:.3f} MSE: {b14:.3f} RMSE: {b15:.3f} MAPE: {b17:.3f}')
b23 = []
b24 = linear_model.LinearRegression(normalize=True)
b26, b25 = [], []
for i in range(a2 - a3 + 1):
    b26.extend([b29.predictions[i + j][0] for j in range(a3)])
    b26.extend([b12[i + j] for j in range(a3)])
    b25.append(b13[i + a3 - 1])
b26 = np.array(b26).reshape(a2 - a3 + 1, 2 * a3)
b24.fit(b26, b25)
b27 = []
for i in range(b29.test_size - a2 - a3 + 1):
    b27.extend([b29.predictions[a2 + i + j][0] for j in range(a3)])
    b27.extend([b12[a2 + i + j] for j in range(a3)])
b27 = np.array(b27).reshape(b29.test_size - a2 - a3 + 1, 2 * a3)
b23 = b24.predict(b27)
b14 = mean_squared_error(b13[test_start:], b23[b29.a3 - a3:])
b15 = math.sqrt(mean_squared_error(b13[test_start:], b23[b29.a3 - a3:]))
b16 = mean_absolute_error(b13[test_start:], b23[b29.a3 - a3:])
b17 = b29.mean_a_p_e(b13[test_start:], b23[b29.a3 - a3:])
print(f'Dynamic Combined Test MAE: {b16:.3f} MSE: {b14:.3f} RMSE: {b15:.3f} MAPE: {b17:.3f}')
plt.figure(b21 = (12, 6))
plt.plot(b13[test_start:], '-', b18 = "Real Flow")
plt.plot(b23[b29.a3 - a3:], '--', b19 = 'red', b18="Arima-LSTM-Linear-7")
plt.legend(b20 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show()
plt.figure(b21 = (12, 6))
plt.plot(b29.predictions[test_start + 40:test_start + 140], '-+', b18 = "ARIMA Predictions")
plt.plot(b12[test_start + 40:test_start + 140], '-.', b18 = "LSTM Predictions")
plt.plot(hm_p[40:140], '--.', b18 = 'HM Predictions')
plt.plot(svr_test[40:140], '-x', b18 = 'SVR Predictions')
plt.plot(b13[test_start + 40:test_start + 140], '-', b18 = "Real Flow")
plt.legend(b20 = 'upper right')
plt.xlabel("Period (15min)")
plt.ylabel("Traffic Volume (Vehicles/Period)")
plt.show()
b28 = np.array(b13[test_start:])
b29 = np.array(b29.predictions[test_start:])
b30 = np.array(b12[test_start:])
b31 = np.array(b23[10 - a3:])
b32 = np.abs(b29 - b28)
b33 = np.abs(b30 - b28)
b34 = np.abs(hm_p[40:140] - b28[40:140])
b35 = np.abs(svr_test[40:140] - b28[40:140])
b36 = np.abs(b31 - b28[40:140])
plt.figure(b21 = (12, 6))
plt.plot(b32, '-', b18 = "ARIMA Error")
plt.plot(b33, '-', b19 = 'r', b18="LSTM Error")
plt.plot(b34, '-', b19 = 'g', b18="HM Error")
plt.plot(b35, '-', b18 = "SVR Error")
plt.legend(b20 = 'upper right')
plt.xlabel("Period (15min)")
plt.ylabel("Traffic Volume (Vehicles/Period)")
plt.ylim(0, 250)
plt.show()
plt.figure(b21 = (12, 6))
plt.plot(b13[test_start + 40:test_start + 140], '-', b18 = "Real Flow")
plt.plot(b23[50 - a3:50 - a3 + 100], '-x', b19 = 'red', b18="Arima-LSTM-Linear-7 Predictions")
plt.plot(b12[test_start + 40:test_start + 140], '-.', b19 = 'g', b18="LSTM Predictions")
plt.legend(b20 = 'upper right')
plt.xlabel("Period (15min)")
plt.ylabel("Traffic Volume (Vehicles/Period)")
plt.show()
plt.figure(b21 = (12, 6))
plt.plot(b36, '-', b19 = 'g', b18="Arima-LSTM-Linear-7 Error")
plt.plot(b33, '-', b19 = 'r', b18="LSTM Error")
plt.legend(b20 = 'upper right')
plt.xlabel("Period (15min)")
plt.ylabel("Traffic Volume (Vehicles/Period)")
plt.ylim(0, 120)
plt.show()