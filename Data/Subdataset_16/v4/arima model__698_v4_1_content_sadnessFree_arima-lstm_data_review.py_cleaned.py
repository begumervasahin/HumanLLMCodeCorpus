import math
import matplotlib.pyplot as plt
import pandas as pd
def fonk1(x):
    return pd.to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for true, pred in zip(y_true, y_pred):
        a1 += abs(pred - true) / true
    return a1 / len(y_true)
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b3 = pd.read_csv(
    b2,
    b4 = [2, 3],
    b5 = 0,
    b6 = [0],
    b7 = 0,
    b8 = parser
)
b9 = b3.values[0:1000]
plt.figure(b10 = (12, 6))
plt.plot(b9, '-', b11 = "Real Flow")
plt.legend(b12 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Vehicle Flow Over Time")
plt.show()