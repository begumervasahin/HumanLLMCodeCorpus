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
dataset = scaler.fit_transform(dataframe.values.astype('float32'))
train_size, test_size = 1200, 300
train, test = dataset[:train_size, :], dataset[train_size:train_size + test_size, :]
print(f"Training set length: {len(train)}, Testing set length: {len(test)}")
look_back = 10
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
trainX, testX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1])), np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)
model.save('../model/lstm.h5')
trainPredict, testPredict = scaler.inverse_transform(model.predict(trainX)), scaler.inverse_transform(model.predict(testX))
trainY, testY = scaler.inverse_transform([trainY]), scaler.inverse_transform([testY])
trainScore, testScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:, 0])), math.sqrt(mean_squared_error(testY[0], testPredict[:, 0]))
print(f'Training Score: {trainScore:.2f} RMSE')
print(f'Testing Score: {testScore:.2f} RMSE')
trainPredictPlot, testPredictPlot = np.empty_like(dataset), np.empty_like(dataset)
trainPredictPlot[:, :], testPredictPlot[:, :] = np.nan, np.nan
trainPredictPlot[look_back:len(trainPredict) + look_back, :] = trainPredict
testPredictPlot[len(trainPredict) + (look_back * 2) + 1:len(dataset) - 1, :] = testPredict
plt.plot(scaler.inverse_transform(dataset), label='Original Data')
plt.plot(trainPredictPlot, label='Training Prediction')
plt.plot(testPredictPlot, label='Testing Prediction')
plt.legend()
plt.show()