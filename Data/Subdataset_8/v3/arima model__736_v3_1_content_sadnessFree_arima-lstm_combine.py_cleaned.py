import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
import arima
def calculate_mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
def invert_predictions(predictions, scaler, reshape=True):
    inverted = scaler.inverse_transform(predictions)[:, 0]
    return inverted.reshape((len(inverted), 1)) if reshape else inverted
def evaluate_and_print_metrics(true_values, predicted_values, prefix=""):
    mse = mean_squared_error(true_values, predicted_values)
    rmse = math.sqrt(mse)
    mae = mean_absolute_error(true_values, predicted_values)
    mape = calculate_mape(true_values, predicted_values)
    print(f'{prefix}Test MAE: {mae:.3f} MSE: {mse:.3f} RMSE: {rmse:.3f} MAPE: {mape:.3f}')
def plot_predictions(true_values, predicted_values, label_true="Real Flow", label_pred="Predictions"):
    plt.plot(true_values, '-', label=label_true)
    plt.plot(predicted_values, '--', color='red', label=label_pred)
    plt.legend(loc='upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicles/period)")
    plt.ylim(0, 800)
    plt.show(figsize=(12, 6))
look_back = 10
window_size = 1
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
lstm_predictions = lstm_model.predict(test_X)
inv_yhat_lstm = invert_predictions(np.concatenate((lstm_predictions, test_X[:, 1:]), axis=1), scaler)
inv_y_lstm = invert_predictions(np.concatenate((test_y.reshape((len(test_y), 1)), test_X[:, 1:]), axis=1), scaler)
evaluate_and_print_metrics(inv_y_lstm[arima.test_start:], inv_yhat_lstm[arima.test_start:], prefix="LSTM ")
plot_predictions(inv_y_lstm[arima.test_start:], inv_yhat_lstm[arima.test_start:], label_true="Real Flow", label_pred="LSTM Predictions")
combined_predictions = [(inv_yhat_lstm[i] + arima.predictions[i]) / 2 for i in range(len(inv_yhat_lstm))]
evaluate_and_print_metrics(inv_y_lstm[arima.test_start:], combined_predictions[arima.test_start:], prefix="EW Combined ")
plot_predictions(inv_y_lstm[arima.test_start:], combined_predictions[arima.test_start:], label_true="Real Flow", label_pred="Combined Predictions")
lstm_error_list = []
arima_error_list = []
lstm_weight = 1
arima_weight = 1
dyn_combined = []
for i in range(len(inv_yhat_lstm)):
    if len(lstm_error_list) > 0:
        lstm_error = math.sqrt(np.sum(lstm_error_list[-window_size:]) / window_size)
        arima_error = math.sqrt(np.sum(arima_error_list[-window_size:]) / window_size)
        lstm_weight = (1 - lstm_error / (lstm_error + arima_error)) * 2
        arima_weight = 2 - lstm_weight
    lstm_error_list.append((inv_yhat_lstm[i] - inv_y_lstm[i]) ** 2)
    arima_error_list.append((arima.predictions[i] - inv_y_lstm[i]) ** 2)
    dyn_combined.append((lstm_weight * inv_yhat_lstm[i] + arima_weight * arima.predictions[i]) / 2)
evaluate_and_print_metrics(inv_y_lstm[arima.test_start:], dyn_combined[arima.test_start:], prefix="Dynamic Combined ")
plot_predictions(inv_y_lstm[arima.test_start:], dyn_combined[arima.test_start:], label_true="Real Flow", label_pred="Dynamic Combined Predictions")