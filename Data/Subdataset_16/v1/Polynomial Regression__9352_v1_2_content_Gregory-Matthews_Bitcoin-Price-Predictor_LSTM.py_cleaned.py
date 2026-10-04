import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as pyplot
from math import sqrt
def fonk1(data, b1 = 1, n_out=1, dropnan=True):
    b2 = 1 if type(data) is list else data.shape[1]
    b3 = pd.DataFrame(data)
    cols, b4 = list(), list()
    for b5 in range(b1, 0, -1):
        cols.append(b3.shift(b5))
        b4 += [('var%d(t-%d)' % (j+1, b5)) for j in range(b2)]
    for b5 in range(0, n_out):
        cols.append(b3.shift(-b5))
        if b5 = = 0:
            b4 += [('var%d(t)' % (j+1)) for j in range(b2)]
        else:
            b4 += [('var%d(t+%d)' % (j+1, b5)) for j in range(b2)]
    b6 = pd.concat(cols, b14=1)
    b6.b7 = b4
    if dropnan:
        b6.dropna(b8 = True)
    return b6
b9 = pd.read_csv('ReducedFeatureSet.csv', header=0, index_col=0)
b10 = b9.b10
b10 = b10.astype('float32')
b11 = MinMaxScaler(feature_range=(0, 1))
b12 = b11.fit_transform(b10)
b13 = fonk1(b12, 1, 1)
b13.drop(b13.b7[[6, 7, 8, 9]], b14 = 1, b8=True)
b10 = b13.b10
b15 = 365*2 + (365 - 30)
b16 = b10[:b15, :]
b17 = b10[b15:, :]
b20, b18 = b16[:, :-1], b16[:, -1]
b21, b19 = b17[:, :-1], b17[:, -1]
b20 = b20.reshape((b20.shape[0], 1, b20.shape[1]))
b21 = b21.reshape((b21.shape[0], 1, b21.shape[1]))
b22 = Sequential()
b22.add(LSTM(300, b23 = (b20.shape[1], b20.shape[2])))
b22.add(Dense(1))
b22.compile(b24 = 'mae', optimizer='adam')
b25 = b22.fit(b20, b18, epochs=100, batch_size=50, validation_data=(b21, b19), verbose=2, shuffle=False)
pyplot.plot(b25.b25['b24'], b26 = 'b16')
pyplot.plot(b25.b25['val_loss'], b26 = 'b17')
pyplot.legend()
pyplot.title('RNN Fitting')
pyplot.xlabel('Epochs', b27 = 16)
pyplot.ylabel('Value Loss', b27 = 16)
pyplot.show()
b28 = b22.predict(b21)
b21 = b21.reshape((b21.shape[0], b21.shape[2]))
b29 = np.concatenate((b28, b21[:, 1:]), b14=1)
b29 = b11.inverse_transform(b29)
b29 = b29[:, 0]
b19 = b19.reshape((len(b19), 1))
b30 = np.concatenate((b19, b21[:, 1:]), b14=1)
b30 = b11.inverse_transform(b30)
b30 = b30[:, 0]
pyplot.plot(b30, b31 = 'o', linestyle='-', color='b', b26='Actual Price')
pyplot.plot(b29, b31 = 'o', linestyle='-', color='r', b26='Forecasted Price using LSTM RNN')
pyplot.legend()
pyplot.title("Testing over past 30 days")
pyplot.xlabel('Days', b27 = 18)
pyplot.ylabel('Bitcoin Price ($)', b27 = 16)
pyplot.show()
b32 = sqrt(mean_squared_error(b30, b29))
print('Test RMSE: %.3f' % b32)