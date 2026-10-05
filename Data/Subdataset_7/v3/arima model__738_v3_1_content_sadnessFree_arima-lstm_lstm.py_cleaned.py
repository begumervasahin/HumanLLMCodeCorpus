import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
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
b4 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv', usecols=[3], engine='python', skipfooter=3)
b5 = scaler.fit_transform(b4.values.astype('float32'))
train_size, b6 = 1200, 300
train, b7 = b5[:train_size, :], b5[train_size:train_size + b6, :]
print(f"Training set length: {len(train)}, Testing set length: {len(b7)}")
b1 = 10
trainX, b8 = fonk1(train, b1)
b10, b9 = fonk1(b7, b1)
trainX, b10 = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1])), np.reshape(b10, (b10.shape[0], 1, b10.shape[1]))
b11 = Sequential()
b11.add(LSTM(4, b12 = (1, b1)))
b11.add(Dense(1))
b11.compile(b13 = 'mean_squared_error', optimizer='adam')
b11.fit(trainX, b8, b14 = 100, batch_size=1, verbose=2)
b11.save('../b11/lstm.h5')
trainPredict, b15 = scaler.inverse_transform(b11.predict(trainX)), scaler.inverse_transform(b11.predict(b10))
b8, b9 = scaler.inverse_transform([b8]), scaler.inverse_transform([b9])
trainScore, b16 = math.sqrt(mean_squared_error(b8[0], trainPredict[:, 0])), math.sqrt(mean_squared_error(b9[0], b15[:, 0]))
print(f'Training Score: {trainScore:.2f} RMSE')
print(f'Testing Score: {b16:.2f} RMSE')
trainPredictPlot, b17 = np.empty_like(b5), np.empty_like(b5)
trainPredictPlot[:, :], b17[:, :] = np.nan, np.nan
trainPredictPlot[b1:len(trainPredict) + b1, :] = trainPredict
b17[len(trainPredict) + (b1 * 2) + 1:len(b5) - 1, :] = b15
plt.plot(scaler.inverse_transform(b5), b18 = 'Original Data')
plt.plot(trainPredictPlot, b18 = 'Training Prediction')
plt.plot(b17, b18 = 'Testing Prediction')
plt.legend()
plt.show()