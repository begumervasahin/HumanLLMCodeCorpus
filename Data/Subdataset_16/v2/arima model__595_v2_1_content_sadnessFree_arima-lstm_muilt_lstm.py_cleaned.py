import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
def fonk1(y_true, y_pred):
    a1 = 0
    for b5 in range(len(y_true)):
        a1 += abs(y_pred[b5] - y_true[b5]) / y_true[b5]
    return a1 / len(y_true)
def fonk2(b9, b1 = 1, n_out=1, dropnan=True):
    b2 = 1 if isinstance(b9, list) else b9.shape[1]
    b3 = pd.DataFrame(b9)
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
    b6 = pd.concat(cols, b14=1)
    b6.b7 = b4
    if dropnan:
        b6.dropna(b8 = True)
    return b6
b9 = pd.read_csv('path_to_your_dataset.csv', header=0, index_col=0)
b10 = b9.b10
b10 = b10.astype('float32')
b11 = MinMaxScaler(feature_range=(0, 1))
b12 = b11.fit_transform(b10)
b13 = fonk2(b12, 1, 1)
b13.drop(b13.b7[[4, 5, 6, 7]], b14 = 1, b8=True)
b10 = b13.b10
b15 = 365 * 24
b16 = b10[:b15, :]
b17 = b10[b15:, :]
b20, b18 = b16[:, :-1], b16[:, -1]
b21, b19 = b17[:, :-1], b17[:, -1]
b20 = b20.reshape((b20.shape[0], 1, b20.shape[1]))
b21 = b21.reshape((b21.shape[0], 1, b21.shape[1]))
b22 = Sequential()
b22.add(LSTM(50, b23 = (b20.shape[1], b20.shape[2])))
b22.add(Dense(1))
b22.compile(b24 = 'mae', optimizer='adam')
b25 = b22.fit(b20, b18, epochs=50, batch_size=72, validation_data=(b21, b19), verbose=2, shuffle=False)
plt.plot(b25.b25['b24'], b26 = 'b16')
plt.plot(b25.b25['val_loss'], b26 = 'b17')
plt.legend()
plt.show()
b27 = b22.predict(b21)
b21 = b21.reshape((b21.shape[0], b21.shape[2]))
b28 = np.concatenate((b27, b21[:, 1:]), b14=1)
b28 = b11.inverse_transform(b28)
b28 = b28[:, 0]
b19 = b19.reshape((len(b19), 1))
b29 = np.concatenate((b19, b21[:, 1:]), b14=1)
b29 = b11.inverse_transform(b29)
b29 = b29[:, 0]
b30 = math.sqrt(mean_squared_error(b29, b28))
print(f'Test RMSE: {b30:.3f}')
b31 = fonk1(b29, b28)
print(f'Test MAPE: {b31:.3f}')