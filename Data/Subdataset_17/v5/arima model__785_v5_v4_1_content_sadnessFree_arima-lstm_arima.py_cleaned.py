import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def parse_date(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    return sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true))) / len(y_true)
def load_dataset(filepath, date_column, value_column, date_parser):
    series = read_csv(filepath, usecols=[date_column, value_column], header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=date_parser)
    return series.values.astype('float32')
def split_dataset(data, start_index, train_size, test_size):
    train_data = data[start_index:start_index + train_size]
    test_data = data[start_index + train_size:start_index + train_size + test_size]
    return train_data, test_data
def arima_forecasting(train_data, test_data, order=(4, 1, 0)):
    history = list(train_data)
    predictions = []
    for t in range(len(test_data)):
        model = ARIMA(history, order=order)
        model_fit = model.fit()
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(test_data[t])
        print(f'Predicted: {yhat}, Expected: {test_data[t]}')
    return predictions
def evaluate_forecast(test_data, predictions):
    mse = mean_squared_error(test_data, predictions)
    mae = mean_absolute_error(test_data, predictions)
    mape = mean_absolute_percentage_error(test_data, predictions)
    rmse = math.sqrt(mse)
    print(f'ARIMA Test - MAE: {mae:.3f}, MSE: {mse:.3f}, RMSE: {rmse:.3f}, MAPE: {mape:.3f}')
    return mse, mae, mape, rmse
def plot_results(test_data, predictions, test_start, title, xlabel, ylabel, ylim, figsize=(12, 6)):
    plt.figure(figsize=figsize)
    plt.plot(test_data[test_start:], '-', label="Real Flow")
    plt.plot(predictions[test_start:], '--', color='red', label="ARIMA")
    plt.legend(loc='upper right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(ylim)
    plt.title(title)
    plt.show()
if __name__ == "__main__":
    dataset_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    DATE_COLUMN = 2
    VALUE_COLUMN = 3
    START_INDEX = 2000
    TRAIN_SIZE = 1100
    TEST_SIZE = 500
    LINE_TEST_SIZE = 300
    WINDOW_SIZE = 10
    TEST_START = LINE_TEST_SIZE + WINDOW_SIZE - 1
    data_values = load_dataset(dataset_path, DATE_COLUMN, VALUE_COLUMN, parse_date)
    train_data, test_data = split_dataset(data_values, START_INDEX, TRAIN_SIZE, TEST_SIZE)
    predictions = arima_forecasting(train_data, test_data)
    mse, mae, mape, rmse = evaluate_forecast(test_data, predictions)
    plot_results(
        test_data, predictions, TEST_START,
        title="ARIMA Model Predictions vs Real Data",
        xlabel="Period (15-minute intervals)",
        ylabel="Volume (Vehicle/Period)",
        ylim=(0, 800)
    )