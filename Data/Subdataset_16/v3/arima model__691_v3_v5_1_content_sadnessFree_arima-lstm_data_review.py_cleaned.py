import math
import matplotlib.pyplot as plt
import pandas as pd
def fonk1(date_str):
    return pd.to_datetime(date_str, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b2 / len(y_true)
def fonk3(b11, b13, b12):
    return pd.read_csv(
        b11,
        b3 = b12,
        b4 = 0,
        b5 = [b13],
        b6 = b13,
        b7 = parse_date
    )
def fonk4(data, b8 = "Real Flow", xlabel="Period (15-minute intervals)", ylabel="Volume (vehicles/period)"):
    plt.plot(data, '-', b9 = b8)
    plt.legend(b10 = 'upper right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
def fonk5():
    b11 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    b12 = [2, 3]
    b13 = 'DateColumn'
    b14 = fonk3(b11, b13, b12)
    b15 = b14.head(1000)
    fonk4(b15)
if b16 = = "__main__":
    fonk5()