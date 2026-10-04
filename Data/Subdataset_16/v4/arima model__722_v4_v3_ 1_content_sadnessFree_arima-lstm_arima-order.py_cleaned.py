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
b4 = read_csv(
    b2,
    b5 = b3,
    b6 = 0,
    b7 = [a1],
    b8 = 0,
    b9 = True,
    b10 = lambda x: to_datetime(x, format='%Y-%m-%d %H:%M:%S')
)
b11 = b4.values
a2 = 2
a3 = 200
b12 = b11[a2 : a2 + a3]
b13 = st.adfuller(b12)
print(b13)