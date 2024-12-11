
import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
def fonk1(y_true, y_pred):
    b1 = np.abs(y_pred - y_true)
    b2 = b1 / y_true
    return np.mean(b2)
def fonk2(data, b3 = 1, n_out=1, dropnan=True):
    b4 = 1 if isinstance(data, list) else data.shape[1]
    b5 = pd.DataFrame(data)
    cols, b6 = [], []
    for b7 in range(b3, 0, -1):
        cols.append(b5.shift(b7))
        b6 += [f'var{j + 1}(t-{b7})' for j in range(b4)]
    for b7 in range(0, n_out):
        cols.append(b5.shift(-b7))
        if b7 = = 0:
            b6 += [f'var{j + 1}(t)' for j in range(b4)]
        else:
            b6 += [f'var{j + 1}(t+{b7})' for j in range(b4)]
    b8 = pd.concat(cols, axis=1)
    b8.b9 = b6
    if dropnan:
        b8.dropna(b10 = True)
    return b8
b11 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b12 = pd.read_csv(b11, usecols=[2, 3], header=0, index_col=0)
b13 = b12.b13[1::2].astype('float32')
b14 = MinMaxScaler(feature_range=(0, 1))
b15 = b14.fit_transform(b13)
b16 = fonk2(b15, 10, 1)
train_start, b17 = 0, 500
b18 = b16.b13[train_start:train_start + b17, :]
b19 = b16.b13[650:700, :]
b22, b20 = b18[:, :-1], b18[:, -1]
b23, b21 = b19[:, :-1], b19[:, -1]
b22 = np.reshape(b22, (b22.shape[0], 1, b22.shape[1]))
b23 = np.reshape(b23, (b23.shape[0], 1, b23.shape[1]))
b24 = Sequential()
b24.add(LSTM(50, b25 = (b22.shape[1], b22.shape[2])))
b24.add(Dense(1))
b24.compile(b26 = 'mean_squared_error', optimizer='adam')
b27 = b24.fit(b22, b20, epochs=10000, batch_size=500, validation_data=(b23, b21), verbose=2, shuffle=False)
b24.save('../b24/lstm-30min.h5')
plt.plot(b27.b27['b26'], b28 = 'Train Loss')
plt.plot(b27.b27['val_loss'], b28 = 'Validation Loss')
plt.legend()
plt.show()
b29 = b24.predict(b23)
b23 = b23.reshape((b23.shape[0], b23.shape[2]))
b30 = b14.inverse_transform(np.concatenate((b29, b23[:, 1:]), axis=1))
b31 = b14.inverse_transform(np.concatenate((b21.reshape((len(b21), 1)), b23[:, 1:]), axis=1))
b32 = mean_squared_error(b31, b30)
b33 = math.sqrt(b32)
b34 = mean_absolute_error(b31, b30)
b35 = fonk1(b31, b30)
print(f'Test MAE: {b34:.3f} MSE: {b32:.3f} RMSE: {b33:.3f} MAPE: {b35:.3f}')
plt.plot(b31, b28 = 'Actual')
plt.plot(b30, b28 = 'Predicted')
plt.show(b36 = (12, 6))