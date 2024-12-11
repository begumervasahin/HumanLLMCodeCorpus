import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
np.random.seed(7)
b1 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv', usecols=[3], engine='python', skipfooter=3)
b2 = b1.values.astype('float32')
b3 = MinMaxScaler(feature_range=(0, 1))
b2 = b3.fit_transform(b2)
train_size, b4 = 1200, 300
train, b5 = b2[:train_size, :], b2[train_size:train_size + b4, :]
print(f"Training set length: {len(train)}, Testing set length: {len(b5)}")
a1 = 10
b8, b6 = create_dataset(train, a1)
b9, b7 = create_dataset(b5, a1)
b8 = np.reshape(b8, (b8.shape[0], 1, b8.shape[1]))
b9 = np.reshape(b9, (b9.shape[0], 1, b9.shape[1]))
b10 = Sequential()
b10.add(LSTM(4, b11 = (1, a1)))
b10.add(Dense(1))
b10.compile(b12 = 'mean_squared_error', optimizer='adam')
b10.fit(b8, b6, b13 = 100, batch_size=1, verbose=2)
b10.save('../b10/lstm.h5')
b14 = b3.inverse_transform(b10.predict(b8))
b15 = b3.inverse_transform(b10.predict(b9))
b6 = b3.inverse_transform([b6])
b7 = b3.inverse_transform([b7])
b16 = math.sqrt(mean_squared_error(b6[0], b14[:, 0]))
b17 = math.sqrt(mean_squared_error(b7[0], b15[:, 0]))
print(f'Train Score: {b16:.2f} RMSE')
print(f'Test Score: {b17:.2f} RMSE')
b18 = np.empty_like(b2)
b18[:, :] = np.nan
b18[a1:len(b14) + a1, :] = b14
b19 = np.empty_like(b2)
b19[:, :] = np.nan
b19[len(b14) + (a1 * 2) + 1:len(b2) - 1, :] = b15
plt.plot(b3.inverse_transform(b2))
plt.plot(b18)
plt.plot(b19)
plt.show()