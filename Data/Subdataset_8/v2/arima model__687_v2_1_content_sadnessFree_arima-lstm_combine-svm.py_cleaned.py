import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
from sklearn.ensemble import GradientBoostingRegressor
import arima
look_back = 10
line_test_size = 300
windows_size = 5
test_start = line_test_size + windows_size - 1
model_path = '../model/lstm-15min.h5'
dataframe = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], engine='python', header=0, index_col=0)
values = dataframe.values.astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
reframed = series_to_supervised(scaled, look_back, 1)
lstm_size = arima.start + arima.size - look_back
test = reframed.values[lstm_size:lstm_size + arima.test_size, :]
test_X, test_y = test[:, :-1], test[:, -1]
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
lstm_model = load_model(model_path)
yhat = lstm_model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
inv_yhat = np.concatenate((yhat, test_X[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)[:, 0]
test_y = test_y.reshape((len(test_y), 1))
inv_y = np.concatenate((test_y, test_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)[:, 0]
mse = mean_squared_error(inv_y[test_start:], inv_yhat[test_start:])
rmse = math.sqrt(mean_squared_error(inv_y[test_start:], inv_yhat[test_start:]))
mae = mean_absolute_error(inv_y[test_start:], inv_yhat[test_start:])
mape = arima.mean_a_p_e(inv_y[test_start:], inv_yhat[test_start:])
print(f'LSTM Test MAE: {mae:.3f}, MSE: {mse:.3f}, RMSE: {rmse:.3f}, MAPE: {mape:.3f}')
plt.plot(inv_y[test_start:], '-', label="Real Flow")
plt.plot(inv_yhat[test_start:], '--', color='red', label="LSTM Predictions")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show(figsize=(12, 6))
combined = [(inv_yhat[i] + arima.predictions[i]) / 2 for i in range(len(inv_yhat))]
mse = mean_squared_error(inv_y[test_start:], combined[test_start:])
rmse = math.sqrt(mean_squared_error(inv_y[test_start:], combined[test_start:]))
mae = mean_absolute_error(inv_y[test_start:], combined[test_start:])
mape = arima.mean_a_p_e(inv_y[test_start:], combined[test_start:])
print(f'EW Combined Test MAE: {mae:.3f}, MSE: {mse:.3f}, RMSE: {rmse:.3f}, MAPE: {mape:.3f}')
dyn_combined = []
model = GradientBoostingRegressor()
line_train_x, line_train_y = [], []
for i in range(line_test_size - windows_size + 1):
    line_train_x.extend([arima.predictions[i + j][0] for j in range(windows_size)])
    line_train_x.extend([inv_yhat[i + j] for j in range(windows_size)])
    line_train_y.append(inv_y[i + windows_size - 1])
line_train_x = np.array(line_train_x).reshape(line_test_size - windows_size + 1, 2 * windows_size)
model.fit(line_train_x, line_train_y)
line_test_x = []
for i in range(arima.test_size - line_test_size - windows_size + 1):
    line_test_x.extend([arima.predictions[line_test_size + i + j][0] for j in range(windows_size)])
    line_test_x.extend([inv_yhat[line_test_size + i + j] for j in range(windows_size)])
line_test_x = np.array(line_test_x).reshape(arima.test_size - line_test_size - windows_size + 1, 2 * windows_size)
dyn_combined = model.predict(line_test_x)
mse = mean_squared_error(inv_y[test_start:], dyn_combined)
rmse = math.sqrt(mean_squared_error(inv_y[test_start:], dyn_combined))
mae = mean_absolute_error(inv_y[test_start:], dyn_combined)
mape = arima.mean_a_p_e(inv_y[test_start:], dyn_combined)
print(f'Dynamic Combined Test MAE: {mae:.3f}, MSE: {mse:.3f}, RMSE: {rmse:.3f}, MAPE: {mape:.3f}')
plt.figure()
plt.plot(inv_y[test_start:], '-', label="Real Flow")
plt.plot(dyn_combined, '--', color='red', label="Combined Predictions")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show(figsize=(12, 6))