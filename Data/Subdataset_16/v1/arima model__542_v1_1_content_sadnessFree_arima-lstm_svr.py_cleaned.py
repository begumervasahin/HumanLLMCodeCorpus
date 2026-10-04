import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from pandas import read_csv
from datetime import datetime
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
def fonk2(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
b1 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0, parse_dates=[0],
                  b2 = 0, date_parser=parser)
b3 = b1.values
b3 = b3.astype('float32')
a2 = 4500
a3 = 6000
a4 = 6409
a5 = 6600
b4 = b3[a2:a3]
b5 = b3[a4 - 1:a5 - 1]
b6 = np.array(b3[a4:a5]).reshape(-1, 1)
b4 = np.array(b4).reshape(-1, 1)
b5 = np.array(b5).reshape(-1, 1)
b7 = svm.SVR()
b7.fit(b4[0:a3 - a2 - 1], b4[1:a3 - a2])
b8 = b7.predict(b5)
b9 = mean_squared_error(b6, b5)
b10 = math.sqrt(mean_squared_error(b6, b5))
b11 = mean_absolute_error(b6, b5)
b12 = fonk1(b6, b5)
print('SVR Test MAE: %.3f MSE: %.3f RMSE: %.3f MAPE: %.3f' % (b11, b9, b10, b12))
plt.figure(b13 = (12, 6))
plt.plot(b6, '-', b14 = "Real Flow")
plt.plot(b5, '--', b15 = 'red', b14="SVR")
plt.legend(b16 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()
a6 = 31
plt.figure(b13 = (12, 6))
plt.plot(b3[a6:a6 + 96*7], '-', b15 = 'r', b14="Real Flow")
plt.legend(b16 = 'upper right')
plt.xlabel("Period (15min)")
plt.ylabel("Traffic Volume (vehicles/period)")
plt.show()