import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
def fonk1(b5, b1 = 1):
    dataX, b2 = [], []
    for i in range(len(b5) - b1 - 1):
        b3 = b5[i:(i + b1), 0]
        dataX.append(b3)
        b2.append(b5[i + b1, 0])
    return numpy.array(dataX), numpy.array(b2)
numpy.random.seed(7)
b4 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv', usecols=[3], engine='python', skipfooter=3)
b5 = b4.values
b5 = b5.astype('float32')
b6 = MinMaxScaler(feature_range=(0, 1))
b5 = b6.fit_transform(b5)
a1 = 1200
a2 = 300
train, b7 = b5[0:a1, :], b5[a1:a1 + a2, :]
print(len(train), len(b7))
b1 = 10
b10, b8 = fonk1(train, b1)
b11, b9 = fonk1(b7, b1)
b10 = numpy.reshape(b10, (b10.shape[0], 1, b10.shape[1]))
b11 = numpy.reshape(b11, (b11.shape[0], 1, b11.shape[1]))
b12 = Sequential()
b12.add(LSTM(4, b13 = (1, b1)))
b12.add(Dense(1))
b12.compile(b14 = 'mean_squared_error', optimizer='adam')
b12.fit(b10, b8, b15 = 100, batch_size=1, verbose=2)
b12.save('../b12/lstm.h5')
b16 = b12.predict(b10)
b17 = b12.predict(b11)
b16 = b6.inverse_transform(b16)
b8 = b6.inverse_transform([b8])
b17 = b6.inverse_transform(b17)
b9 = b6.inverse_transform([b9])
b18 = math.sqrt(mean_squared_error(b8[0], b16[:, 0]))
print('Train Score: %.2f RMSE' % (b18))
b19 = math.sqrt(mean_squared_error(b9[0], b17[:, 0]))
print('Test Score: %.2f RMSE' % (b19))
b20 = numpy.empty_like(b5)
b20[:, :] = numpy.nan
b20[b1:len(b16) + b1, :] = b16
b21 = numpy.empty_like(b5)
b21[:, :] = numpy.nan
b21[len(b16) + (b1 * 2) + 1:len(b5) - 1, :] = b17
plt.plot(b6.inverse_transform(b5))
plt.plot(b20)
plt.plot(b21)
plt.show()