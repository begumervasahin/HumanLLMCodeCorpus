import math
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
def fonk1(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
def fonk2(actual, predicted):
    b1 = sum(abs(pred - act) / act for act, pred in zip(actual, predicted))
    return b1 / len(actual)
def fonk3(file_path):
    b2 = pd.read_csv(
        file_path,
        b3 = [2, 3],
        b4 = 0,
        b5 = [0],
        b6 = 0,
        b7 = True,
        b8 = parse_date
    )
    return b2
def fonk4(b2, b9 = "Traffic Volume over Time"):
    plt.figure(b10 = (12, 6))
    plt.plot(b2, '-', b11 = "Real Flow")
    plt.legend(b12 = 'upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicles/period)")
    plt.b9(b9)
    plt.show()
def fonk5():
    b13 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    b14 = fonk3(b13)
    b15 = b14.values[:1000]
    fonk4(b15)
if b16 = = "__main__":
    fonk5()