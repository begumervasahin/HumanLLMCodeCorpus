import math
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += abs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
b1 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv', usecols=[2, 3], header=0, parse_dates=[0],
                     b2 = 0, date_parser=parser)
b3 = b1.values[0:1000]
plt.figure(b4 = (12, 6))
plt.plot(b3, '-', b5 = "real flow")
plt.legend(b6 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.show()