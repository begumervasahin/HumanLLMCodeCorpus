import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
def fonk2(x):
    return pd.to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
b2 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0,
                     b3 = [0], index_col=0, squeeze=True, date_parser=parser)
b4 = b2.values.astype('float32')
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
print('SVR Test MAE: {:.3f}, MSE: {:.3f}, RMSE: {:.3f}, MAPE: {:.3f}%'.b1(b14, b12, b13, b15))
plt.plot(b9, '-', b16 = "Real Flow")
plt.plot(b8, '--', b17 = 'red', b16="SVR Prediction")
plt.legend(b18 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()
a2 = 31
plt.figure(b19 = (12, 6))
plt.plot(b4[a2:a2 + 96*7], '-', b17 = 'r', b16="Real Flow")
plt.legend(b18 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.show()