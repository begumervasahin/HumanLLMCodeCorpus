import numpy as np
import math
import pandas as pd
from keras.models import Sequential, model_from_json
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
def fonk1(b5, b1 = 1):
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
train, b8 = b5[0:b7], b5[b7:]
b1 = 1
b11, b9 = fonk1(train, b1)
b12, b10 = fonk1(b8, b1)
b11 = np.reshape(b11, (b11.shape[0], 1, b11.shape[1]))
b12 = np.reshape(b12, (b12.shape[0], 1, b12.shape[1]))
with open('model.json', 'r') as json_file:
    b13 = json_file.read()
b14 = model_from_json(b13)
b14.load_weights("model.h5")
b14.compile(b15 = 'mean_squared_error', optimizer='adam')
print("Loaded model from disk")
b16 = b14.predict(b11)
b17 = b14.predict(b12)
b16 = b6.inverse_transform(b16)
b9 = b6.inverse_transform([b9])
b17 = b6.inverse_transform(b17)
b10 = b6.inverse_transform([b10])
b18 = math.sqrt(mean_squared_error(b9[0], b16[:, 0]))
print(f'Train Score: {b18:.2f} RMSE')
b19 = math.sqrt(mean_squared_error(b10[0], b17[:, 0]))
print(f'Test Score: {b19:.2f} RMSE')