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
b9 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0, index_col=0)
b10 = b9.b10[1::2]
b10 = b10.astype('float32')
b11 = MinMaxScaler(feature_range=(0, 1))
b12 = b11.fit_transform(b10)
b13 = fonk2(b12, 10, 1)
a2 = 0
a3 = 500
b14 = b13.b10[a2:a2 + a3, :]
b15 = b13.b10[650:700, :]
b18, b16 = b14[:, :-1], b14[:, -1]
b19, b17 = b15[:, :-1], b15[:, -1]
b18 = b18.reshape((b18.shape[0], 1, b18.shape[1]))
b19 = b19.reshape((b19.shape[0], 1, b19.shape[1]))
b20 = Sequential()
b20.add(LSTM(50, b21 = (b18.shape[1], b18.shape[2])))
b20.add(Dense(1))
b20.compile(b22 = 'mean_squared_error', optimizer='adam')
b23 = b20.fit(b18, b16, epochs=10000, batch_size=500, validation_data=(b19, b17), verbose=2, shuffle=False)
b20.save('../b20/lstm-30min.h5')
pyplot.plot(b23.b23['b22'], b24 = 'b14')
pyplot.plot(b23.b23['val_loss'], b24 = 'b15')
pyplot.legend()
pyplot.show()
b25 = b20.predict(b19)
b19 = b19.reshape((b19.shape[0], b19.shape[2]))
b26 = concatenate((b25, b19[:, 1:]), axis=1)
b26 = b11.inverse_transform(b26)
b26 = b26[:, 0]
b17 = b17.reshape((len(b17), 1))
b27 = concatenate((b17, b19[:, 1:]), axis=1)
b27 = b11.inverse_transform(b27)
b27 = b27[:, 0]
b28 = mean_squared_error(b27, b26)
b29 = sqrt(b28)
b30 = mean_absolute_error(b27, b26)
b31 = fonk1(b27, b26)
print('Test MAE: %.3f, MSE: %.3f, RMSE: %.3f, MAPE: %.3f' % (b30, b28, b29, b31))
pyplot.plot(b27, b24 = 'Actual')
pyplot.plot(b26, b24 = 'Predicted')
pyplot.legend()
pyplot.show()