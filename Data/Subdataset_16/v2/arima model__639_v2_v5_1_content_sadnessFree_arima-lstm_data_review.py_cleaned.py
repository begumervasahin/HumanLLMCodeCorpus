import math
import matplotlib.pyplot as plt
import pandas as pd
def fonk1(date_str):
    return pd.to_datetime(date_str, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b2 / len(y_true)
def fonk3(b12, b14, b13):
    return pd.read_csv(
        b12,
        b3 = b13,
        b4 = 0,
        b5 = [b14],
        b6 = b14,
        b7 = parse_date
    )
def fonk4(data, b8 = "Real Flow", xlabel="Period (15-minute intervals)", ylabel="Volume (vehicles/period)"):
    plt.plot(data, '-', b9 = b8)
    plt.legend(b10 = 'upper right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
if b11 = = "__main__":
    b12 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    b13 = [2, 3]
    b14 = 'DateColumn'
    b15 = fonk3(b12, b14, b13)
    b16 = b15.head(1000)
    fonk4(b16)