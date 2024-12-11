import pandas
import numpy
import math
import matplotlib.pyplot as plt
import arima
from keras.models import load_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
a1 = 10
b1 = pandas.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], engine='python',
                            b2 = 0, index_col=0)
b3 = b1.b3
b3 = b3.astype('float32')
b4 = MinMaxScaler(feature_range=(0, 1))
b5 = b4.fit_transform(b3)
b6 = series_to_supervised(b5, a1, 1)
print(b6.head())
b3 = b6.b3
b7 = arima.start + arima.size - a1
b8 = b3[b7:b7 + arima.test_size, :]
b10, b9 = b8[:, :-1], b8[:, -1]
b10 = b10.reshape((b10.shape[0], 1, b10.shape[1]))
print(b10.shape, b9.shape)
b11 = load_model('../model/lstm-15min.h5')
b12 = b11.predict(b10)
b10 = b10.reshape((b10.shape[0], b10.shape[2]))
b13 = numpy.concatenate((b12, b10[:, 1:]), axis=1)
b13 = b4.inverse_transform(b13)
b13 = b13[:, 0]
b9 = b9.reshape((len(b9), 1))
b14 = numpy.concatenate((b9, b10[:, 1:]), axis=1)
b14 = b4.inverse_transform(b14)
b14 = b14[:, 0]
b15 = mean_squared_error(b14[arima.test_start:], b13[arima.test_start:])
b16 = math.sqrt(mean_squared_error(b14[arima.test_start:], b13[arima.test_start:]))
b17 = mean_absolute_error(b14[arima.test_start:], b13[arima.test_start:])
b18 = arima.mean_a_p_e(b14[arima.test_start:], b13[arima.test_start:])
print('LSTM Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b17, b15, b16, b18))
plt.plot(b14[arima.test_start:], '-', b19 = "real flow")
plt.plot(b13[arima.test_start:], '--', b20 = 'red', b19="LSTM")
plt.legend(b21 = 'upper right')
plt.xlabel("period(15-minute intervals)")
plt.ylabel("volume(vehicle/period)")
plt.ylim(0, 800)
plt.show(b22 = (12, 6))
b23 = list()
for i in range(len(b13)):
    b23.append((b13[i] + arima.predictions[i]) / 2)
b15 = mean_squared_error(b14[arima.test_start:], b23[arima.test_start:])
b16 = math.sqrt(mean_squared_error(b14[arima.test_start:], b23[arima.test_start:]))
b17 = mean_absolute_error(b14[arima.test_start:], b23[arima.test_start:])
b18 = arima.mean_a_p_e(b14[arima.test_start:], b23[arima.test_start:])
print('EW b23 Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b17, b15, b16, b18))
a2 = 1
b24 = []
b25 = []
a3 = 1
a4 = 1
b26 = list()
for i in range(len(b13)):
    if len(b24) > 0:
        b27 = math.pow(numpy.sum(b24[-a2:]), 1 / 2) / math.pow(a2, 1 / 2)
        b28 = math.pow(numpy.sum(b25[-a2:]), 1 / 2) / math.pow(a2, 1 / 2)
        a3 = (1 - b27 / (b27 + b28)) * 2
        a4 = 2 - a3
    b24.append(math.pow(b13[i] - b14[i], 2))
    b25.append(math.pow(arima.predictions[i] - b14[i], 2))
    b26.append((a3 * b13[i] + a4 * arima.predictions[i]) / 2)
b15 = mean_squared_error(b14[arima.test_start:], b26[arima.test_start:])
b16 = math.sqrt(mean_squared_error(b14[arima.test_start:], b26[arima.test_start:]))
b17 = mean_absolute_error(b14[arima.test_start:], b26[arima.test_start:])
b18 = arima.mean_a_p_e(b14[arima.test_start:], b26[arima.test_start:])
print('dyn b23 Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b17, b15, b16, b18))
plt.figure()
plt.plot(b14[arima.test_start:], '-', b19 = "real flow")
plt.plot(b26[arima.test_start:], '--', b20 = 'red', b19="b23")
plt.legend(b21 = 'upper right')
plt.xlabel("period(15-minute intervals)")
plt.ylabel("volume(vehicle/period)")
plt.ylim(0, 800)
plt.show(b22 = (12, 6))