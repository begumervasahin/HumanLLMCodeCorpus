import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(y_true, y_pred):
    b1 = np.abs(y_true - y_pred)
    return np.mean(b1 / y_true) * 100
def fonk2(x):
    return pd.to_datetime(x, b2 = '%Y-%m-%d %H:%M:%S')
b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b4 = pd.read_csv(b3, usecols=[2, 3], header=0, parse_dates=[0],
                   b5 = 0, squeeze=True, date_parser=parse_datetime)
b6 = b4.values.astype('float32')
train_start, b7 = 4500, 6000
test_start, b8 = 6409, 6600
b9 = b6[train_start:b7].reshape(-1, 1)
b10 = b6[test_start - 1:b8 - 1].reshape(-1, 1)
b11 = b6[test_start:b8].reshape(-1, 1)
b12 = svm.SVR()
b12.fit(b9[:-1], b9[1:])
b13 = b12.predict(b10)
b14 = mean_squared_error(b11, b10)
b15 = np.sqrt(b14)
b16 = mean_absolute_error(b11, b10)
b17 = fonk1(b11.flatten(), b10.flatten())
print('Support Vector Regression Evaluation:')
print(f'MAE: {b16:.3f}, MSE: {b14:.3f}, RMSE: {b15:.3f}, MAPE: {b17:.3f}%')
plt.plot(b11, '-', b18 = "Real Flow")
plt.plot(b10, '--', b19 = 'red', b18="SVR Prediction")
plt.legend(b20 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.title('SVR Prediction vs Real Flow')
plt.show()
a1 = 31
plt.figure(b21 = (12, 6))
plt.plot(b6[a1:a1 + 96*7], '-', b19 = 'r', b18="Real Flow")
plt.legend(b20 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title('Real Flow for a Week')
plt.show()