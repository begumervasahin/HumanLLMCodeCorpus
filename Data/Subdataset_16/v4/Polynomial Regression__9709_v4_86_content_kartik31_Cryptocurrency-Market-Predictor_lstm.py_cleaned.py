import numpy as np
import math
import pandas as pd
from keras.models import Sequential, model_from_json
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
def fonk1(b5, b1 = 5):
    dataX, b2 = [], []
    for i in range(len(b5) - b1 - 1):
        b3 = b5[i:(i + b1), 0]
        dataX.append(b3)
        b2.append(b5[i + b1, 0])
    return np.array(dataX), np.array(b2)
np.random.seed(7)
b4 = pd.read_csv('int2.csv', usecols=[1], engine='python', skipfooter=3)
b5 = b4.values.astype('float32')
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
print("Training data (X):", b12)
print("Training data shape (X):", b12.shape)
print("Training data (Y):", b10)
print("Training data shape (Y):", b10.shape)
print("Testing data (X):", b13)
print("Testing data shape (X):", b13.shape)
print("Testing data (Y):", b11)
print("Testing data shape (Y):", b11.shape)
print("-----------------------------")
with open('model.json', 'r') as json_file:
    b14 = json_file.read()
b15 = model_from_json(b14)
b15.load_weights("model.h5")
b15.compile(b16 = 'mean_squared_error', optimizer='adam')
print("Loaded model from disk")
b17 = b15.predict(b12)
b18 = b15.predict(b13)
print("--------------------------------------------------------")
print("Train Predictions:", b17)
print("Train Predictions shape:", b17.shape)
print("Test Predictions:", b18)
print("Test Predictions shape:", b18.shape)
print("--------------------------------------------------------")
b17 = b6.inverse_transform(b17)
b10 = b6.inverse_transform([b10])
b18 = b6.inverse_transform(b18)
b11 = b6.inverse_transform([b11])
b19 = math.sqrt(mean_squared_error(b10[0], b17[:, 0]))
print('Train Score: %.2f RMSE' % (b19))
b20 = math.sqrt(mean_squared_error(b11[0], b18[:, 0]))
print('Test Score: %.2f RMSE' % (b20))