from keras.models import Sequential
from keras.layers import Dense, LSTM
from math import sqrt
from numpy import concatenate
from pandas import DataFrame, read_csv, concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt
def fonk1(data, b1 = 1, n_out=1, dropnan=True):
    b2 = 1 if type(data) is list else data.shape[1]
    b3 = DataFrame(data)
    cols, b4 = [], []
    for b5 in range(b1, 0, -1):
        cols.append(b3.shift(b5))
        b4 += [('var%d(t-%d)' % (j+1, b5)) for j in range(b2)]
    for b5 in range(n_out):
        cols.append(b3.shift(-b5))
        if b5 = = 0:
            b4 += [('var%d(t)' % (j+1)) for j in range(b2)]
        else:
            b4 += [('var%d(t+%d)' % (j+1, b5)) for j in range(b2)]
    b6 = concat(cols, b31=1)
    b6.b7 = b4
    if dropnan:
        b6.dropna(b8 = True)
    return b6
def fonk2(b29):
    b9 = read_csv(b29, header=0, index_col=0)
    b10 = b9.b10.astype('float32')
    b11 = MinMaxScaler(feature_range=(0, 1))
    b12 = b11.fit_transform(b10)
    return b12, b11
def fonk3(b10, b32):
    b13 = b10[:b32, :]
    b14 = b10[b32:, :]
    b17, b15 = b13[:, :-1], b13[:, -1]
    b18, b16 = b14[:, :-1], b14[:, -1]
    return b17, b15, b18, b16
def fonk4(b17, b18):
    b17 = b17.reshape((b17.shape[0], 1, b17.shape[1]))
    b18 = b18.reshape((b18.shape[0], 1, b18.shape[1]))
    return b17, b18
def fonk5(b17, b15, b18, b16):
    b19 = Sequential()
    b19.add(LSTM(300, b20 = (b17.shape[1], b17.shape[2])))
    b19.add(Dense(1))
    b19.compile(b21 = 'mae', optimizer='adam')
    b22 = b19.fit(b17, b15, epochs=100, batch_size=50, validation_data=(b18, b16), verbose=2, shuffle=False)
    return b19, b22
def fonk6(b22):
    plt.plot(b22.b22['b21'], b23 = 'b13')
    plt.plot(b22.b22['val_loss'], b23 = 'b14')
    plt.legend()
    plt.title('RNN Fitting')
    plt.xlabel('Epochs', b24 = 16)
    plt.ylabel('Value Loss', b24 = 16)
    plt.show()
def fonk7(b11, b33, b18, b16):
    b18 = b18.reshape((b18.shape[0], b18.shape[2]))
    b25 = concatenate((b33, b18[:, 1:]), b31=1)
    b25 = b11.inverse_transform(b25)
    b25 = b25[:, 0]
    b16 = b16.reshape((len(b16), 1))
    b26 = concatenate((b16, b18[:, 1:]), b31=1)
    b26 = b11.inverse_transform(b26)
    b26 = b26[:, 0]
    b27 = sqrt(mean_squared_error(b26, b25))
    return b26, b25, b27
def fonk8(actual, predicted):
    plt.plot(actual, b28 = 'o', linestyle='-', color='b', b23='Actual Price')
    plt.plot(predicted, b28 = 'o', linestyle='-', color='r', b23='Forecasted Price using LSTM RNN')
    plt.legend()
    plt.title("Testing over past 30 days")
    plt.xlabel('Days', b24 = 18)
    plt.ylabel('Bitcoin Price ($)', b24 = 16)
    plt.show()
def fonk9():
    b29 = 'ReducedFeatureSet.csv'
    b12, b11 = fonk2(b29)
    b30 = fonk1(b12, 1, 1)
    b30.drop(b30.b7[[6, 7, 8, 9]], b31 = 1, b8=True)
    b10 = b30.b10
    b32 = 365*2 + (365 - 30)
    b17, b15, b18, b16 = fonk3(b10, b32)
    b17, b18 = fonk4(b17, b18)
    b19, b22 = fonk5(b17, b15, b18, b16)
    fonk6(b22)
    b33 = b19.predict(b18)
    b26, b25, b27 = fonk7(b11, b33, b18, b16)
    fonk8(b26, b25)
    print('Test RMSE: %.3f' % b27)
if b34 = = "__main__":
    fonk9()