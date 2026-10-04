import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(b15, b16):
    b2 = sum(math.fabs((y_p - y_t) / y_t) for y_t, y_p in zip(b15, b16))
    return (b2 / len(b15)) * 100
def fonk3(data, b3 = "Traffic Volume Over Time", xlabel="Period (15-minute intervals)", ylabel="Volume (vehicle/period)", b4="Real Flow"):
    plt.plot(data, '-', b4 = b4)
    plt.legend(b5 = 'upper right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.b3(b3)
    plt.show()
def fonk4():
    b6 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    b7 = read_csv(
        b6,
        b8 = [2, 3],
        b9 = 0,
        b10 = [0],
        b11 = 0,
        b12 = True,
        b13 = parse_datetime
    )
    b14 = b7.values[:1000]
    fonk3(b14)
    b15 = [1, 2, 3, 4, 5]
    b16 = [0.9, 2.1, 3.2, 4.3, 5.1]
    b17 = fonk2(b15, b16)
    print(f"Mean Absolute Percentage Error (MAPE): {b17:.2f}%")
if b18 = = "__main__":
    fonk4()