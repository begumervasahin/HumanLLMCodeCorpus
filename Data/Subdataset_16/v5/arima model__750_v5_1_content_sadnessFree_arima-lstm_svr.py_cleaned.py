import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(y_true, y_pred):
    b1 = np.mean(np.abs((y_true - y_pred) / y_true))
    return b1
def fonk2(x):
    return pd.to_datetime(x, b2 = '%Y-%m-%d %H:%M:%S')
b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b4 = pd.read_csv(b3, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
b5 = b4.values.astype('float32')
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
b1 = fonk1(b10, b9)
print(f'SVR Test MAE: {b15:.3f} MSE: {b13:.3f} RMSE: {b14:.3f} MAPE: {b1:.3f}')
plt.figure(b16 = (12, 6))
plt.plot(b10, '-', b17 = "Real Flow")
plt.plot(b9, '--', b18 = 'red', b17="SVR Predicted")
plt.legend(b19 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()
a1 = 31
plt.figure(b16 = (12, 6))
plt.plot(b5[a1:a1 + 96*7], '-', b18 = 'r', b17="çå®æµé")
plt.legend(b19 = 'upper right')
plt.xlabel("å¨æ(15min)")
plt.ylabel("è½¦æµé(è½¦è¾æ°/å¨æï¼")
plt.show()