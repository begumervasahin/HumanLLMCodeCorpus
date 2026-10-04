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
    return a1 / len(y_true)
def fonk2(x):
    return pd.to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
b2 = '/path/to/your/dataset/FEB15-2.csv'
b3 = pd.read_csv(b2, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
b4 = b3.values.astype('float32')
train_start, b5 = 4500, 6000
test_start, b6 = 6409, 6600
b7 = b4[train_start:b5].reshape(-1, 1)
b8 = b4[test_start - 1:b6 - 1].reshape(-1, 1)
b9 = b4[test_start:b6].reshape(-1, 1)
b10 = svm.SVR()
b10.fit(b7[:-1], b7[1:])
b11 = b10.predict(b8)
b12 = mean_squared_error(b9, b8)
b13 = math.sqrt(b12)
b14 = mean_absolute_error(b9, b8)
b15 = fonk1(b9.flatten(), b8.flatten()) * 100
print(f'SVR Test MAE: {b14:.3f}, MSE: {b12:.3f}, RMSE: {b13:.3f}, MAPE: {b15:.3f}%')
plt.figure(b16 = (10, 6))
plt.plot(b9, '-', b17 = "Real Flow")
plt.plot(b8, '--', b18 = 'red', b17="SVR Prediction")
plt.legend(b19 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.title("SVR Prediction vs Real Values")
plt.show()
a2 = 31
plt.figure(b16 = (12, 6))
plt.plot(b4[a2:a2 + 96*7], '-', b18 = 'r', b17="Real Flow")
plt.legend(b19 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Real Flow for a Week")
plt.show()