import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
b1 = '/Users/daihanru/Desktop/ç ç©¶çå°è®ºæ/æ¶é´åºåæ°æ®9-8-2.csv'
b2 = pd.read_csv(b1, usecols=[1, 2, 3], engine='python', skipfooter=3)
b3 = b2.values
b3 = b3.astype('float32')
b4 = MinMaxScaler(feature_range=(0, 1))
b3 = b4.fit_transform(b3)
b5 = int(len(b3) * 0.6)
train, b6 = b3[0:b5, :], b3[b5:len(b3), :]
def fonk1(b3, b7 = 1):
    dataX, b8 = [], []
    for i in range(len(b3) - b7 - 1):
        b9 = b3[i:(i + b7), 0]
        b9 = np.append(b9, [b3[i + b7 - 1, 1]])
        b9 = np.append(b9, [b3[i + b7 - 1, 2] / 2])
        dataX.append(b9)
        b8.append(b3[i + b7, 0])
    return np.array(dataX), np.array(b8)
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
b16 = b4.inverse_transform(np.concatenate((trainX[:, :1], b16), axis=1))[:, 1]
b10 = b4.inverse_transform(np.concatenate((trainX[:, :1], b10.reshape(-1, 1)), axis=1))[:, 1]
b17 = b4.inverse_transform(np.concatenate((testX[:, :1], b17), axis=1))[:, 1]
b11 = b4.inverse_transform(np.concatenate((testX[:, :1], b11.reshape(-1, 1)), axis=1))[:, 1]
b18 = mean_squared_error(b11, b17)
print('Test Score: %.2f MSE (%.2f RMSE)' % (b18, math.sqrt(b18)))
plt.plot(b3[6000:6100, 0], '-', b19 = "Real Flow")
plt.plot(b17[6000:6100], '--', b20 = 'red', b19="LSTM Prediction")
plt.legend(b21 = 'upper left')
plt.show()