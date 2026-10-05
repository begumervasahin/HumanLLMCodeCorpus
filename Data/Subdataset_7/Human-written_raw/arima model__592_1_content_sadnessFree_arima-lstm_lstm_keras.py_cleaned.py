import numpy
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
b1 = pandas.read_csv('/Users/daihanru/Desktop/ç ç©¶çå°è®ºæ/æ¶é´åºåæ°æ®9-8-2.csv', usecols=[1, 2, 3], engine='python',
                            b2 = 3)
b3 = b1.values
b3 = b3.astype('float32')
b4 = int(len(b3) * 0.6)
b5 = len(b3) - b4
train, b6 = b3[0:b4, :], b3[b4:len(b3), :]
print(len(train), len(b6))
def fonk1(b3, b7 = 1):
    dataX, b8 = [], []
    for i in range(len(b3) - b7 - 1):
        b9 = b3[i:(i + b7), 0]
        b9 = numpy.append(b9, [b3[i + b7 - 1, 1]])
        b9 = numpy.append(b9, [b3[i + b7 - 1, 2] / 2])
        dataX.append(b9)
        b8.append(b3[i + b7, 0])
    return numpy.array(dataX), numpy.array(b8)
b7 = 5
trainX, b10 = fonk1(train, b7)
testX, b11 = fonk1(b6, b7)
b12 = Sequential()
b12.add(Dense(8, b13 = b7 + 2, activation='relu'))
b12.add(Dense(1))
b12.compile(b14 = 'mean_squared_error', optimizer='adam')
b12.fit(trainX, b10, b15 = 1000, batch_size=2, verbose=2)
b12.save('../b12/lstm.h5')
b16 = b12.predict(trainX)
b17 = b12.predict(testX)
b18 = b12.evaluate(testX, b11, verbose=0)
print('Test Score: %.2f MSE (%.2f RMSE)' % (b18, math.sqrt(b18)))
b19 = numpy.empty_like(b3)
b19[:, :] = numpy.nan
b19[b7:len(b16) + b7, :] = b16
b20 = numpy.empty_like(b3)
b20[:, :] = numpy.nan
b20[len(b16) + (b7 * 2) + 1:len(b3) - 1, :] = b17
plt.plot(b3[6000:6100, 0], '-', b21 = "real flow")
plt.plot(b20[6000:6100, 0], '--', b22 = 'red', b21="LSTM")
plt.legend(b23 = 'upper left')
plt.show()