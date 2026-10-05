import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
b1 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv',
                  b2 = [2, 3],
                  b3 = 0,
                  b4 = [0],
                  b5 = 0,
                  b6 = True,
                  b7 = parser)
b8 = b1.values[0:1000]
plt.plot(b8, '-', b9 = "Real Flow")
plt.legend(b10 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicles/period)")
plt.show(b11 = (12, 6))