import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def mean_absolute_percentage_error(y_true, y_pred):
    sum_errors = 0
    for i in range(len(y_true)):
        sum_errors += abs(y_pred[i] - y_true[i]) / y_true[i]
    return sum_errors / len(y_true)
def date_parser(x):
    return pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def read_data(file_path):
    return pd.read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=date_parser)
def prepare_data(series, train_start, train_end, test_start, test_end):
    X = series.values.astype('float32')
    svr_train = X[train_start:train_end].reshape(-1, 1)
    svr_test = X[test_start - 1:test_end - 1].reshape(-1, 1)
    svr_real = X[test_start:test_end].reshape(-1, 1)
    return svr_train, svr_test, svr_real
def train_svr_model(svr_train):
    model = svm.SVR()
    model.fit(svr_train[:-1], svr_train[1:])
    return model
def evaluate_model(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = math.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true.flatten(), y_pred.flatten()) * 100
    return mse, rmse, mae, mape
def plot_predictions(svr_real, svr_test):
    plt.figure(figsize=(10, 6))
    plt.plot(svr_real, '-', label="Real Flow")
    plt.plot(svr_test, '--', color='red', label="SVR Prediction")
    plt.legend(loc='upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicle/period)")
    plt.ylim(0, 800)
    plt.title("SVR Prediction vs Real Values")
    plt.show()
def plot_real_flow(X, start_period, num_periods):
    plt.figure(figsize=(12, 6))
    plt.plot(X[start_period:start_period + num_periods], '-', color='r', label="Real Flow")
    plt.legend(loc='upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicle/period)")
    plt.title("Real Flow for a Week")
    plt.show()
def main():
    file_path = '/path/to/your/dataset/FEB15-2.csv'
    series = read_data(file_path)
    train_start, train_end = 4500, 6000
    test_start, test_end = 6409, 6600
    svr_train, svr_test, svr_real = prepare_data(series, train_start, train_end, test_start, test_end)
    model = train_svr_model(svr_train)
    predictions = model.predict(svr_test)
    mse, rmse, mae, mape = evaluate_model(svr_real, svr_test)
    print(f'SVR Test MAE: {mae:.3f}, MSE: {mse:.3f}, RMSE: {rmse:.3f}, MAPE: {mape:.3f}%')
    plot_predictions(svr_real, svr_test)
    plot_real_flow(series.values, start_period=31, num_periods=96*7)
if __name__ == "__main__":
    main()