
from math import fabs, sqrt
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
def calculate_mape(y_true, y_pred):
    absolute_percentage_errors = np.abs(y_pred - y_true) / y_true
    mean_absolute_percentage_error = np.mean(absolute_percentage_errors)
    return mean_absolute_percentage_error
def convert_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if isinstance(data, list) else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = [], []
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    aggregated = pd.concat(cols, axis=1)
    aggregated.columns = names
    if dropnan:
        aggregated.dropna(inplace=True)
    return aggregated
dataset_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
dataset = pd.read_csv(dataset_path, usecols=[2, 3], header=0, index_col=0)
values = dataset.values[1::2].astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_values = scaler.fit_transform(values)
reframed_data = convert_to_supervised(scaled_values, 10, 1)
train_start, train_size = 0, 500
train_data = reframed_data.values[train_start:train_start + train_size, :]
test_data = reframed_data.values[650:700, :]
train_X, train_Y = train_data[:, :-1], train_data[:, -1]
test_X, test_Y = test_data[:, :-1], test_data[:, -1]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
history = model.fit(train_X, train_Y, epochs=10000, batch_size=500, validation_data=(test_X, test_Y), verbose=2, shuffle=False)
model.save('../model/lstm-30min.h5')
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()
predicted_values = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
inv_yhat = np.concatenate((predicted_values, test_X[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)[:, 0]
inv_y = np.concatenate((test_Y.reshape((len(test_Y), 1)), test_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)[:, 0]
mse = mean_squared_error(inv_y, inv_yhat)
rmse = sqrt(mse)
mae = mean_absolute_error(inv_y, inv_yhat)
mape = calculate_mape(inv_y, inv_yhat)
print(f'Test MAE: {mae:.3f}, MSE: {mse:.3f}, RMSE: {rmse:.3f}, MAPE: {mape:.3f}')
plt.plot(inv_y, label='Actual')
plt.plot(inv_yhat, label='Predicted')
plt.legend()
plt.show()