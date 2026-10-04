import numpy as np
import math
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import model_from_json
def fonk1(b5, b1 = 1):
    dataX, b2 = [], []
    for i in range(len(b5)-b1-1):
        b3 = b5[i:(i+b1), 0]
        dataX.append(b3)
        b2.append(b5[i + b1, 0])
    return np.array(dataX), np.array(b2)
np.random.seed(7)
b4 = pd.read_csv('int2.csv', usecols=[1], engine='python', skipfooter=3)
b5 = b4.values
b5 = b5.astype('float32')
b6 = MinMaxScaler(feature_range=(0, 1))
b5 = b6.fit_transform(b5)
b7 = int(len(b5) * 0.9)
b8 = len(b5) - b7
train, b9 = b5[0:b7, :], b5[b7:len(b5), :]
b1 = 1
b12, b10 = fonk1(train, b1)
b13, b11 = fonk1(b9, b1)
b12 = np.reshape(b12, (b12.shape[0], 1, b12.shape[1]))
b13 = np.reshape(b13, (b13.shape[0], 1, b13.shape[1]))
b14 = open('model.json', 'r')
b15 = b14.read()
b14.close()
b16 = model_from_json(b15)
b16.load_weights("model.h5")
b16.compile(b17 = 'mean_squared_error', optimizer='adam')
print("Loaded model from disk")
b18 = b16.predict(b12)
b19 = b16.predict(b13)
b18 = b6.inverse_transform(b18)
b10 = b6.inverse_transform([b10])
b19 = b6.inverse_transform(b19)
b11 = b6.inverse_transform([b11])
b20 = math.sqrt(mean_squared_error(b10[0], b18[:, 0]))
print('Train Score: %.2f RMSE' % (b20))
b21 = math.sqrt(mean_squared_error(b11[0], b19[:, 0]))
print('Test Score: %.2f RMSE' % (b21))