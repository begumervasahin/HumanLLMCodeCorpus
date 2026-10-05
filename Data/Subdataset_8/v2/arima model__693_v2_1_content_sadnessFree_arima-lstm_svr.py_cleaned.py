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
    return (sum_errors / len(y_true)) * 100
def parse_datetime(x):
    return pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
dataset_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
data = pd.read_csv(dataset_path, usecols=[2, 3], header=0, parse_dates=[0],
                   index_col=0, squeeze=True, date_parser=parse_datetime)
data_values = data.values.astype('float32')
train_start, train_end = 4500, 6000
test_start, test_end = 6409, 6600
train_data = data_values[train_start:train_end].reshape(-1, 1)
test_data = data_values[test_start - 1:test_end - 1].reshape(-1, 1)
real_data = data_values[test_start:test_end].reshape(-1, 1)
svr_model = svm.SVR()
svr_model.fit(train_data[:-1], train_data[1:])
predictions = svr_model.predict(test_data)
mse = mean_squared_error(real_data, test_data)
rmse = math.sqrt(mse)
mae = mean_absolute_error(real_data, test_data)
mape = mean_absolute_percentage_error(real_data.flatten(), test_data.flatten())
print('Support Vector Regression Evaluation:')
print('MAE: {:.3f}, MSE: {:.3f}, RMSE: {:.3f}, MAPE: {:.3f}%'.format(mae, mse, rmse, mape))
plt.plot(real_data, '-', label="Real Flow")
plt.plot(test_data, '--', color='red', label="SVR Prediction")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.title('SVR Prediction vs Real Flow')
plt.show()
start_day = 31
plt.figure(figsize=(12, 6))
plt.plot(data_values[start_day:start_day + 96*7], '-', color='r', label="Real Flow")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title('Real Flow for a Week')
plt.show()