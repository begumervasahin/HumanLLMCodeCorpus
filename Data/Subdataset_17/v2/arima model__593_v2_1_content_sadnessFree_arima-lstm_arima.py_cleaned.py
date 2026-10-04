import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def parser(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return total_error / len(y_true)
file_path = 'path/to/your/FEB15-2.csv'
series = read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
X = series.values.astype('float32')
start_idx = 2000
train_size = 1100
test_size = 500
line_test_size = 300
window_size = 10
test_start_idx = line_test_size + window_size - 1
train_data, test_data = X[start_idx:start_idx + train_size], X[start_idx + train_size:start_idx + train_size + test_size]
history = list(train_data)
predictions = []
for t in range(len(test_data)):
    model = ARIMA(history, order=(4, 1, 0))
    model_fit = model.fit()
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
plt.plot(test_data[test_start_idx:], '-', label="Real Flow")
plt.plot(predictions[test_start_idx:], '--', color='red', label="ARIMA")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.gcf().set_size_inches(12, 6)
plt.show()