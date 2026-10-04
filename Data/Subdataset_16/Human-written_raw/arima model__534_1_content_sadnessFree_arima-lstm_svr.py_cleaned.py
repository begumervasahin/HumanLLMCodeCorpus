import pandas
import numpy
import math
import matplotlib
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import datetime
from sklearn import svm
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from pandas import concat
from pandas import DataFrame
def fonk1(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
def fonk2(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
b1 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0, parse_dates=[0],
                  b2 = 0,
                  b3 = True,
                  b4 = parser)
b5 = b1.values
b5 = b5.astype('float32')
a2 = 4500
a3 = 6000
a4 = 6409
a5 = 6600
b8, b6 = b5[a2:a3], b5[a4 - 1:a5 - 1]
b7 = numpy.array(b5[a4:a5]).reshape(-1, 1)
b8 = numpy.array(b8).reshape(-1, 1)
b6 = numpy.array(b6).reshape(-1, 1)
b9 = svm.SVR()
b9.fit(b8[0:a3 - a2 - 1], b8[1:a3 - a2])
b10 = b9.predict(b6)
b11 = mean_squared_error(b7, b6)
b12 = math.sqrt(mean_squared_error(b7, b6))
b13 = mean_absolute_error(b7, b6)
b14 = fonk1(b7, b6)
print('SVR Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b13, b11, b12, b14))
plt.plot(b7, '-', b15 = "real flow")
plt.plot(b6, '--', b16 = 'red', b15="SVR")
plt.legend(b17 = 'upper right')
plt.xlabel("period(15-minute intervals)")
plt.ylabel("volume(vehicle/period)")
plt.ylim(0, 800)
plt.show(b18 = (12, 6))
a6 = 31
matplotlib.rcParams['font.family'] = 'SimHei'
plt.figure(b18 = (12, 6))
plt.plot(b5[a6:a6 + 96*7], '-', b16 = 'r', b15="çå®æµé")
plt.legend(b17 = 'upper right')
plt.xlabel("å¨æ(15min)")
plt.ylabel("è½¦æµé(è½¦è¾æ°/å¨æï¼")
plt.show()