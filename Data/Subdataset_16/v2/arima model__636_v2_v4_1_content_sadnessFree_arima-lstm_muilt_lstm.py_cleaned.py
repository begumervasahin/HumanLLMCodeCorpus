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
def fonk2(b15, b2 = 1, a1=1, dropnan=True):
    b3 = 1 if isinstance(b15, list) else b15.shape[1]
    b4 = pd.DataFrame(b15)
    cols, b5 = [], []
    for b6 in range(b2, 0, -1):
        cols.append(b4.shift(b6))
        b5 += [('var%d(t-%d)' % (j + 1, b6)) for j in range(b3)]
    for b6 in range(0, a1):
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
def fonk5():
    b15 = np.sin(np.linspace(0, 100, 200))
    b15 = b15.reshape((len(b15), 1))
    b16 = MinMaxScaler(feature_range=(0, 1))
    b17 = b16.fit_transform(b15)
    b2 = 3
    a1 = 1
    b18 = fonk2(b17, b2, a1)
    b19 = b18.b19
    b20 = int(len(b19) * 0.67)
    b21 = b19[:b20, :]
    b22 = b19[b20:, :]
    b23 = b2
    b26, b24 = b21[:, :b23], b21[:, -a1]
    b27, b25 = b22[:, :b23], b22[:, -a1]
    b26 = b26.reshape((b26.shape[0], b2, 1))
    b27 = b27.reshape((b27.shape[0], b2, 1))
    b10 = fonk3((b26.shape[1], b26.shape[2]))
    b10.fit(b26, b24, b28 = 50, batch_size=72, validation_data=(b27, b25), verbose=2, shuffle=False)
    b29 = b10.predict(b27)
    b27 = b27.reshape((b27.shape[0], b2))
    b30 = np.concatenate((b29, b27[:, 1:]), axis=1)
    b30 = b16.inverse_transform(b30)
    b30 = b30[:, 0]
    b25 = b25.reshape((len(b25), 1))
    b31 = np.concatenate((b25, b27[:, 1:]), axis=1)
    b31 = b16.inverse_transform(b31)
    b31 = b31[:, 0]
    b32 = mean_absolute_error(b31, b30)
    b33 = mean_squared_error(b31, b30)
    b34 = fonk1(b31, b30)
    print(f'MAE: {b32}')
    print(f'MSE: {b33}')
    print(f'MAPE: {b34}')
    fonk4(b31, b30)
if b35 = = "__main__":
    fonk5()