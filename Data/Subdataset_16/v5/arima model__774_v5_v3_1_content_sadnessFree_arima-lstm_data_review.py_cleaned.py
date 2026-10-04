import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs((predicted - actual) / actual) for actual, predicted in zip(y_true, y_pred))
    return (b2 / len(y_true)) * 100
def fonk3(data, b3 = "Time Series of Traffic Flow", xlabel="Period (15-minute intervals)", ylabel="Volume (vehicle/period)"):
    plt.figure(b4 = (10, 6))
    plt.plot(data, '-', b5 = "Real Flow")
    plt.legend(b6 = 'upper right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.b3(b3)
    plt.grid(True)
    plt.show()
b7 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b8 = read_csv(b7, usecols=[2, 3], header=0, parse_dates=[0],
                  b9 = 0, squeeze=True, date_parser=parse_datetime)
b10 = b8.values[:1000]
fonk3(b10)
b11 = [1, 2, 3, 4, 5]
b12 = [0.9, 2.1, 3.2, 4.3, 5.1]
b13 = fonk2(b11, b12)
print(f"Mean Absolute Percentage Error (MAPE): {b13:.2f}%")