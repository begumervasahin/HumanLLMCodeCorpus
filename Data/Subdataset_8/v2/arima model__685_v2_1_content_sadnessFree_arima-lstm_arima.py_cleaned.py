import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
import statsmodels.tsa.stattools as st
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def parser(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    sum_percentage_error = 0
    for i in range(len(y_true)):
        sum_percentage_error += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return sum_percentage_error / len(y_true)
dataset_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
series = read_csv(dataset_path, usecols=[2, 3], header=0, parse_dates=[0],
                  index_col=0, squeeze=True, date_parser=parser)
data_values = series.values.astype('float32')
train_start = 2000
train_size = 1100
test_size = 500
line_test_size = 300
window_size = 10
test_start = line_test_size + window_size - 1
train_data, test_data = data_values[train_start:train_start + train_size], data_values[train_start + train_size:train_start + train_size + test_size]
history = [x for x in train_data]
predictions = []
for t in range(len(test_data)):
    model = ARIMA(history, order=(4, 1, 0))
    model_fit = model.fit(disp=0)
    forecast = model_fit.forecast()
    predicted_value = forecast[0]
    predictions.append(predicted_value)
    observed_value = test_data[t]
    history.append(observed_value)
    print(f'Predicted: {predicted_value}, Expected: {observed_value}')
mse = mean_squared_error(test_data, predictions)
mae = mean_absolute_error(test_data, predictions)
mape = mean_absolute_percentage_error(test_data, predictions)
print(f'ARIMA Test MAE: {mae:.3f}, MSE: {mse:.3f}, RMSE: {math.sqrt(mse):.3f}, MAPE: {mape:.3f}')
plt.plot(test_data[test_start:], '-', label="Real Flow")
plt.plot(predictions[test_start:], '--', color='red', label="ARIMA Predictions")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show(figsize=(12, 6))