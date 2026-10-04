import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def mean_a_p_e(y_true, y_pred):
    sum = 0
    for i in range(len(y_true)):
        sum += abs(y_pred[i] - y_true[i]) / y_true[i]
    return sum / len(y_true)
def parser(x):
    return pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
series = pd.read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
X = series.values.astype('float32')
train_start = 4500
train_end = 6000
test_start = 6409
test_end = 6600
svr_train = X[train_start:train_end].reshape(-1, 1)
svr_test = X[test_start - 1:test_end - 1].reshape(-1, 1)
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
plt.plot(svr_test, '--', color='red', label="SVR Predicted")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()
datStart = 31
plt.figure(figsize=(12, 6))
plt.plot(X[datStart:datStart + 96*7], '-', color='r', label="çå®æµé")
plt.legend(loc='upper right')
plt.xlabel("å¨æ(15min)")
plt.ylabel("è½¦æµé(è½¦è¾æ°/å¨æï¼")
plt.show()