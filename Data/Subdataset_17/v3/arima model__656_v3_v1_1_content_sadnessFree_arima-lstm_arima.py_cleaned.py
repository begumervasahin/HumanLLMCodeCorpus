import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def parser(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_a_p_e(y_true, y_pred):
    total = sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return total / len(y_true)
def load_dataset(filepath):
    return read_csv(filepath, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
def prepare_data(series):
    X = series.values.astype('float32')
    start, size, test_size = 2000, 1100, 500
    line_test_size, windows_size = 300, 10
    test_start = line_test_size + windows_size - 1
    train_data = X[start:start + size]
    test_data = X[start + size:start + size + test_size]
    return train_data, test_data, test_start
def arima_forecast(train, test):
    history = list(train)
    predictions = []
    for t in range(len(test)):
        model = ARIMA(history, order=(4, 1, 0))
        model_fit = model.fit()
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(test[t])
        print(f'predicted={yhat:.6f}, expected={test[t]:.6f}')
    return predictions
def calculate_metrics(test, predictions):
    mse = mean_squared_error(test, predictions)
    mae = mean_absolute_error(test, predictions)
    rmse = math.sqrt(mse)
    mape = mean_a_p_e(test, predictions)
    print(f'ARIMA Test MAE: {mae:.3f} MSE: {mse:.3f} RMSE: {rmse:.3f} MAPE: {mape:.3f}')
    return mse, mae, rmse, mape
def plot_results(test, predictions, test_start):
    plt.figure(figsize=(12, 6))
    plt.plot(test[test_start:], '-', label="Real Flow")
    plt.plot(predictions[test_start:], '--', color='red', label="ARIMA Predictions")
    plt.legend(loc='upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicle/period)")
    plt.ylim(0, 800)
    plt.show()
if __name__ == "__main__":
    filepath = '/path/to/your/FEB15-2.csv'
    series = load_dataset(filepath)
    train_data, test_data, test_start = prepare_data(series)
    predictions = arima_forecast(train_data, test_data)
    calculate_metrics(test_data, predictions)
    plot_results(test_data, predictions, test_start)