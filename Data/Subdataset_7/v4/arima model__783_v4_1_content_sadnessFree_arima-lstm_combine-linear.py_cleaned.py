import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
from b30 import mean_a_p_e
from HM import hm_p
from svr import svr_test
from keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
from sklearn import linear_model
matplotlib.rcParams['font.family'] = 'SimHei'
a1 = 10
a2 = 300
a3 = 7
b1 = a2 + b30.a3 - 1
b2 = pd.read_csv('/Users/daihanru/Desktop/b30-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], engine='python', header=0, index_col=0)
b3 = b2.b3.astype('float32')
b4 = MinMaxScaler(feature_range=(0, 1))
b5 = b4.fit_transform(b3)
b6 = series_to_supervised(b5, a1, 1)
b7 = b30.start + b30.size - a1
b8 = b6.b3[b7:b7 + b30.test_size, :]
b10, b9 = b8[:, :-1], b8[:, -1]
b10 = b10.reshape((b10.shape[0], 1, b10.shape[1]))
b11 = load_model('../b25/lstm-15min.h5')
b12 = b11.predict(b10)
b10 = b10.reshape((b10.shape[0], b10.shape[2]))
b13 = b4.inverse_transform(np.concatenate((b12, b10[:, 1:]), axis=1))
b13 = b13[:, 0]
b9 = b9.reshape((len(b9), 1))
b14 = b4.inverse_transform(np.concatenate((b9, b10[:, 1:]), axis=1))
b14 = b14[:, 0]
b15 = mean_squared_error(b14[b1:], b13[b1:])
b16 = math.sqrt(mean_squared_error(b14[b1:], b13[b1:]))
b17 = mean_absolute_error(b14[b1:], b13[b1:])
b18 = b30.mean_a_p_e(b14[b1:], b13[b1:])
print('LSTM Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b17, b15, b16, b18))
plt.plot(b14[b1:], '-', b19 = "b29 flow")
plt.plot(b13[b1:], '--', b20 = 'red', b19="LSTM")
plt.legend(b21 = 'upper right')
plt.xlabel("period (15-minute intervals)")
plt.ylabel("volume (vehicle/period)")
plt.ylim(0, 800)
plt.show(b22 = (12, 6))
b23 = [(b13[i] + b30.predictions[i]) / 2 for i in range(len(b13))]
b15 = mean_squared_error(b14[b1:], b23[b1:])
b16 = math.sqrt(mean_squared_error(b14[b1:], b23[b1:]))
b17 = mean_absolute_error(b14[b1:], b23[b1:])
b18 = b30.mean_a_p_e(b14[b1:], b23[b1:])
print('EW b23 Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b17, b15, b16, b18))
b24 = []
b25 = linear_model.LinearRegression(normalize=True)
b27, b26 = [], []
for i in range(a2 - a3 + 1):
    for j in range(a3):
        b27.append(b30.predictions[i + j][0])
    for j in range(a3):
        b27.append(b13[i + j])
    b26.append(b14[i + a3 - 1])
b27 = np.array(b27).reshape(a2 - a3 + 1, 2 * a3)
b25.fit(b27, b26)
b28 = []
for i in range(b30.test_size - a2 - a3 + 1):
    for j in range(a3):
        b28.append(b30.predictions[a2 + i + j][0])
    for j in range(a3):
        b28.append(b13[a2 + i + j])
b28 = np.array(b28).reshape(b30.test_size - a2 - a3 + 1, 2 * a3)
b24 = b25.predict(b28)
b15 = mean_squared_error(b14[b1:], b24[b30.a3 - a3:])
b16 = math.sqrt(mean_squared_error(b14[b1:], b24[b30.a3 - a3:]))
b17 = mean_absolute_error(b14[b1:], b24[b30.a3 - a3:])
b18 = b30.mean_a_p_e(b14[b1:], b24[b30.a3 - a3:])
print('dyn b23 Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b17, b15, b16, b18))
plt.figure(b22 = (12, 6))
plt.plot(b14[b1:], '-', b19 = "b29 flow")
plt.plot(b24[b30.a3 - a3:], '--', b20 = 'red', b19="b30-lstm-linear-7")
plt.legend(b21 = 'upper right')
plt.xlabel("period (15-minute intervals)")
plt.ylabel("volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()
plt.figure(b22 = (12, 6))
plt.plot(b30.predictions[b1 + 40:b1 + 140], '-+', b19 = "ARIMA predictions")
plt.plot(b13[b1 + 40:b1 + 140], '-.', b19 = "LSTM predictions")
plt.plot(hm_p[40:140], '--.', b19 = 'HM predictions')
plt.plot(svr_test[40:140], '-x', b19 = 'SVR predictions')
plt.plot(b14[b1 + 40:b1 + 140], '-', b19 = "b29 flow")
plt.legend(b21 = 'upper right')
plt.xlabel("period (15min)")
plt.ylabel("traffic volume (vehicles/period)")
plt.show()
b29 = np.array(b14[b1:])
b30 = np.array(ar