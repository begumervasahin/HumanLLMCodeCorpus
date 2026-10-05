
import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
def mean_absolute_percentage_error(y_true, y_pred):
    absolute_errors = np.abs(y_pred - y_true)
    percentage_errors = absolute_errors / y_true
    return np.mean(percentage_errors)
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if isinstance(data, list) else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = [], []
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [f'var{j + 1}(t-{i})' for j in range(n_vars)]
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [f'var{j + 1}(t)' for j in range(n_vars)]
        else:
            names += [f'var{j + 1}(t+{i})' for j in range(n_vars)]
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace=True)
    return agg
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
dataset = pd.read_csv(file_path, usecols=[2, 3], header=0, index_col=0)
values = dataset.values[1::2].astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
reframed = series_to_supervised(scaled, 10, 1)
train_start, train_size = 0, 500
train = reframed.values[train_start:train_start + train_size, :]
test = reframed.values[650:700, :]
train_X, train_Y = train[:, :-1], train[:, -1]
test_X, test_Y = test[:, :-1], test[:, -1]
train_X = np.reshape(train_X, (train_X.shape[0], 1, train_X.shape[1]))
test_X = np.reshape(test_X, (test_X.shape[0], 1, test_X.shape[1]))
model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
history = model.fit(train_X, train_Y, epochs=10000, batch_size=500, validation_data=(test_X, test_Y), verbose=2, shuffle=False)
model.save('../model/lstm-30min.h5')
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()
yhat = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
inv_yhat = scaler.inverse_transform(np.concatenate((yhat, test_X[:, 1:]), axis=1))
inv_y = scaler.inverse_transform(np.concatenate((test_Y.reshape((len(test_Y), 1)), test_X[:, 1:]), axis=1))
mse = mean_squared_error(inv_y, inv_yhat)
rmse = math.sqrt(mse)
mae = mean_absolute_error(inv_y, inv_yhat)
mape = mean_absolute_percentage_error(inv_y, inv_yhat)
print(f'Test MAE: {mae:.3f} MSE: {mse:.3f} RMSE: {rmse:.3f} MAPE: {mape:.3f}')
plt.plot(inv_y, label='Actual')
plt.plot(inv_yhat, label='Predicted')
plt.show(figsize=(12, 6))