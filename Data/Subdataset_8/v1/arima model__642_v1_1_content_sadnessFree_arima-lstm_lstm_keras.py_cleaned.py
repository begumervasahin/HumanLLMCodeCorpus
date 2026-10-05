import numpy
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
dataframe = pandas.read_csv('/Users/daihanru/Desktop/ç ç©¶çå°è®ºæ/æ¶é´åºåæ°æ®9-8-2.csv', usecols=[1, 2, 3], engine='python', skipfooter=3)
dataset = dataframe.values
dataset = dataset.astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)
train_size = int(len(dataset) * 0.6)
train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        a = numpy.append(a, [dataset[i + look_back - 1, 1]])
        a = numpy.append(a, [dataset[i + look_back - 1, 2] / 2])
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return numpy.array(dataX), numpy.array(dataY)
look_back = 5
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
model = Sequential()
model.add(Dense(8, input_dim=look_back + 2, activation='relu'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=1000, batch_size=2, verbose=2)
model.save('../model/lstm.h5')
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)
trainPredict = scaler.inverse_transform(numpy.concatenate((trainX[:, :1], trainPredict), axis=1))[:, 1]
trainY = scaler.inverse_transform(numpy.concatenate((trainX[:, :1], trainY.reshape(-1, 1)), axis=1))[:, 1]
testPredict = scaler.inverse_transform(numpy.concatenate((testX[:, :1], testPredict), axis=1))[:, 1]
testY = scaler.inverse_transform(numpy.concatenate((testX[:, :1], testY.reshape(-1, 1)), axis=1))[:, 1]
testScore = mean_squared_error(testY, testPredict)
print('Test Score: %.2f MSE (%.2f RMSE)' % (testScore, math.sqrt(testScore)))
plt.plot(dataset[6000:6100, 0], '-', label="Real Flow")
plt.plot(testPredict[6000:6100], '--', color='red', label="LSTM Prediction")
plt.legend(loc='upper left')
plt.show()