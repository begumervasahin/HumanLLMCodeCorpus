import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from muilt_lstm import series_to_supervised
from sklearn.metrics import mean_squared_error, mean_absolute_error
from keras.models import load_model
from sklearn import linear_model
plt.rcParams['font.family'] = 'SimHei'
def read_and_preprocess_data(file_path):
    dataframe = pd.read_csv(file_path, usecols=[2, 3], engine='python', header=0, index_col=0)
    values = dataframe.values.astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(values)
    return scaler, scaled
def prepare_lstm_data(scaled_data, look_back):
    reframed = series_to_supervised(scaled_data, look_back, 1)
    values = reframed.values
    return values
def make_lstm_predictions(model, test_X):
    yhat = model.predict(test_X.reshape((test_X.shape[0], 1, test_X.shape[1])))
    return yhat
def invert_and_evaluate_predictions(test_y, test_X, inv_yhat, scaler, start_idx):
    inv_yhat = scaler.inverse_transform(np.concatenate((yhat, test_X[:, 1:]), axis=1))[:, 0]
    test_y = test_y.reshape((len(test_y), 1))
    inv_y = scaler.inverse_transform(np.concatenate((test_y, test_X[:, 1:]), axis=1))[:, 0]
    mse = mean_squared_error(inv_y[start_idx:], inv_yhat[start_idx:])
    rmse = math.sqrt(mean_squared_error(inv_y[start_idx:], inv_yhat[start_idx:]))
    mae = mean_absolute_error(inv_y[start_idx:], inv_yhat[start_idx:])
    mape = arima.mean_a_p_e(inv_y[start_idx:], inv_yhat[start_idx:])
    return inv_y, inv_yhat, mse, rmse, mae, mape
def plot_results(inv_y, inv_yhat, label_real='real flow', label_predicted='LSTM'):
    plt.plot(inv_y, '-', label=label_real)
    plt.plot(inv_yhat, '--', color='red', label=label_predicted)
    plt.legend(loc='upper right')
    plt.xlabel("period(15-minute intervals)")
    plt.ylabel("volume(vehicle/period)")
    plt.ylim(0, 800)
    plt.show(figsize=(12, 6))
def main():
    look_back = 10
    line_test_size = 300
    windows_size = 7
    file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    scaler, scaled_data = read_and_preprocess_data(file_path)
    lstm_data = prepare_lstm_data(scaled_data, look_back)
    lstm_model = load_model('../model/lstm-15min.h5')
    lstm_size = arima.start + arima.size - look_back
    test = lstm_data[lstm_size:lstm_size + arima.test_size, :]
    test_X, test_y = test[:, :-1], test[:, -1]
    yhat = make_lstm_predictions(lstm_model, test_X)
    inv_y, inv_yhat, mse, rmse, mae, mape = invert_and_evaluate_predictions(test_y, test_X, yhat, scaler, test_start)
    print(f'LSTM Test MAE: {mae:.3f} MSE: {mse:.3f} RMSE: {rmse:.3f} MAPE: {mape:.3f}')
    plot_results(inv_y, inv_yhat, label_real='real flow', label_predicted='LSTM')
if __name__ == "__main__":
    main()