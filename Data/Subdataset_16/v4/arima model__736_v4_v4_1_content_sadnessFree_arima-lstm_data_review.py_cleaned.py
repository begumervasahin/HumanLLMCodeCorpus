import math
import matplotlib.pyplot as plt
import pandas as pd
def fonk1(date_string):
    return pd.to_datetime(date_string, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs(y_p - y_t) / y_t for y_t, y_p in zip(y_true, y_pred))
    return b2 / len(y_true)
def fonk3():
    b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    b4 = pd.read_csv(
        b3,
        b5 = [2, 3],
        b6 = 0,
        b7 = [0],
        b8 = 0,
        b9 = parse_date
    )
    b10 = b4.values[0:1000]
    plt.figure(b11 = (12, 6))
    plt.plot(b10, '-', b12 = "Real Flow")
    plt.legend(b13 = 'upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicles/period)")
    plt.title("Traffic Volume Over Time")
    plt.show()
if b14 = = "__main__":
    fonk3()