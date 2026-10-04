import numpy as np
import math
import pandas as pd
from keras.models import Sequential, model_from_json
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
def create_dataset(dataset, look_back=5):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)
np.random.seed(7)
dataframe = pd.read_csv('int2.csv', usecols=[1], engine='python', skipfooter=3)
dataset = dataframe.values.astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)
train_size = int(len(dataset) * 0.9)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
print("Training data (X):", trainX)
print("Training data shape (X):", trainX.shape)
print("Training data (Y):", trainY)
print("Training data shape (Y):", trainY.shape)
print("Testing data (X):", testX)
print("Testing data shape (X):", testX.shape)
print("Testing data (Y):", testY)
print("Testing data shape (Y):", testY.shape)
print("-----------------------------")
with open('model.json', 'r') as json_file:
    loaded_model_json = json_file.read()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
loaded_model.compile(loss='mean_squared_error', optimizer='adam')
print("Loaded model from disk")
trainPredict = loaded_model.predict(trainX)
testPredict = loaded_model.predict(testX)
print("--------------------------------------------------------")
print("Train Predictions:", trainPredict)
print("Train Predictions shape:", trainPredict.shape)
print("Test Predictions:", testPredict)
print("Test Predictions shape:", testPredict.shape)
print("--------------------------------------------------------")
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:, 0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:, 0]))
print('Test Score: %.2f RMSE' % (testScore))