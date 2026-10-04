import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def fonk1(date_str):
    return to_datetime(date_str, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(b17, b18):
    a1 = 0
    for true, pred in zip(b17, b18):
        a1 += abs((pred - true) / true)
    return (a1 / len(b17)) * 100
def fonk3(b13, b14, b15, b16):
    plt.plot(b13, '-', b2 = "Real Flow")
    plt.legend(b3 = 'upper right')
    plt.xlabel(b15)
    plt.ylabel(b16)
    plt.b14(b14)
    plt.show()
def fonk4():
    b4 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    b5 = read_csv(
        b4,
        b6 = [2, 3],
        b7 = 0,
        b8 = [0],
        b9 = 0,
        b10 = True,
        b11 = parser
    )
    b12 = b5.values[:1000]
    fonk3(
        b13 = b12,
        b14 = "Vehicle Volume Over Time",
        b15 = "Period (15-minute intervals)",
        b16 = "Volume (vehicle/period)"
    )
    b17 = [1, 2, 3, 4, 5]
    b18 = [0.9, 2.1, 3.2, 4.3, 5.1]
    b19 = fonk2(b17, b18)
    print(f"Mean Absolute Percentage Error (MAPE): {b19:.2f}%")
if b20 = = "__main__":
    fonk4()