import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += abs(y_pred[i] - y_true[i]) / y_true[i]
    return (a1 / len(y_true)) * 100
def fonk2(x):
    return pd.to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b3 = pd.read_csv(b2, usecols=[2, 3], header=0, parse_dates=[0],
                   b4 = 0, squeeze=True, date_parser=parse_datetime)
b5 = b3.values.astype('float32')
train_start, b6 = 4500, 6000
test_start, b7 = 6409, 6600
b8 = b5[train_start:b6].reshape(-1, 1)
b9 = b5[test_start - 1:b7 - 1].reshape(-1, 1)
b10 = b5[test_start:b7].reshape(-1, 1)
b11 = svm.SVR()
b11.fit(b8[:-1], b8[1:])
b12 = b11.predict(b9)
b13 = mean_squared_error(b10, b9)
b14 = math.sqrt(b13)
b15 = mean_absolute_error(b10, b9)
b16 = fonk1(b10.flatten(), b9.flatten())
print('Support Vector Regression Evaluation:')
print('MAE: {:.3f}, MSE: {:.3f}, RMSE: {:.3f}, MAPE: {:.3f}%'.b1(b15, b13, b14, b16))
plt.plot(b10, '-', b17 = "Real Flow")
plt.plot(b9, '--', b18 = 'red', b17="SVR Prediction")
plt.legend(b19 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.title('SVR Prediction vs Real Flow')
plt.show()
a2 = 31
plt.figure(b20 = (12, 6))
plt.plot(b5[a2:a2 + 96*7], '-', b18 = 'r', b17="Real Flow")
plt.legend(b19 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title('Real Flow for a Week')
plt.show()