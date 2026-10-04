import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def parse_datetime(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    return sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred)) / len(y_true)
dataset_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
series = read_csv(
    dataset_path,
    usecols=[2, 3],
    header=0,
    parse_dates=[0],
    index_col=0,
    squeeze=True,
    date_parser=parse_datetime
)
X = series.values.astype('float32')
start_index = 2000
train_size = 1100
test_size = 500
line_test_size = 300
window_size = 10
test_start = line_test_size + window_size - 1
train_data = X[start_index:start_index + train_size]
test_data = X[start_index + train_size:start_index + train_size + test_size]
history = list(train_data)
predictions = []
for t in range(len(test_data)):
    model = ARIMA(history, order=(4, 1, 0))
    model_fit = model.fit(disp=0)
    yhat = model_fit.forecast()[0]
    predictions.append(yhat)
    obs = test_data[t]
    history.append(obs)
    print(f'Predicted: {yhat}, Expected: {obs}')
mse = mean_squared_error(test_data, predictions)
mae = mean_absolute_error(test_data, predictions)
mape = mean_absolute_percentage_error(test_data, predictions)
print(f'ARIMA Test - MAE: {mae:.3f}, MSE: {mse:.3f}, RMSE: {math.sqrt(mse):.3f}, MAPE: {mape:.3f}')
plt.figure(figsize=(12, 6))
plt.plot(test_data[test_start:], '-', label="Real Flow")
plt.plot(predictions[test_start:], '--', color='red', label="ARIMA Predictions")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.title("ARIMA Model Predictions vs Real Flow")
plt.show()