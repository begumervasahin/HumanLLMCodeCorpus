import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
import seaborn as sns
def fonk1(y_true, y_pred):
    b1 = sum(abs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b1 / len(y_true)
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b3 = [2, 3]
a1 = 0
def fonk2(date_str):
    return to_datetime(date_str, b4 = '%Y-%m-%d %H:%M:%S')
b5 = read_csv(
    b2,
    b6 = b3,
    b7 = 0,
    b8 = [a1],
    b9 = 0,
    b10 = True,
    b11 = b8
)
b12 = b5.values
a2 = 2
a3 = 200
b13 = b12[a2 : a2 + a3]
b14 = st.adfuller(b13)
print("Augmented Dickey-Fuller Test Result:", b14)