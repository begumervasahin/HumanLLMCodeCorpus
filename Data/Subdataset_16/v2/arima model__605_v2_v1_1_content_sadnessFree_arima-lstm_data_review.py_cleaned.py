import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(b7, b8):
    a1 = 0
    for true, pred in zip(b7, b8):
        a1 += abs((pred - true) / true)
    return (a1 / len(b7)) * 100
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b3 = read_csv(b2, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
b4 = b3.values[:1000]
plt.plot(b4, '-', b5 = "Real Flow")
plt.legend(b6 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Vehicle Volume Over Time")
plt.show()
b7 = [1, 2, 3, 4, 5]
b8 = [0.9, 2.1, 3.2, 4.3, 5.1]
b9 = fonk2(b7, b8)
print(f"Mean Absolute Percentage Error (MAPE): {b9:.2f}%")