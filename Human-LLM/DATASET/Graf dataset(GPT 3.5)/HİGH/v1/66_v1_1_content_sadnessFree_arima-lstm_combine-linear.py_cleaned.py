import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
from sklearn.metrics import mean_squared_error, mean_absolute_error
from HM import hm_p
from svr import svr_test
from keras.models import load_model
from sklearn import linear_model
plt.rcParams['font.family'] = 'SimHei'
a1 = 10
a2 = 300
a3 = 7
b1 = a2 + arima.a3 - 1
b2 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3],
                        b3 = 'python', header=0, index_col=0)
b4 = b2.b4
b4 = b4.astype('float32')
b5 = MinMaxScaler(feature_range=(0, 1))
b6 = b5.fit_transform(b4)
b7 = series_to_supervised(b6, a1, 1)
b4 = b7.b4
b8 = arima.start + arima.size - a1
b9 = b4[b8:b8 + arima.test_size, :]
b11, b10 = b9[:, :-1], b9[:, -1]
b11 = b11.reshape((b11.shape[0], 1, b11.shape[1]))
b12 = load_model('../b26/lstm-15min.h5')
b13 = b12.predict(b11)
b11 = b11.reshape((b11.shape[0], b11.shape[2]))
b14 = np.concatenate((b13, b11[:, 1:]), axis=1)
b14 = b5.inverse_transform(b14)
b14 = b14[:, 0]
b10 = b10.reshape((len(b10), 1))
b15 = np.concatenate((b10, b11[:, 1:]), axis=1)
b15 = b5.inverse_transform(b15)
b15 = b15[:, 0]
b16 = mean_squared_error(b15[b1:], b14[b1:])
b17 = math.sqrt(mean_squared_error(b15[b1:], b14[b1:]))
b18 = mean_absolute_error(b15[b1:], b14[b1:])
b19 = arima.mean_a_p_e(b15[b1:], b14[b1:])
print('LSTM Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b18, b16, b17, b19))
plt.plot(b15[b1:], '-', b20 = "real flow")
plt.plot(b14[b1:], '--', b21 = 'red', b20="LSTM")
plt.legend(b22 = 'upper right')
plt.xlabel("period(15-minute intervals)")
plt.ylabel("volume(vehicle/period)")
plt.ylim(0, 800)
plt.show(b23 = (12, 6))
b24 = [(b14[i] + arima.predictions[i]) / 2 for i in range(len(b14))]
b16 = mean_squared_error(b15[b1:], b24[b1:])
b17 = math.sqrt(mean_squared_error(b15[b1:], b24[b1:]))
b18 = mean_absolute_error(b15[b1:], b24[b1:])
b19 = arima.mean_a_p_e(b15[b1:], b24[b1:])
print('EW b24 Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b18, b16, b17, b19))
b25 = []
b26 = linear_model.LinearRegression(normalize=True)
b27 = []
b28 = []
plt.show()