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
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b3 = pd.read_csv(b2, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
b4 = b3.values.astype('float32')
a2 = 4500
a3 = 6000
a4 = 6409
a5 = 6600
b5 = b4[a2:a3].reshape(-1, 1)
b6 = b4[a4 - 1:a5 - 1].reshape(-1, 1)
b7 = b4[a4:a5].reshape(-1, 1)
b8 = svm.SVR()
b8.fit(b5[:-1], b5[1:])
b9 = b8.predict(b6)
b10 = mean_squared_error(b7, b6)
b11 = math.sqrt(b10)
b12 = mean_absolute_error(b7, b6)
b13 = fonk1(b7, b6)
print(f'SVR Test MAE: {b12:.3f} MSE: {b10:.3f} RMSE: {b11:.3f} MAPE: {b13:.3f}')
plt.figure(b14 = (12, 6))
plt.plot(b7, '-', b15 = "Real Flow")
plt.plot(b6, '--', b16 = 'red', b15="SVR Predicted")
plt.legend(b17 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()
a6 = 31
plt.figure(b14 = (12, 6))
plt.plot(b4[a6:a6 + 96*7], '-', b16 = 'r', b15="çå®æµé")
plt.legend(b17 = 'upper right')
plt.xlabel("å¨æ(15min)")
plt.ylabel("è½¦æµé(è½¦è¾æ°/å¨æï¼")
plt.show()