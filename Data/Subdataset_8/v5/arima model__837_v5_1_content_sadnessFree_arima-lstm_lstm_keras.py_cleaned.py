import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
file_path = '/Users/daihanru/Desktop/ç ç©¶çå°è®ºæ/æ¶é´åºåæ°æ®9-8-2.csv'
dataframe = pd.read_csv(file_path, usecols=[1, 2, 3], engine='python', skipfooter=3)
dataset = dataframe.values.astype('float32')
train_size = int(len(dataset) * 0.6)
train_data, test_data = dataset[:train_size], dataset[train_size:]
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        features = dataset[i:(i + look_back), 0]
        features = np.append(features, [dataset[i + look_back - 1, 1]])
        features = np.append(features, [dataset[i + look_back - 1, 2] / 2])
        dataX.append(features)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)
look_back = 5
trainX, trainY = create_dataset(train_data, look_back)
testX, testY = create_dataset(test_data, look_back)
model = Sequential([
    Dense(8, input_dim=look_back + 2, activation='relu'),
    Dense(1)
])
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=1000, batch_size=2, verbose=2)
model.save('../model/lstm.h5')
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)
testScore = model.evaluate(testX, testY, verbose=0)
print('Test Score: %.2f MSE (%.2f RMSE)' % (testScore, math.sqrt(testScore)))
plt.plot(dataset[6000:6100, 0], '-', label="Real Flow")
plt.plot(testPredict[6000 - train_size:6100 - train_size, 0], '--', color='red', label="LSTM Predictions")
plt.legend(loc='upper left')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Comparison between Real Flow and LSTM Predictions')
plt.show()