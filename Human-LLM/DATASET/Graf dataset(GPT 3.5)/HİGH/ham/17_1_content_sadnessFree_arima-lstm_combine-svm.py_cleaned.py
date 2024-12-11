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
from sklearn import svm
from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor
a1 = 10
a2 = 300
a3 = 5
b1 = a2 + a3 - 1
b2 = pandas.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], engine='python',
                            b3 = 0, index_col=0)
b4 = b2.b4
b4 = b4.astype('float32')
b5 = MinMaxScaler(feature_range=(0, 1))
b6 = b5.fit_transform(b4)
b7 = series_to_supervised(b6, a1, 1)
print(b7.head())
b4 = b7.b4
b8 = arima.start + arima.size - a1
b9 = b4[b8:b8 + arima.test_size, :]
b11, b10 = b9[:, :-1], b9[:, -1]
b11 = b11.reshape((b11.shape[0], 1, b11.shape[1]))
print(b11.shape, b10.shape)
b12 = load_model('../b26/lstm-15min.h5')
b13 = b12.predict(b11)
b11 = b11.reshape((b11.shape[0], b11.shape[2]))
b14 = numpy.concatenate((b13, b11[:, 1:]), axis=1)
b14 = b5.inverse_transform(b14)
b14 = b14[:, 0]
b10 = b10.reshape((len(b10), 1))
b15 = numpy.concatenate((b10, b11[:, 1:]), axis=1)
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
b24 = list()
for i in range(len(b14)):
    b24.append((b14[i] + arima.predictions[i]) / 2)
b16 = mean_squared_error(b15[b1:], b24[b1:])
b17 = math.sqrt(mean_squared_error(b15[b1:], b24[b1:]))
b18 = mean_absolute_error(b15[b1:], b24[b1:])
b19 = arima.mean_a_p_e(b15[b1:], b24[b1:])
print('EW b24 Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b18, b16, b17, b19))
b25 = list()
b26 = GradientBoostingRegressor()
b27 = []
b28 = []
for i in range(a2 - a3 + 1):
    for j in range(a3):
        b27.append(arima.predictions[i + j][0])
    for j in range(a3):
        b27.append(b14[i + j])
    b28.append(b15[i + a3 - 1])
b27 = numpy.array(b27).reshape(a2 - a3 + 1, 2 * a3)
b26.fit(b27, b28)
b29 = []
for i in range(arima.test_size - a2 - a3 + 1):
    for j in range(a3):
        b29.append(arima.predictions[a2 + i + j][0])
    for j in range(a3):
        b29.append(b14[a2 + i + j])
b29 = numpy.array(b29).reshape(arima.test_size - a2 - a3 + 1,
                                               2 * a3)
b25 = b26.predict(b29)
b16 = mean_squared_error(b15[b1:], b25)
b17 = math.sqrt(mean_squared_error(b15[b1:], b25))
b18 = mean_absolute_error(b15[b1:], b25)
b19 = arima.mean_a_p_e(b15[b1:], b25)
print('dyn b24 Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b18, b16, b17, b19))
plt.figure()
plt.plot(b15[b1:], '-', b20 = "real flow")
plt.plot(b25, '--', b21 = 'red', b20="b24")
plt.legend(b22 = 'upper right')
plt.xlabel("period(15-minute intervals)")
plt.ylabel("volume(vehicle/period)")
plt.ylim(0, 800)
plt.show(b23 = (12, 6))