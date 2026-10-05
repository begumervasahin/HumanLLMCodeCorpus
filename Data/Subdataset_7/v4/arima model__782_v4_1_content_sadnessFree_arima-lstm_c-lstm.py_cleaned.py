
import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
from matplotlib import pyplot
def fonk1(y_true, y_pred):
    a1 = 0
    for b5 in range(len(y_true)):
        a1 += abs(y_pred[b5] - y_true[b5]) / y_true[b5]
    return a1 / len(y_true)
def fonk2(data, b1 = 1, n_out=1, dropnan=True):
    b2 = 1 if type(data) is list else data.shape[1]
    b3 = pd.DataFrame(data)
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
    b6 = pd.concat(cols, axis=1)
    b6.b7 = b4
    if dropnan:
        b6.dropna(b8 = True)
    return b6
b9 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0, index_col=0)
b10 = b9.b10[1::2].astype('float32')
b11 = MinMaxScaler(feature_range=(0, 1))
b12 = b11.fit_transform(b10)
b13 = fonk2(b12, 10, 1)
train_start, b14 = 0, 500
b15 = b13.b10[train_start:train_start + b14, :]
b16 = b13.b10[650:700, :]
b19, b17 = b15[:, :-1], b15[:, -1]
b20, b18 = b16[:, :-1], b16[:, -1]
b19 = np.reshape(b19, (b19.shape[0], 1, b19.shape[1]))
b20 = np.reshape(b20, (b20.shape[0], 1, b20.shape[1]))
b21 = Sequential()
b21.add(LSTM(50, b22 = (b19.shape[1], b19.shape[2])))
b21.add(Dense(1))
b21.compile(b23 = 'mean_squared_error', optimizer='adam')
b24 = b21.fit(b19, b17, epochs=10000, batch_size=500, validation_data=(b20, b18), verbose=2, shuffle=False)
b21.save('../b21/lstm-30min.h5')
pyplot.plot(b24.b24['b23'], b25 = 'b15')
pyplot.plot(b24.b24['val_loss'], b25 = 'b16')
pyplot.legend()
pyplot.show()
b26 = b21.predict(b20)
b20 = b20.reshape((b20.shape[0], b20.shape[2]))
b27 = b11.inverse_transform(np.concatenate((b26, b20[:, 1:]), axis=1))
b28 = b11.inverse_transform(np.concatenate((b18.reshape((len(b18), 1)), b20[:, 1:]), axis=1))
b29 = mean_squared_error(b28, b27)
b30 = math.sqrt(b29)
b31 = mean_absolute_error(b28, b27)
b32 = fonk1(b28, b27)
print(f'Test MAE: {b31:.3f} MSE: {b29:.3f} RMSE: {b30:.3f} MAPE: {b32:.3f}')
pyplot.plot(b28, b25 = 'Actual')
pyplot.plot(b27, b25 = 'Predicted')
pyplot.show(b33 = (12, 6))