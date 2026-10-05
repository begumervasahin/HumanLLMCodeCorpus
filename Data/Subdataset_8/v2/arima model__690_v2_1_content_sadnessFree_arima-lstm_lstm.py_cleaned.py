import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        sequence = dataset[i:(i + look_back), 0]
        dataX.append(sequence)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)
np.random.seed(7)
dataframe = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv', usecols=[3], engine='python', skipfooter=3)
dataset = dataframe.values
dataset = dataset.astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)
train_size = 1200
test_size = 300
train, test = dataset[0:train_size, :], dataset[train_size:train_size + test_size, :]
print(f"Training set length: {len(train)}, Testing set length: {len(test)}")
look_back = 10
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)
model.save('../model/lstm.h5')
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:, 0]))
print(f'Training Score: {trainScore:.2f} RMSE')
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:, 0]))
print(f'Testing Score: {testScore:.2f} RMSE')
trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict) + look_back, :] = trainPredict
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict) + (look_back * 2) + 1:len(dataset) - 1, :] = testPredict
plt.plot(scaler.inverse_transform(dataset), label='Original Data')
plt.plot(trainPredictPlot, label='Training Prediction')
plt.plot(testPredictPlot, label='Testing Prediction')
plt.legend()
plt.show()