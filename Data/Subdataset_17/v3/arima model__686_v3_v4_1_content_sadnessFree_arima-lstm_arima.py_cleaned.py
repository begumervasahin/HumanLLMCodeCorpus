import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def parser(date_string):
    return to_datetime(date_string, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    sum_error = 0
    for i in range(len(y_true)):
        sum_error += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return sum_error / len(y_true)
def load_dataset(filepath, date_col, value_cols):
    series = read_csv(filepath, usecols=value_cols, header=0, parse_dates=[date_col], index_col=0, squeeze=True, date_parser=parser)
    return series.values.astype('float32')
def split_dataset(data, start_idx, train_size, test_size):
    train = data[start_idx:start_idx + train_size]
    test = data[start_idx + train_size:start_idx + train_size + test_size]
    return train, test
def arima_forecast(train, test, order):
    history = list(train)
    predictions = []
    for t in range(len(test)):
        model = ARIMA(history, order=order)
        model_fit = model.fit()
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        print(f'Predicted: {yhat}, Expected: {obs}')
    return predictions
def evaluate_model(test, predictions):
    mse = mean_squared_error(test, predictions)
    mae = mean_absolute_error(test, predictions)
    mape = mean_absolute_percentage_error(test, predictions)
    return mae, mse, mape
def plot_results(test, predictions, test_start, title='ARIMA Model Results'):
    plt.figure(figsize=(12, 6))
    plt.plot(test[test_start:], '-', label="Real Flow")
    plt.plot(predictions[test_start:], '--', color='red', label="ARIMA")
    plt.legend(loc='upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (Vehicle/Period)")
    plt.ylim(0, 800)
    plt.title(title)
    plt.show()
def main():
    DATASET_PATH = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    DATE_COL = 2
    VALUE_COLS = [2, 3]
    START_INDEX = 2000
    TRAIN_SIZE = 1100
    TEST_SIZE = 500
    LINE_TEST_SIZE = 300
    WINDOWS_SIZE = 10
    TEST_START = LINE_TEST_SIZE + WINDOWS_SIZE - 1
    ARIMA_ORDER = (4, 1, 0)
    data = load_dataset(DATASET_PATH, DATE_COL, VALUE_COLS)
    train, test = split_dataset(data, START_INDEX, TRAIN_SIZE, TEST_SIZE)
    predictions = arima_forecast(train, test, ARIMA_ORDER)
    mae, mse, mape = evaluate_model(test, predictions)
    print(f'ARIMA Test - MAE: {mae:.3f}, MSE: {mse:.3f}, RMSE: {math.sqrt(mse):.3f}, MAPE: {mape:.3f}')
    plot_results(test, predictions, TEST_START)
if __name__ == "__main__":
    main()