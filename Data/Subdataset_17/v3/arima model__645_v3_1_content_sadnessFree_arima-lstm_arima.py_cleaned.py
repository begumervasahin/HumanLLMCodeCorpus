import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def parse_dates(date_str):
    return to_datetime(date_str, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return total_error / len(y_true)
def load_dataset(file_path, usecols, date_col, parser_func):
    return read_csv(file_path, usecols=usecols, header=0, parse_dates=[date_col], index_col=date_col, date_parser=parser_func)
def train_arima_model(history, order):
    model = ARIMA(history, order=order)
    return model.fit()
def plot_results(real_data, predictions, start_idx):
    plt.plot(real_data[start_idx:], '-', label="Real Flow")
    plt.plot(predictions[start_idx:], '--', color='red', label="ARIMA")
    plt.legend(loc='upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicle/period)")
    plt.ylim(0, 800)
    plt.gcf().set_size_inches(12, 6)
    plt.show()
FILE_PATH = 'path/to/your/FEB15-2.csv'
USECOLS = [2, 3]
DATE_COL = 0
START_IDX = 2000
TRAIN_SIZE = 1100
TEST_SIZE = 500
LINE_TEST_SIZE = 300
WINDOW_SIZE = 10
TEST_START_IDX = LINE_TEST_SIZE + WINDOW_SIZE - 1
ARIMA_ORDER = (4, 1, 0)
series = load_dataset(FILE_PATH, USECOLS, DATE_COL, parse_dates)
X = series.values.astype('float32')
train_data = X[START_IDX:START_IDX + TRAIN_SIZE]
test_data = X[START_IDX + TRAIN_SIZE:START_IDX + TRAIN_SIZE + TEST_SIZE]
history = list(train_data)
predictions = []
for t in range(len(test_data)):
    model_fit = train_arima_model(history, ARIMA_ORDER)
    forecast = model_fit.forecast()
    predicted_value = forecast[0]
    predictions.append(predicted_value)
    observed_value = test_data[t]
    history.append(observed_value)
    print(f'predicted={predicted_value[0]:.6f}, expected={observed_value[0]:.6f}')
mse = mean_squared_error(test_data, predictions)
mae = mean_absolute_error(test_data, predictions)
mape = mean_absolute_percentage_error(test_data, predictions)
rmse = math.sqrt(mse)
print(f'ARIMA Test MAE: {mae:.3f} MSE: {mse:.3f} RMSE: {rmse:.3f} MAPE: {mape:.3f}')
plot_results(test_data, predictions, TEST_START_IDX)