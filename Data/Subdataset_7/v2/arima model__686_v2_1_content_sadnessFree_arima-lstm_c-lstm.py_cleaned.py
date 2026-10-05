
from math import fabs, sqrt
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
def fonk1(y_true, y_pred):
    b1 = np.sum(np.abs(y_pred - y_true) / y_true)
    return b1 / len(y_true)
def fonk2(data, b2 = 1, n_out=1, dropnan=True):
    b3 = 1 if isinstance(data, list) else data.shape[1]
    b4 = pd.DataFrame(data)
    cols, b5 = [], []
    for b6 in range(b2, 0, -1):
        cols.append(b4.shift(b6))
        b5 += [('var%d(t-%d)' % (j + 1, b6)) for j in range(b3)]
    for b6 in range(0, n_out):
        cols.append(b4.shift(-b6))
        if b6 = = 0:
            b5 += [('var%d(t)' % (j + 1)) for j in range(b3)]
        else:
            b5 += [('var%d(t+%d)' % (j + 1, b6)) for j in range(b3)]
    b7 = pd.concat(cols, axis=1)
    b7.b8 = b5
    if dropnan:
        b7.dropna(b9 = True)
    return b7
b10 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0, index_col=0)
b11 = b10.b11[1::2]
b11 = b11.astype('float32')
b12 = MinMaxScaler(feature_range=(0, 1))
b13 = b12.fit_transform(b11)
b14 = fonk2(b13, 10, 1)
train_start, b15 = 0, 500
b16 = b14.b11[train_start:train_start + b15, :]
b17 = b14.b11[650:700, :]
b20, b18 = b16[:, :-1], b16[:, -1]
b21, b19 = b17[:, :-1], b17[:, -1]
b20 = b20.reshape((b20.shape[0], 1, b20.shape[1]))
b21 = b21.reshape((b21.shape[0], 1, b21.shape[1]))
b22 = Sequential()
b22.add(LSTM(50, b23 = (b20.shape[1], b20.shape[2])))
b22.add(Dense(1))
b22.compile(b24 = 'mean_squared_error', optimizer='adam')
b25 = b22.fit(b20, b18, epochs=10000, batch_size=500, validation_data=(b21, b19), verbose=2, shuffle=False)
b22.save('../b22/lstm-30min.h5')
plt.plot(b25.b25['b24'], b26 = 'b16')
plt.plot(b25.b25['val_loss'], b26 = 'b17')
plt.legend()
plt.show()
b27 = b22.predict(b21)
b21 = b21.reshape((b21.shape[0], b21.shape[2]))
b28 = concatenate((b27, b21[:, 1:]), axis=1)
b28 = b12.inverse_transform(b28)
b28 = b28[:, 0]
b19 = b19.reshape((len(b19), 1))
b29 = concatenate((b19, b21[:, 1:]), axis=1)
b29 = b12.inverse_transform(b29)
b29 = b29[:, 0]
b30 = mean_squared_error(b29, b28)
b31 = sqrt(b30)
b32 = mean_absolute_error(b29, b28)
b33 = fonk1(b29, b28)
print(f'Test MAE: {b32:.3f}, MSE: {b30:.3f}, RMSE: {b31:.3f}, MAPE: {b33:.3f}')
plt.plot(b29, b26 = 'Actual')
plt.plot(b28, b26 = 'Predicted')
plt.legend()
plt.show()