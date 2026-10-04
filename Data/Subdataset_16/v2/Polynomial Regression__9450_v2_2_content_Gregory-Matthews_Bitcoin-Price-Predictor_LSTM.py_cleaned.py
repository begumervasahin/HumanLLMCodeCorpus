import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from math import sqrt
def fonk1(data, b1 = 1, n_out=1, dropnan=True):
    b2 = data.shape[1] if isinstance(data, np.ndarray) else 1
    b3 = pd.DataFrame(data)
    cols, b4 = [], []
    for b5 in range(b1, 0, -1):
        cols.append(b3.shift(b5))
        b4 += [f'var{j+1}(t-{b5})' for j in range(b2)]
    for b5 in range(n_out):
        cols.append(b3.shift(-b5))
        if b5 = = 0:
            b4 += [f'var{j+1}(t)' for j in range(b2)]
        else:
            b4 += [f'var{j+1}(t+{b5})' for j in range(b2)]
    b6 = pd.concat(cols, b14=1)
    b6.b7 = b4
    if dropnan:
        b6.dropna(b8 = True)
    return b6
b9 = pd.read_csv('ReducedFeatureSet.csv', header=0, index_col=0)
b10 = b9.b10.astype('float32')
b11 = MinMaxScaler(feature_range=(0, 1))
b12 = b11.fit_transform(b10)
b13 = fonk1(b12, 1, 1)
b13.drop(b13.b7[[6, 7, 8, 9]], b14 = 1, b8=True)
b10 = b13.b10
b15 = 365*2 + (365 - 30)
train, b16 = b10[:b15, :], b10[b15:, :]
b19, b17 = train[:, :-1], train[:, -1]
b20, b18 = b16[:, :-1], b16[:, -1]
b19 = b19.reshape((b19.shape[0], 1, b19.shape[1]))
b20 = b20.reshape((b20.shape[0], 1, b20.shape[1]))
b21 = Sequential()
b21.add(LSTM(300, b22 = (b19.shape[1], b19.shape[2])))
b21.add(Dense(1))
b21.compile(b23 = 'mae', optimizer='adam')
b24 = b21.fit(b19, b17, epochs=100, batch_size=50, validation_data=(b20, b18), verbose=2, shuffle=False)
plt.plot(b24.b24['b23'], b25 = 'train')
plt.plot(b24.b24['val_loss'], b25 = 'b16')
plt.legend()
plt.title('RNN Fitting')
plt.xlabel('Epochs', b26 = 16)
plt.ylabel('Value Loss', b26 = 16)
plt.show()
b27 = b21.predict(b20)
b20 = b20.reshape((b20.shape[0], b20.shape[1]))
b28 = np.concatenate((b27, b20[:, 1:]), b14=1)
b28 = b11.inverse_transform(b28)
b28 = b28[:, 0]
b18 = b18.reshape((len(b18), 1))
b29 = np.concatenate((b18, b20[:, 1:]), b14=1)
b29 = b11.inverse_transform(b29)
b29 = b29[:, 0]
plt.plot(b29, b30 = 'o', linestyle='-', color='b', b25='Actual Price')
plt.plot(b28, b30 = 'o', linestyle='-', color='r', b25='Forecasted Price using LSTM RNN')
plt.legend()
plt.title("Testing over past 30 days")
plt.xlabel('Days', b26 = 18)
plt.ylabel('Bitcoin Price ($)', b26 = 16)
plt.show()
b31 = sqrt(mean_squared_error(b29, b28))
print(f'Test RMSE: {b31:.3f}')