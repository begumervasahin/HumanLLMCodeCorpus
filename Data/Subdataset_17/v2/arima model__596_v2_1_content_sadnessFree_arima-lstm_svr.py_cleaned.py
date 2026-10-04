import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
from datetime import datetime
def mean_a_p_e(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true))
def parser(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
series = pd.read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
X = series.values.astype('float32')
train_start, train_end = 4500, 6000
test_start, test_end = 6409, 6600
svr_train = X[train_start:train_end].reshape(-1, 1)
svr_test = X[test_start-1:test_end-1].reshape(-1, 1)
svr_real = X[test_start:test_end].reshape(-1, 1)
model = svm.SVR()
model.fit(svr_train[:-1], svr_train[1:])
predictions = model.predict(svr_test)
mse = mean_squared_error(svr_real, svr_test)
rmse = math.sqrt(mse)
mae = mean_absolute_error(svr_real, svr_test)
mape = mean_a_p_e(svr_real, svr_test)
print(f'SVR Test MAE: {mae:.3f} MSE: {mse:.3f} RMSE: {rmse:.3f} MAPE: {mape:.3f}')
plt.figure(figsize=(12, 6))
plt.plot(svr_real, '-', label="Real Flow")
plt.plot(svr_test, '--', color='red', label="SVR")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()
dat_start = 31
plt.figure(figsize=(12, 6))
plt.plot(X[dat_start:dat_start + 96*7], '-', color='r', label="Real Flow")
plt.legend(loc='upper right')
plt.xlabel("Period (15min)")
plt.ylabel("Traffic Volume (vehicles/period)")
plt.show()