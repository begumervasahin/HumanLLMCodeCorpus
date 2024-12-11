from math import sqrt
import math
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import numpy
def fonk1(y_true, y_pred):
    a1 = 0
    for b5 in range(len(y_true)):
        a1 += math.fabs(y_pred[b5] - y_true[b5]) / y_true[b5]
    return a1 / len(y_true)
def fonk2(data, b1 = 1, n_out=1, dropnan=True):
    b2 = 1 if type(data) is list else data.shape[1]
    b3 = DataFrame(data)
    cols, b4 = list(), list()
    for b5 in range(b1, 0, -1):
        cols.append(b3.shift(b5))
        b4 += [('var%d(t-%d)' % (j + 1, b5)) for j in range(b2)]
    for b5 in range(0, n_out):
        cols.append(b3.shift(-b5))
        if b5 = = 0:
            b4 += [('var%d(t)' % (j + 1)) for j in range(b2)]
        else:
            b4 += [('var%d(t+%d)' % (j + 1, b5)) for j in range(b2)]
    b6 = concat(cols, axis=1)
    b6.b7 = b4
    if dropnan:
        b6.dropna(b8 = True)
    return b6
b9 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0,
                   b10 = 0)
b11 = b9.b11[1::2]
b11 = b11.astype('float32')
b12 = MinMaxScaler(feature_range=(0, 1))
b13 = b12.fit_transform(b11)
b14 = fonk2(b13, 10, 1)
print(b14.head())
b11 = b14.b11
a2 = 0
a3 = 500
b15 = b11[a2:a2 + a3, :]
b16 = b11[650:700, :]
b19, b17 = b15[:, :-1], b15[:, -1]
b20, b18 = b16[:, :-1], b16[:, -1]
b19 = b19.reshape((b19.shape[0], 1, b19.shape[1]))
b20 = b20.reshape((b20.shape[0], 1, b20.shape[1]))
print(b19.shape, b17.shape, b20.shape, b18.shape)
b21 = Sequential()
b21.add(LSTM(50, b22 = (b19.shape[1], b19.shape[2])))
b21.add(Dense(1))
b21.compile(b23 = 'mean_squared_error', optimizer='adam')
b24 = b21.fit(b19, b17, epochs=10000, batch_size=500, validation_data=(b20, b18), verbose=2,
                    b25 = False)
b21.save('../b21/lstm-30min.h5')
pyplot.plot(b24.b24['b23'], b26 = 'b15')
pyplot.plot(b24.b24['val_loss'], b26 = 'b16')
pyplot.legend()
pyplot.show()
b27 = b21.predict(b20)
b20 = b20.reshape((b20.shape[0], b20.shape[2]))
b28 = concatenate((b27, b20[:, 1:]), axis=1)
b28 = b12.inverse_transform(b28)
b28 = b28[:, 0]
b18 = b18.reshape((len(b18), 1))
b29 = concatenate((b18, b20[:, 1:]), axis=1)
b29 = b12.inverse_transform(b29)
b29 = b29[:, 0]
b30 = mean_squared_error(b29, b28)
b31 = math.sqrt(mean_squared_error(b29, b28))
b32 = mean_absolute_error(b29, b28)
b33 = fonk1(b29, b28)
print('Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b32, b30, b31, b33))
pyplot.plot(b29)
pyplot.plot(b28)
pyplot.show(b34 = (12, 6))