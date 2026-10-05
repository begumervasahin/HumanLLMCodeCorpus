import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
np.random.seed(7)
b1 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b2 = pd.read_csv(b1, usecols=[3], engine='python', skipfooter=3)
b3 = b2.values.astype('float32')
b4 = MinMaxScaler(feature_range=(0, 1))
b3 = b4.fit_transform(b3)
train_size, b5 = 1200, 300
train, b6 = b3[:train_size, :], b3[train_size:train_size + b5, :]
print(f"Training set length: {len(train)}, Testing set length: {len(b6)}")
a1 = 10
b9, b7 = create_dataset(train, a1)
b10, b8 = create_dataset(b6, a1)
b9 = np.reshape(b9, (b9.shape[0], 1, b9.shape[1]))
b10 = np.reshape(b10, (b10.shape[0], 1, b10.shape[1]))
b11 = Sequential()
b11.add(LSTM(4, b12 = (1, a1)))
b11.add(Dense(1))
b11.compile(b13 = 'mean_squared_error', optimizer='adam')
b11.fit(b9, b7, b14 = 100, batch_size=1, verbose=2)
b11.save('../b11/lstm.h5')
b15 = b4.inverse_transform(b11.predict(b9))
b16 = b4.inverse_transform(b11.predict(b10))
b7 = b4.inverse_transform([b7])
b8 = b4.inverse_transform([b8])
b17 = math.sqrt(mean_squared_error(b7[0], b15[:, 0]))
b18 = math.sqrt(mean_squared_error(b8[0], b16[:, 0]))
print(f'Train Score: {b17:.2f} RMSE')
print(f'Test Score: {b18:.2f} RMSE')
plot_original_and_predictions(b3, b15, b16, a1)