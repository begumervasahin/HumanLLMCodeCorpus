import pandas
import numpy
import math
import matplotlib.pyplot as plt
import matplotlib
import b31
from HM import hm_p
from svr import svr_test
from keras.models import load_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
from sklearn import linear_model
matplotlib.rcParams['font.family'] = 'SimHei'
a1 = 10
a2 = 300
a3 = 7
b1 = a2 + b31.a3 - 1
b2 = pandas.read_csv('/Users/daihanru/Desktop/b31-b32/DataSet/FEB15-2.csv', usecols=[2, 3], engine='python',
                            b3 = 0, index_col=0)
b4 = b2.b4
b4 = b4.astype('float32')
b5 = MinMaxScaler(feature_range=(0, 1))
b6 = b5.fit_transform(b4)
b7 = series_to_supervised(b6, a1, 1)
print(b7.head())
b4 = b7.b4
b8 = b31.start + b31.size - a1
b9 = b4[b8:b8 + b31.test_size, :]
b11, b10 = b9[:, :-1], b9[:, -1]
b11 = b11.reshape((b11.shape[0], 1, b11.shape[1]))
print(b11.shape, b10.shape)
b12 = load_model('../b26/b32-15min.h5')
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
b19 = b31.mean_a_p_e(b15[b1:], b14[b1:])
print('LSTM Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b18, b16, b17, b19))
plt.plot(b15[b1:], '-', b20 = "b30 flow")
plt.plot(b14[b1:], '--', b21 = 'red', b20="LSTM")
plt.legend(b22 = 'upper right')
plt.xlabel("period(15-minute intervals)")
plt.ylabel("volume(vehicle/period)")
plt.ylim(0, 800)
plt.show(b23 = (12, 6))
b24 = list()
for i in range(len(b14)):
    b24.append((b14[i] + b31.predictions[i]) / 2)
b16 = mean_squared_error(b15[b1:], b24[b1:])
b17 = math.sqrt(mean_squared_error(b15[b1:], b24[b1:]))
b18 = mean_absolute_error(b15[b1:], b24[b1:])
b19 = b31.mean_a_p_e(b15[b1:], b24[b1:])
print('EW b24 Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b18, b16, b17, b19))
b25 = list()
b26 = linear_model.LinearRegression(normalize=True)
b27 = []
b28 = []
for i in range(a2 - a3 + 1):
    for j in range(a3):
        b27.append(b31.predictions[i + j][0])
    for j in range(a3):
        b27.append(b14[i + j])
    b28.append(b15[i + a3 - 1])
b27 = numpy.array(b27).reshape(a2 - a3 + 1, 2 * a3)
b26.fit(b27, b28)
b29 = []
for i in range(b31.test_size - a2 - a3 + 1):
    for j in range(a3):
        b29.append(b31.predictions[a2 + i + j][0])
    for j in range(a3):
        b29.append(b14[a2 + i + j])
b29 = numpy.array(b29).reshape(b31.test_size - a2 - a3 + 1,
                                               2 * a3)
b25 = b26.predict(b29)
b16 = mean_squared_error(b15[b1:], b25[b31.a3 - a3:])
b17 = math.sqrt(mean_squared_error(b15[b1:], b25[b31.a3 - a3:]))
b18 = mean_absolute_error(b15[b1:], b25[b31.a3 - a3:])
b19 = b31.mean_a_p_e(b15[b1:], b25[b31.a3 - a3:])
print('dyn b24 Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b18, b16, b17, b19))
plt.figure(b23 = (12, 6))
plt.plot(b15[b1:], '-', b20 = "b30 flow")
plt.plot(b25[b31.a3 - a3:], '--', b21 = 'red', b20="b31-b32-linear-7")
plt.legend(b22 = 'upper right')
plt.xlabel("period(15-minute intervals)")
plt.ylabel("volume(vehicle/period)")
plt.ylim(0, 800)
plt.show()
plt.figure(b23 = (12, 6))
plt.plot(b31.predictions[b1 + 40:b1 + 140], '-+', b20 = "ARIMAé¢æµç»æ")
plt.plot(b14[b1 + 40:b1 + 140], '-.', b20 = "LSTMé¢æµç»æ")
plt.plot(hm_p[40:140], '--.', b20 = 'HMé¢æµç»æ')
plt.plot(svr_test[40:140], '-x', b20 = 'SVRé¢æµç»æ')
plt.plot(b15[b1 + 40:b1 + 140], '-', b20 = "çå®æµé")
plt.legend(b22 = 'upper right')
plt.xlabel("å¨æ(15min)")
plt.ylabel("è½¦æµé(è½¦è¾æ°/å¨æï¼")
plt.show()
b30 = numpy.array(b15[b1:])
b31 = numpy.array(b31.predictions[b1:])
b32 = numpy.array(b14[b1:])
b33 = numpy.array(b25[10 - a3:])
b34 = list()
b35 = list()
b36 = list()
b37 = list()
b38 = list()
for i in range(40, 140):
    b34.append(math.fabs(b31[i] - b30[i]))
    b35.append(math.fabs(b32[i] - b30[i]))
    b36.append(math.fabs(hm_p[i] - b30[i]))
    b37.append(math.fabs(svr_test[i] - b30[i]))
    b38.append(math.fabs(b33[i] - b30[i]))
plt.figure(b23 = (12, 6))
plt.plot(b34, '-', b20 = "ARIMA è¯¯å·®")
plt.plot(b35, '-', b21 = 'r', b20="LSTM è¯¯å·®")
plt.plot(b36, '-', b21 = 'g', b20="HM è¯¯å·®")
plt.plot(b37, '-', b20 = "SVR è¯¯å·®")
plt.legend(b22 = 'upper right')
plt.xlabel("å¨æ(15min)")
plt.ylabel("è½¦æµé(è½¦è¾æ°/å¨æï¼")
plt.ylim(0, 250)
plt.show()
plt.figure(b23 = (12, 6))
plt.plot(b15[b1 + 40:b1 + 140], '-', b20 = "çå®æµé")
plt.plot(b25[50 - a3:50 - a3 + 100], '-x', b21 = 'red',
         b20 = "b31-b32-linear-7é¢æµç»æ")
plt.plot(b14[b1 + 40:b1 + 140], '-.', b21 = 'g', b20="LSTMé¢æµç»æ")
plt.legend(b22 = 'upper right')
plt.xlabel("å¨æ(15min)")
plt.ylabel("è½¦æµé(è½¦è¾æ°/å¨æï¼")
plt.show()
plt.figure(b23 = (12, 6))
plt.plot(b38, '-', b21 = 'g', b20="b31-b32-linear-7 è¯¯å·®")
plt.plot(b35, '-', b21 = 'r', b20="LSTM è¯¯å·®")
plt.legend(b22 = 'upper right')
plt.xlabel("å¨æ(15min)")
plt.ylabel("è½¦æµé(è½¦è¾æ°/å¨æï¼")
plt.ylim(0, 120)
plt.show()