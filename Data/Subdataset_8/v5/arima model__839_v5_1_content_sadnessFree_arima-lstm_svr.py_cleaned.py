import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def mean_absolute_percentage_error(y_true, y_pred):
    abs_error = np.abs(y_true - y_pred)
    return np.mean(abs_error / y_true) * 100
def parse_datetime(x):
    return pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
data = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv',
                   usecols=[2, 3],
                   header=0,
                   parse_dates=[0],
                   index_col=0,
                   squeeze=True,
                   date_parser=parse_datetime)
values = data.values.astype('float32')
train_start_index, train_end_index = 4500, 6000
test_start_index, test_end_index = 6409, 6600
train_data = values[train_start_index:train_end_index]
test_data = values[test_start_index - 1:test_end_index - 1]
real_test_data = values[test_start_index:test_end_index].reshape(-1, 1)
train_data = train_data.reshape(-1, 1)
test_data = test_data.reshape(-1, 1)
model = svm.SVR()
model.fit(train_data[:-1], train_data[1:])
predicted_values = model.predict(test_data)
mse = mean_squared_error(real_test_data, test_data)
rmse = math.sqrt(mse)
mae = mean_absolute_error(real_test_data, test_data)
mape = mean_absolute_percentage_error(real_test_data, test_data)
print('SVR Test MAE: %.3f, MSE: %.3f, RMSE: %.3f, MAPE: %.3f%%' % (mae, mse, rmse, mape))
plt.plot(real_test_data, label="Real Flow")
plt.plot(predicted_values, '--', color='red', label="SVR Predictions")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicles/period)")
plt.ylim(0, 800)
plt.show()
start_index = 31
plt.figure(figsize=(12, 6))
plt.plot(values[start_index:start_index + 96*7], label="Real Traffic Flow", color='r')
plt.legend(loc='upper right')
plt.xlabel("Period (15 minutes)")
plt.ylabel("Traffic Volume (vehicles/period)")
plt.show()