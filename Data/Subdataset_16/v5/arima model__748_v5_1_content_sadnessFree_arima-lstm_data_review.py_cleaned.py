import math
import matplotlib.pyplot as plt
import pandas as pd
def fonk1(x):
    return pd.to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b2 / len(y_true)
b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b4 = pd.read_csv(
    b3,
    b5 = [2, 3],
    b6 = 0,
    b7 = [0],
    b8 = 0,
    b9 = parse_date
)
b10 = b4.values[:1000]
plt.figure(b11 = (12, 6))
plt.plot(b10, '-', b12 = "Real Flow")
plt.legend(b13 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Vehicle Flow Over Time")
plt.show()