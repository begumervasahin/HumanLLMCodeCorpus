import numpy as np
import pandas as pd
from keras.models import model_from_json
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import math
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        dataX.append(dataset[i:(i + look_back), 0])
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)
def load_and_preprocess_data(file_path, look_back=1, train_split=0.9):
    dataframe = pd.read_csv(file_path, usecols=[1], engine='python', skipfooter=3)
    dataset = dataframe.values.astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform(dataset)
    train_size = int(len(dataset) * train_split)
    train, test = dataset[:train_size], dataset[train_size:]
    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)
    trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    return trainX, trainY, testX, testY, scaler
def load_model(model_json_path, model_weights_path):
    with open(model_json_path, 'r') as json_file:
        loaded_model_json = json_file.read()
    model = model_from_json(loaded_model_json)
    model.load_weights(model_weights_path)
    model.compile(loss='mean_squared_error', optimizer='adam')
    print("Loaded model from disk")
    return model
def invert_predictions(predictions, scaler):
    return scaler.inverse_transform(predictions)
def evaluate_model(model, trainX, trainY, testX, testY, scaler):
    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)
    trainPredict = invert_predictions(trainPredict, scaler)
    trainY = invert_predictions([trainY], scaler)
    testPredict = invert_predictions(testPredict, scaler)
    testY = invert_predictions([testY], scaler)
    trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:, 0]))
    print(f'Train Score: {trainScore:.2f} RMSE')
    testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:, 0]))
    print(f'Test Score: {testScore:.2f} RMSE')
np.random.seed(7)
trainX, trainY, testX, testY, scaler = load_and_preprocess_data('int2.csv')
model = load_model('model.json', 'model.h5')
evaluate_model(model, trainX, trainY, testX, testY, scaler)