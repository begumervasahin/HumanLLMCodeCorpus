import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
b1 = pd.read_csv('/Users/daihanru/Desktop/ç ç©¶çå°è®ºæ/æ¶é´åºåæ°æ®9-8-2.csv', usecols=[1, 2, 3], engine='python', skipfooter=3)
b2 = b1.values.astype('float32')
b3 = int(len(b2) * 0.6)
b4 = len(b2) - b3
train, b5 = b2[0:b3, :], b2[b3:len(b2), :]
def fonk1(b2, b6 = 1):
    dataX, b7 = [], []
    for i in range(len(b2) - b6 - 1):
        b8 = b2[i:(i + b6), 0]
        b8 = np.append(b8, [b2[i + b6 - 1, 1]])
        b8 = np.append(b8, [b2[i + b6 - 1, 2] / 2])
        dataX.append(b8)
        b7.append(b2[i + b6, 0])
    return np.array(dataX), np.array(b7)
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
b17 = b11.evaluate(testX, b10, verbose=0)
print('Test Score: %.2f MSE (%.2f RMSE)' % (b17, math.sqrt(b17)))
b18 = np.empty_like(b2)
b18[:, :] = np.nan
b18[b6:len(b15) + b6, :] = b15
b19 = np.empty_like(b2)
b19[:, :] = np.nan
b19[len(b15) + (b6 * 2) + 1:len(b2) - 1, :] = b16
plt.plot(b2[6000:6100, 0], '-', b20 = "real flow")
plt.plot(b19[6000:6100, 0], '--', b21 = 'red', b20="LSTM")
plt.legend(b22 = 'upper left')
plt.show()