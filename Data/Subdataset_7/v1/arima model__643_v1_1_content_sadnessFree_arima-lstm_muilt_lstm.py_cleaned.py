import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
def fonk1(y_true, y_pred):
    return np.mean(np.abs((y_pred - y_true) / y_true)) * 100
def fonk2(data, b1 = 1, n_out=1, dropnan=True):
    b2 = 1 if isinstance(data, list) else data.shape[1]
    b3 = pd.DataFrame(data)
    cols, b4 = [], []
    for b5 in range(b1, 0, -1):
        cols.append(b3.shift(b5))
        b4 += [('var%d(t-%d)' % (j+1, b5)) for j in range(b2)]
    for b5 in range(0, n_out):
        cols.append(b3.shift(-b5))
        if b5 = = 0:
            b4 += [('var%d(t)' % (j+1)) for j in range(b2)]
        else:
            b4 += [('var%d(t+%d)' % (j+1, b5)) for j in range(b2)]
    b6 = pd.concat(cols, b11=1)
    b6.b7 = b4
    if dropnan:
        b6.dropna(b8 = True)
    return b6
b9 = pd.read_csv('your_dataset.csv')
a1 = 1
a2 = 1
b10 = fonk2(b9, a1, 1)
b10.drop(b10.b7[-a2:], b11 = 1, b8=True)
b12 = b10.b12
b13 = int(len(b12) * 0.7)
b14 = b12[:b13, :]
b15 = b12[b13:, :]
b18, b16 = b14[:, :-1], b14[:, -1]
b19, b17 = b15[:, :-1], b15[:, -1]
b18 = b18.reshape((b18.shape[0], 1, b18.shape[1]))
b19 = b19.reshape((b19.shape[0], 1, b19.shape[1]))
b20 = Sequential()
b20.add(LSTM(50, b21 = (b18.shape[1], b18.shape[2])))
b20.add(Dense(1))
b20.compile(b22 = 'mae', optimizer='adam')
b23 = b20.fit(b18, b16, epochs=50, batch_size=72, validation_data=(b19, b17), verbose=2, shuffle=False)
b24 = b20.predict(b19)
b19 = b19.reshape((b19.shape[0], b19.shape[2]))
b25 = np.concatenate((b24, b19[:, 1:]), b11=1)
b26 = fonk1(b17, b24)
print('Test MAPE: %.3f' % b26)
plt.plot(b23.b23['b22'])
plt.plot(b23.b23['val_loss'])
plt.title('Model b22')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], b27 = 'upper left')
plt.show()