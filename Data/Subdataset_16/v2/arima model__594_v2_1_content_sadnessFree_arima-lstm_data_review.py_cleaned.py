import math
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for true, pred in zip(y_true, y_pred):
        a1 += abs(pred - true) / true
    return a1 / len(y_true)
b1 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b2 = pd.read_csv(b1, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
b3 = b2.values[:1000]
plt.figure(b4 = (12, 6))
plt.plot(b3, '-', b5 = "Real Flow")
plt.legend(b6 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicles/period)")
plt.title("Vehicle Volume Over Time")
plt.show()