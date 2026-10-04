import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def mean_a_p_e(y_true, y_pred):
    sum_errors = 0
    for i in range(len(y_true)):
        sum_errors += abs(y_pred[i] - y_true[i]) / y_true[i]
    return sum_errors / len(y_true)
def parser(x):
    return pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
series = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0,
                     parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
X = series.values.astype('float32')
train_start, train_end = 4500, 6000
test_start, test_end = 6409, 6600
svr_train = X[train_start:train_end].reshape(-1, 1)
svr_test = X[test_start - 1:test_end - 1].reshape(-1, 1)
svr_real = X[test_start:test_end].reshape(-1, 1)
model = svm.SVR()
model.fit(svr_train[:-1], svr_train[1:])
predictions = model.predict(svr_test)
mse = mean_squared_error(svr_real, svr_test)
rmse = math.sqrt(mse)
mae = mean_absolute_error(svr_real, svr_test)
mape = mean_a_p_e(svr_real.flatten(), svr_test.flatten()) * 100
print('SVR Test MAE: {:.3f}, MSE: {:.3f}, RMSE: {:.3f}, MAPE: {:.3f}%'.format(mae, mse, rmse, mape))
plt.figure(figsize=(10, 5))
plt.plot(svr_real, '-', label="Real Flow")
plt.plot(svr_test, '--', color='red', label="SVR Prediction")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.title("SVR Prediction vs Real Values")
plt.show()
dat_start = 31
plt.figure(figsize=(12, 6))
plt.plot(X[dat_start:dat_start + 96*7], '-', color='r', label="Real Flow")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Real Flow for a Week")
plt.show()