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
def fonk2(b30):
    b9 = pd.read_csv(b30, header=0, index_col=0)
    b10 = b9.b10.astype('float32')
    b11 = MinMaxScaler(feature_range=(0, 1))
    b12 = b11.fit_transform(b10)
    b13 = fonk1(b12, 1, 1)
    b13.drop(b13.b7[[6, 7, 8, 9]], b14 = 1, b8=True)
    return b13, b11
def fonk3(b13, b31):
    b10 = b13.b10
    train, b15 = b10[:b31, :], b10[b31:, :]
    b18, b16 = train[:, :-1], train[:, -1]
    b19, b17 = b15[:, :-1], b15[:, -1]
    b18 = b18.reshape((b18.shape[0], 1, b18.shape[1]))
    b19 = b19.reshape((b19.shape[0], 1, b19.shape[1]))
    return b18, b16, b19, b17
def fonk4(b18, b16, b19, b17, b20 = 100, batch_size=50):
    b21 = Sequential()
    b21.add(LSTM(300, b22 = (b18.shape[1], b18.shape[2])))
    b21.add(Dense(1))
    b21.compile(b23 = 'mae', optimizer='adam')
    b24 = b21.fit(b18, b16, b20=b20, batch_size=batch_size, validation_data=(b19, b17), verbose=2, shuffle=False)
    return b21, b24
def fonk5(b24):
    plt.plot(b24.b24['b23'], b25 = 'train')
    plt.plot(b24.b24['val_loss'], b25 = 'b15')
    plt.legend()
    plt.title('RNN Fitting')
    plt.xlabel('Epochs', b26 = 16)
    plt.ylabel('Value Loss', b26 = 16)
    plt.show()
def fonk6(b32, b19, b11):
    b19 = b19.reshape((b19.shape[0], b19.shape[2]))
    b27 = np.concatenate((b32, b19[:, 1:]), b14=1)
    b27 = b11.inverse_transform(b27)
    return b27[:, 0]
def fonk7(b33, b27):
    plt.plot(b33, b28 = 'o', linestyle='-', color='b', b25='Actual Price')
    plt.plot(b27, b28 = 'o', linestyle='-', color='r', b25='Forecasted Price using LSTM RNN')
    plt.legend()
    plt.title("Testing over past 30 days")
    plt.xlabel('Days', b26 = 18)
    plt.ylabel('Bitcoin Price ($)', b26 = 16)
    plt.show()
def fonk8(b33, b27):
    b29 = sqrt(mean_squared_error(b33, b27))
    print(f'Test RMSE: {b29:.3f}')
def fonk9():
    b30 = 'ReducedFeatureSet.csv'
    b31 = 365*2 + (365 - 30)
    b13, b11 = fonk2(b30)
    b18, b16, b19, b17 = fonk3(b13, b31)
    b21, b24 = fonk4(b18, b16, b19, b17)
    fonk5(b24)
    b32 = b21.predict(b19)
    b27 = fonk6(b32, b19, b11)
    b17 = b17.reshape((len(b17), 1))
    b33 = np.concatenate((b17, b19[:, 1:]), b14=1)
    b33 = b11.inverse_transform(b33)
    b33 = b33[:, 0]
    fonk7(b33, b27)
    fonk8(b33, b27)
if b34 = = "__main__":
    fonk9()