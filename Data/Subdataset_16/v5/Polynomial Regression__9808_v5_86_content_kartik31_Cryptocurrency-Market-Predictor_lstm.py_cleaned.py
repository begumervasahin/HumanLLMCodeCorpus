import numpy as np
import math
import pandas as pd
from keras.models import Sequential, model_from_json
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
def fonk1(b4, b1 = 5):
    dataX, b2 = [], []
    for i in range(len(b4) - b1 - 1):
        dataX.append(b4[i:(i + b1), 0])
        b2.append(b4[i + b1, 0])
    return np.array(dataX), np.array(b2)
def fonk2(file_path, usecols, skipfooter):
    b3 = pd.read_csv(file_path, usecols=usecols, engine='python', skipfooter=skipfooter)
    b4 = b3.values.astype('float32')
    b5 = MinMaxScaler(feature_range=(0, 1))
    b4 = b5.fit_transform(b4)
    return b4, b5
def fonk3(b4, b6 = 0.9):
    b7 = int(len(b4) * b6)
    train, b8 = b4[0:b7, :], b4[b7:len(b4), :]
    return train, b8
def fonk4(dataX):
    return np.reshape(dataX, (dataX.shape[0], 1, dataX.shape[1]))
def fonk5(model_json_path, model_weights_path):
    with open(model_json_path, 'r') as json_file:
        b9 = json_file.read()
    b10 = model_from_json(b9)
    b10.load_weights(model_weights_path)
    b10.compile(b11 = 'mean_squared_error', optimizer='adam')
    return b10
def fonk6(b5, b12, b13):
    b12 = b5.inverse_transform(b12)
    b13 = b5.inverse_transform([b13])
    return b12, b13
def fonk7(b13, predicted_values):
    return math.sqrt(mean_squared_error(b13[0], predicted_values[:, 0]))
np.random.seed(7)
b4, b5 = fonk2('int2.csv', usecols=[1], skipfooter=3)
train, b8 = fonk3(b4)
b1 = 1
b16, b14 = fonk1(train, b1)
b17, b15 = fonk1(b8, b1)
b16 = fonk4(b16)
b17 = fonk4(b17)
print(f"Training data (X): {b16}")
print(f"Training data shape (X): {b16.shape}")
print(f"Training data (Y): {b14}")
print(f"Training data shape (Y): {b14.shape}")
print(f"Testing data (X): {b17}")
print(f"Testing data shape (X): {b17.shape}")
print(f"Testing data (Y): {b15}")
print(f"Testing data shape (Y): {b15.shape}")
print("-----------------------------")
b18 = fonk5('b18.json', 'b18.h5')
print("Loaded b18 from disk")
b19 = b18.predict(b16)
b20 = b18.predict(b17)
print("--------------------------------------------------------")
print(f"Train Predictions: {b19}")
print(f"Train Predictions shape: {b19.shape}")
print(f"Test Predictions: {b20}")
print(f"Test Predictions shape: {b20.shape}")
print("--------------------------------------------------------")
b19, b14 = fonk6(b5, b19, b14)
b20, b15 = fonk6(b5, b20, b15)
b21 = fonk7(b14, b19)
print(f'Train Score: {b21:.2f} RMSE')
b22 = fonk7(b15, b20)
print(f'Test Score: {b22:.2f} RMSE')