import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
import arima
def mean_a_p_e(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
look_back = 10
dataframe = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], engine='python', header=0, index_col=0)
values = dataframe.values.astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
reframed = series_to_supervised(scaled, look_back, 1)
values = reframed.values
lstm_size = arima.start + arima.size - look_back
test = values[lstm_size:lstm_size + arima.test_size, :]
test_X, test_y = test[:, :-1], test[:, -1]
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
lstm_model = load_model('../model/lstm-15min.h5')
yhat = lstm_model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
inv_yhat = np.concatenate((yhat, test_X[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:, 0]
test_y = test_y.reshape((len(test_y), 1))
inv_y = np.concatenate((test_y, test_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:, 0]
mse = mean_squared_error(inv_y[arima.test_start:], inv_yhat[arima.test_start:])
rmse = math.sqrt(mse)
mae = mean_absolute_error(inv_y[arima.test_start:], inv_yhat[arima.test_start:])
mape = mean_a_p_e(inv_y[arima.test_start:], inv_yhat[arima.test_start:])
print('LSTM Test MAE: %.3f MSE: %.3f RMSE: %.3f MAPE: %.3f' % (mae, mse, rmse, mape))
plt.plot(inv_y[arima.test_start:], '-', label="real flow")
plt.plot(inv_yhat[arima.test_start:], '--', color='red', label="LSTM")
plt.legend(loc='upper right')
plt.xlabel("period (15-minute intervals)")
plt.ylabel("volume (vehicle/period)")
plt.ylim(0, 800)
plt.show(figsize=(12, 6))
combined = [(inv_yhat[i] + arima.predictions[i]) / 2 for i in range(len(inv_yhat))]
mse = mean_squared_error(inv_y[arima.test_start:], combined[arima.test_start:])
rmse = math.sqrt(mse)
mae = mean_absolute_error(inv_y[arima.test_start:], combined[arima.test_start:])
mape = mean_a_p_e(inv_y[arima.test_start:], combined[arima.test_start:])
print('EW combined Test MAE: %.3f MSE: %.3f RMSE: %.3f MAPE: %.3f' % (mae, mse, rmse, mape))
plt.figure()
plt.plot(inv_y[arima.test_start:], '-', label="real flow")
plt.plot(combined[arima.test_start:], '--', color='red', label="combined")
plt.legend(loc='upper right')
plt.xlabel("period (15-minute intervals)")
plt.ylabel("volume (vehicle/period)")
plt.ylim(0, 800)
plt.show(figsize=(12, 6))
windows_size = 1
lstm_error_list = []
arima_error_list = []
lstm_weight = 1
arima_weight = 1
dyn_combined = []
for i in range(len(inv_yhat)):
    if len(lstm_error_list) > 0:
        lstm_error = math.pow(np.sum(lstm_error_list[-windows_size:]), 1 / 2) / math.pow(windows_size, 1 / 2)
        arima_error = math.pow(np.sum(arima_error_list[-windows_size:]), 1 / 2) / math.pow(windows_size, 1 / 2)
        lstm_weight = (1 - lstm_error / (lstm_error + arima_error)) * 2
        arima_weight = 2 - lstm_weight
    lstm_error_list.append(math.pow(inv_yhat[i] - inv_y[i], 2))
    arima_error_list.append(math.pow(arima.predictions[i] - inv_y[i], 2))
    dyn_combined.append((lstm_weight * inv_yhat[i] + arima_weight * arima.predictions[i]) / 2)
mse = mean_squared_error(inv_y[arima.test_start:], dyn_combined[arima.test_start:])
rmse = math.sqrt(mse)
mae = mean_absolute_error(inv_y[arima.test_start:], dyn_combined[arima.test_start:])
mape = mean_a_p_e(inv_y[arima.test_start:], dyn_combined[arima.test_start:])
print('Dyn combined Test MAE: %.3f MSE: %.3f RMSE: %.3f MAPE: %.3f' % (mae, mse, rmse, mape))
plt.figure()
plt.plot(inv_y[arima.test_start:], '-', label="real flow")
plt.plot(dyn_combined[arima.test_start:], '--', color='red', label="combined")
plt.legend(loc='upper right')
plt.xlabel("period (15-minute intervals)")
plt.ylabel("volume (vehicle/period)")
plt.ylim(0, 800)
plt.show(figsize=(12, 6))