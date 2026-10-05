import math
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import datetime
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
b1 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv', usecols=[2, 3], header=0, parse_dates=[0],
                  b2 = 0,
                  b3 = True,
                  b4 = parser)
b5 = b1.values[0:1000]
plt.plot(b5, '-', b6 = "real flow")
plt.legend(b7 = 'upper right')
plt.xlabel("period(15-minute intervals)")
plt.ylabel("volume(vehicle/period)")
plt.show(b8 = (12, 6))