import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b2 / len(y_true)
def fonk3():
    b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    b4 = read_csv(
        b3,
        b5 = [2, 3],
        b6 = 0,
        b7 = [0],
        b8 = 0,
        b9 = True,
        b10 = parse_datetime
    )
    b11 = b4.values
    a1 = 2
    a2 = 200
    b12 = b11[a1:a1 + a2]
    b13 = st.adfuller(b12)
    print("ADF Statistic:", b13[0])
    print("p-value:", b13[1])
    for key, value in b13[4].items():
        print(f'Critical Value ({key}): {value}')
if b14 = = "__main__":
    fonk3()