import numpy as np
import pandas as pd
from keras.models import model_from_json
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import math
def fonk1(b4, b1 = 1):
    dataX, b2 = [], []
    for i in range(len(b4) - b1 - 1):
        dataX.append(b4[i:(i + b1), 0])
        b2.append(b4[i + b1, 0])
    return np.array(dataX), np.array(b2)
def fonk2(file_path, b1 = 1, train_split=0.9):
    b3 = pd.read_csv(file_path, usecols=[1], engine='python', skipfooter=3)
    b4 = b3.values.astype('float32')
    b5 = MinMaxScaler(feature_range=(0, 1))
    b4 = b5.fit_transform(b4)
    b6 = int(len(b4) * train_split)
    train, b7 = b4[:b6], b4[b6:]
    b10, b8 = fonk1(train, b1)
    b11, b9 = fonk1(b7, b1)
    b10 = np.reshape(b10, (b10.shape[0], 1, b10.shape[1]))
    b11 = np.reshape(b11, (b11.shape[0], 1, b11.shape[1]))
    return b10, b8, b11, b9, b5
def fonk3(model_json_path, model_weights_path):
    with open(model_json_path, 'r') as json_file:
        b12 = json_file.read()
    b13 = model_from_json(b12)
    b13.load_weights(model_weights_path)
    b13.compile(b14 = 'mean_squared_error', optimizer='adam')
    print("Loaded b13 from disk")
    return b13
def fonk4(predictions, b5):
    return b5.inverse_transform(predictions)
def fonk5(b13, b10, b8, b11, b9, b5):
    b15 = b13.predict(b10)
    b16 = b13.predict(b11)
    b15 = fonk4(b15, b5)
    b8 = fonk4([b8], b5)
    b16 = fonk4(b16, b5)
    b9 = fonk4([b9], b5)
    b17 = math.sqrt(mean_squared_error(b8[0], b15[:, 0]))
    print(f'Train Score: {b17:.2f} RMSE')
    b18 = math.sqrt(mean_squared_error(b9[0], b16[:, 0]))
    print(f'Test Score: {b18:.2f} RMSE')
np.random.seed(7)
b10, b8, b11, b9, b5 = fonk2('int2.csv')
b13 = fonk3('b13.json', 'b13.h5')
fonk5(b13, b10, b8, b11, b9, b5)