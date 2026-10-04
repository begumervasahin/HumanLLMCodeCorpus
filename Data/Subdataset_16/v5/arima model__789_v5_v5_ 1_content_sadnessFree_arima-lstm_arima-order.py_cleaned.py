import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b2 / len(y_true)
def fonk3(b10):
    return read_csv(
        b10,
        b3 = [2, 3],
        b4 = 0,
        b5 = [0],
        b6 = 0,
        b7 = True,
        b8 = parse_datetime
    )
def fonk4(data):
    b9 = st.adfuller(data)
    return b9[0], b9[1], b9[4]
def fonk5():
    b10 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    b11 = fonk3(b10)
    b12 = b11.values
    a1 = 2
    a2 = 200
    b13 = b12[a1:a1 + a2]
    adf_stat, p_value, b14 = fonk4(b13)
    print("ADF Statistic:", adf_stat)
    print("p-value:", p_value)
    for key, value in b14.items():
        print(f'Critical Value ({key}): {value}')
if b15 = = "__main__":
    fonk5()