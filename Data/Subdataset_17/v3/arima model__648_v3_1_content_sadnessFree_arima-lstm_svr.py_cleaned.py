import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
from datetime import datetime
def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true))
def date_parser(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
series = pd.read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=date_parser)
data = series.values.astype('float32')
TRAIN_START, TRAIN_END = 4500, 6000
TEST_START, TEST_END = 6409, 6600
train_data = data[TRAIN_START:TRAIN_END].reshape(-1, 1)
test_data = data[TEST_START-1:TEST_END-1].reshape(-1, 1)
real_data = data[TEST_START:TEST_END].reshape(-1, 1)
svr_model = svm.SVR()
svr_model.fit(train_data[:-1], train_data[1:])
predictions = svr_model.predict(test_data)
mse = mean_squared_error(real_data, test_data)
rmse = math.sqrt(mse)
mae = mean_absolute_error(real_data, test_data)
mape = mean_absolute_percentage_error(real_data, test_data)
print(f'SVR Test MAE: {mae:.3f} MSE: {mse:.3f} RMSE: {rmse:.3f} MAPE: {mape:.3f}')
plt.figure(figsize=(12, 6))
plt.plot(real_data, '-', label="Real Flow")
plt.plot(test_data, '--', color='red', label="SVR")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()
DATA_START = 31
plt.figure(figsize=(12, 6))
plt.plot(data[DATA_START:DATA_START + 96*7], '-', color='r', label="Real Flow")
plt.legend(loc='upper right')
plt.xlabel("Period (15min)")
plt.ylabel("Traffic Volume (vehicles/period)")
plt.show()