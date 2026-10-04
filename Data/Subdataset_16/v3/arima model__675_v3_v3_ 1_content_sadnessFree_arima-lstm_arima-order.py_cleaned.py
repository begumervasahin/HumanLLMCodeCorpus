import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b2 / len(y_true)
def fonk3(b9, b10, b11, b8):
    return read_csv(
        b9,
        b3 = b10,
        b4 = 0,
        b5 = b11,
        b6 = 0,
        b7 = True,
        b8 = b8
    )
def fonk4():
    b9 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    b10 = [2, 3]
    b11 = [0]
    b12 = fonk3(b9, b10, b11, parse_datetime)
    b13 = b12.values
    a1 = 2
    a2 = 200
    b14 = b13[a1 : a1 + a2]
    b15 = st.adfuller(b14)
    print("ADF Test Result:", b15)
    plt.plot(b14)
    plt.title('Training Data')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.show()
if b16 = = "__main__":
    fonk4()