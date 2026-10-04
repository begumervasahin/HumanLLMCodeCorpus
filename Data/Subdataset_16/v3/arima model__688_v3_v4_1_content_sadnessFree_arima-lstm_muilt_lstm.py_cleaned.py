import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
def fonk1(y_true, b1):
    y_true, b1 = np.array(y_true), np.array(b1)
    return np.mean(np.abs((y_true - b1) / y_true)) * 100
def fonk2(b27, b2 = 1, b28=1, dropnan=True):
    b3 = 1 if isinstance(b27, list) else b27.shape[1]
    b4 = pd.DataFrame(b27)
    cols, b5 = [], []
    for b6 in range(b2, 0, -1):
        cols.append(b4.shift(b6))
        b5 += [('var%d(t-%d)' % (j + 1, b6)) for j in range(b3)]
    for b6 in range(0, b28):
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
def fonk3(b11):
    b10 = Sequential()
    b10.add(LSTM(50, b11 = b11))
    b10.add(Dense(1))
    b10.compile(b12 = 'b32', optimizer='adam')
    return b10
def fonk4(true_values, predicted_values):
    plt.figure(b13 = (10, 6))
    plt.plot(true_values, b14 = 'True Values')
    plt.plot(predicted_values, b14 = 'Predicted Values')
    plt.title('True vs Predicted Values')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
def fonk5(sequence, b2, b28):
    b15 = MinMaxScaler(feature_range=(0, 1))
    b16 = b15.fit_transform(sequence.reshape(-1, 1))
    b17 = fonk2(b16, b2, b28)
    b18 = b17.b18
    b19 = int(len(b18) * 0.67)
    train, b20 = b18[:b19, :], b18[b19:, :]
    return b15, train, b20
def fonk6(train, b20, b2, b28):
    b21 = b2
    b24, b22 = train[:, :b21], train[:, -b28]
    b25, b23 = b20[:, :b21], b20[:, -b28]
    b24 = b24.reshape((b24.shape[0], b2, 1))
    b25 = b25.reshape((b25.shape[0], b2, 1))
    return b24, b22, b25, b23
def fonk7(b15, b30, b25, b2):
    b25 = b25.reshape((b25.shape[0], b2))
    b26 = np.concatenate((b30, b25[:, 1:]), axis=1)
    b26 = b15.inverse_transform(b26)[:, 0]
    return b26
def fonk8():
    b27 = np.sin(np.linspace(0, 100, 200))
    b2, b28 = 3, 1
    b15, train, b20 = fonk5(b27, b2, b28)
    b24, b22, b25, b23 = fonk6(train, b20, b2, b28)
    b10 = fonk3((b24.shape[1], b24.shape[2]))
    b10.fit(b24, b22, b29 = 50, batch_size=72, validation_data=(b25, b23), verbose=2, shuffle=False)
    b30 = b10.predict(b25)
    b26 = fonk7(b15, b30, b25, b2)
    b23 = b23.reshape((len(b23), 1))
    b31 = fonk7(b15, b23, b25, b2)
    b32 = mean_absolute_error(b31, b26)
    b33 = mean_squared_error(b31, b26)
    b34 = fonk1(b31, b26)
    print(f'MAE: {b32}')
    print(f'MSE: {b33}')
    print(f'MAPE: {b34}')
    fonk4(b31, b26)
if b35 = = "__main__":
    fonk8()