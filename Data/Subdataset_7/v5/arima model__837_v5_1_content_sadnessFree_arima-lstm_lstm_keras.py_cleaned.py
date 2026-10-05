import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
b1 = '/Users/daihanru/Desktop/ç ç©¶çå°è®ºæ/æ¶é´åºåæ°æ®9-8-2.csv'
b2 = pd.read_csv(b1, usecols=[1, 2, 3], engine='python', skipfooter=3)
b3 = b2.values.astype('float32')
b4 = int(len(b3) * 0.6)
train_data, b5 = b3[:b4], b3[b4:]
def fonk1(b3, b6 = 1):
    dataX, b7 = [], []
    for i in range(len(b3) - b6 - 1):
        b8 = b3[i:(i + b6), 0]
        b8 = np.append(b8, [b3[i + b6 - 1, 1]])
        b8 = np.append(b8, [b3[i + b6 - 1, 2] / 2])
        dataX.append(b8)
        b7.append(b3[i + b6, 0])
    return np.array(dataX), np.array(b7)
b6 = 5
trainX, b9 = fonk1(train_data, b6)
testX, b10 = fonk1(b5, b6)
b11 = Sequential([
    Dense(8, b12 = b6 + 2, activation='relu'),
    Dense(1)
])
b11.compile(b13 = 'mean_squared_error', optimizer='adam')
b11.fit(trainX, b9, b14 = 1000, batch_size=2, verbose=2)
b11.save('../b11/lstm.h5')
b15 = b11.predict(trainX)
b16 = b11.predict(testX)
b17 = b11.evaluate(testX, b10, verbose=0)
print('Test Score: %.2f MSE (%.2f RMSE)' % (b17, math.sqrt(b17)))
plt.plot(b3[6000:6100, 0], '-', b18 = "Real Flow")
plt.plot(b16[6000 - b4:6100 - b4, 0], '--', b19 = 'red', b18="LSTM Predictions")
plt.legend(b20 = 'upper left')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Comparison between Real Flow and LSTM Predictions')
plt.show()