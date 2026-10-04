import math
import matplotlib.pyplot as plt
import pandas as pd
def fonk1(date_string):
    return pd.to_datetime(date_string, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs(y_p - y_t) / y_t for y_t, y_p in zip(y_true, y_pred))
    return b2 / len(y_true)
def fonk3(b14, b15, b16, b17):
    plt.figure(b3 = (12, 6))
    plt.plot(b14, '-', b4 = "Real Flow")
    plt.legend(b5 = 'upper right')
    plt.b16(b16)
    plt.b17(b17)
    plt.b15(b15)
    plt.show()
def fonk4():
    b6 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    b7 = pd.read_csv(
        b6,
        b8 = [2, 3],
        b9 = 0,
        b10 = [0],
        b11 = 0,
        b12 = parse_date
    )
    b13 = b7.values[0:1000]
    fonk3(
        b14 = b13,
        b15 = "Traffic Volume Over Time",
        b16 = "Period (15-minute intervals)",
        b17 = "Volume (vehicles/period)"
    )
if b18 = = "__main__":
    fonk4()