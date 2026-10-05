import numpy
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
b1 = pandas.read_csv('/Users/daihanru/Desktop/ç ç©¶çå°è®ºæ/æ¶é´åºåæ°æ®9-8-2.csv', usecols=[1, 2, 3], engine='python', skipfooter=3)
b2 = b1.values
b2 = b2.astype('float32')
b3 = MinMaxScaler(feature_range=(0, 1))
b2 = b3.fit_transform(b2)
b4 = int(len(b2) * 0.6)
train, b5 = b2[0:b4, :], b2[b4:len(b2), :]
def fonk1(b2, b6 = 1):
    dataX, b7 = [], []
    for i in range(len(b2) - b6 - 1):
        b8 = b2[i:(i + b6), 0]
        b8 = numpy.append(b8, [b2[i + b6 - 1, 1]])
        b8 = numpy.append(b8, [b2[i + b6 - 1, 2] / 2])
        dataX.append(b8)
        b7.append(b2[i + b6, 0])
    return numpy.array(dataX), numpy.array(b7)
b6 = 5
trainX, b9 = fonk1(train, b6)
testX, b10 = fonk1(b5, b6)
b11 = Sequential()
b11.add(Dense(8, b12 = b6 + 2, activation='relu'))
b11.add(Dense(1))
b11.compile(b13 = 'mean_squared_error', optimizer='adam')
b11.fit(trainX, b9, b14 = 1000, batch_size=2, verbose=2)
b11.save('../b11/lstm.h5')
b15 = b11.predict(trainX)
b16 = b11.predict(testX)
b15 = b3.inverse_transform(numpy.concatenate((trainX[:, :1], b15), axis=1))[:, 1]
b9 = b3.inverse_transform(numpy.concatenate((trainX[:, :1], b9.reshape(-1, 1)), axis=1))[:, 1]
b16 = b3.inverse_transform(numpy.concatenate((testX[:, :1], b16), axis=1))[:, 1]
b10 = b3.inverse_transform(numpy.concatenate((testX[:, :1], b10.reshape(-1, 1)), axis=1))[:, 1]
b17 = mean_squared_error(b10, b16)
print('Test Score: %.2f MSE (%.2f RMSE)' % (b17, math.sqrt(b17)))
plt.plot(b2[6000:6100, 0], '-', b18 = "Real Flow")
plt.plot(b16[6000:6100], '--', b19 = 'red', b18="LSTM Prediction")
plt.legend(b20 = 'upper left')
plt.show()