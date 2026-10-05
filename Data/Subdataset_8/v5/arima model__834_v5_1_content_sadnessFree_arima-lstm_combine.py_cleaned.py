import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
import arima
def load_and_preprocess_data(file_path, columns):
    dataframe = pd.read_csv(file_path, usecols=columns, engine='python', header=0, index_col=0)
    values = dataframe.values.astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(values)
    reframed = series_to_supervised(scaled, look_back, 1)
    return reframed, scaler
def inverse_transform_and_reshape(test_X, test_y, yhat, scaler):
    test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
    inv_yhat = scaler.inverse_transform(np.concatenate((yhat, test_X[:, 1:]), axis=1))[:, 0]
    test_y = test_y.reshape((len(test_y), 1))
    inv_y = scaler.inverse_transform(np.concatenate((test_y, test_X[:, 1:]), axis=1))[:, 0]
    return inv_yhat, inv_y
def evaluate_performance(true_values, predicted_values, model_name):
    mse = mean_squared_error(true_values[arima.test_start:], predicted_values[arima.test_start:])
    rmse = math.sqrt(mean_squared_error(true_values[arima.test_start:], predicted_values[arima.test_start:]))
    mae = mean_absolute_error(true_values[arima.test_start:], predicted_values[arima.test_start:])
    mape = arima.mean_a_p_e(true_values[arima.test_start:], predicted_values[arima.test_start:])
    print(f'{model_name} Test MAE: {mae:.3f} MSE: {mse:.3f} RMSE: {rmse:.3f} MAPE: {mape:.3f}')
def plot_predictions(true_values, predicted_values, label, title):
    plt.plot(true_values[arima.test_start:], '-', label="real flow")
    plt.plot(predicted_values[arima.test_start:], '--', color='red', label=label)
    plt.legend(loc='upper right')
    plt.xlabel("period (15-minute intervals)")
    plt.ylabel("volume (vehicle/period)")
    plt.ylim(0, 800)
    plt.title(title)
    plt.show(figsize=(12, 6))
look_back = 10
lstm_model_path = '../model/lstm-15min.h5'
reframed, scaler = load_and_preprocess_data('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', [2, 3])
lstm_size = arima.start + arima.size - look_back
test = reframed.values[lstm_size:lstm_size + arima.test_size, :]
test_X, test_y = test[:, :-1], test[:, -1]
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
lstm_model = load_model(lstm_model_path)
yhat = lstm_model.predict(test_X)
inv_yhat, inv_y = inverse_transform_and_reshape(test_X, test_y, yhat, scaler)
evaluate_performance(inv_y, inv_yhat, 'LSTM')
plot_predictions(inv_y, inv_yhat, 'LSTM', 'LSTM Predictions')
combined = [(inv_yhat[i] + arima.predictions[i]) / 2 for i in range(len(inv_yhat))]
evaluate_performance(inv_y, combined, 'EW combined')
window_size = 1
lstm_error_list = []
arima_error_list = []
lstm_weight = 1
arima_weight = 1
dyn_combined = []
for i in range(len(inv_yhat)):
    if len(lstm_error_list) > 0:
        lstm_error = np.sqrt(np.sum(lstm_error_list[-window_size:]) / window_size)
        arima_error = np.sqrt(np.sum(arima_error_list[-window_size:]) / window_size)
        lstm_weight = (1 - lstm_error / (lstm_error + arima_error)) * 2
        arima_weight = 2 - lstm_weight
    lstm_error_list.append(np.power(inv_yhat[i] - inv_y[i], 2))
    arima_error_list.append(np.power(arima.predictions[i] - inv_y[i], 2))
    dyn_combined.append((lstm_weight * inv_yhat[i] + arima_weight * arima.predictions[i]) / 2)
evaluate_performance(inv_y, dyn_combined, 'Dynamic combined')
plot_predictions(inv_y, dyn_combined, 'Dynamic combined', 'Dynamically Combined Predictions')