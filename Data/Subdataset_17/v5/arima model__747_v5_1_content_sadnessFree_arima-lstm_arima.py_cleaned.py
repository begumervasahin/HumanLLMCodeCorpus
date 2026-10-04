import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def parser(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    return sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true))) / len(y_true)
def load_dataset(filepath):
    return read_csv(filepath, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser).values.astype('float32')
def train_arima_model(history, order=(4, 1, 0)):
    model = ARIMA(history, order=order)
    model_fit = model.fit()
    return model_fit.forecast()[0]
def calculate_errors(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true, y_pred)
    print(f'ARIMA Test MAE: {mae:.3f}, MSE: {mse:.3f}, RMSE: {math.sqrt(mse):.3f}, MAPE: {mape:.3f}')
    return mae, mse, math.sqrt(mse), mape
def plot_results(real, predicted, test_start, ylabel="Volume (vehicle/period)"):
    plt.figure(figsize=(12, 6))
    plt.plot(real[test_start:], '-', label="Real flow")
    plt.plot(predicted[test_start:], '--', color='red', label="ARIMA")
    plt.legend(loc='upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel(ylabel)
    plt.ylim(0, 800)
    plt.show()
def main():
    filepath = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    X = load_dataset(filepath)
    start = 2000
    size = 1100
    test_size = 500
    line_test_size = 300
    windows_size = 10
    test_start = line_test_size + windows_size - 1
    arima_train, arima_test = X[start:start + size], X[start + size:start + size + test_size]
    history = list(arima_train)
    predictions = []
    for t in range(len(arima_test)):
        yhat = train_arima_model(history)
        predictions.append(yhat)
        obs = arima_test[t]
        history.append(obs)
        print(f'predicted={yhat:.6f}, expected={obs:.6f}')
    calculate_errors(arima_test, predictions)
    plot_results(arima_test, predictions, test_start)
if __name__ == "__main__":
    main()