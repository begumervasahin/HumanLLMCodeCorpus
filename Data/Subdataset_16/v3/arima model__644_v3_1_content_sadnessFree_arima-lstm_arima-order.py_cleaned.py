import math
import matplotlib.pyplot as plt
import pandas as pd
from pandas import to_datetime
import statsmodels.tsa.stattools as st
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return b2 / len(y_true)
def fonk3(b5):
    return pd.read_csv(b5, b3 = [2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
def fonk4(b6, a1, a2):
    b4 = st.adfuller(b6[a1:a1 + a2])
    print(f"ADF Statistic: {b4[0]:.6f}")
    print(f"p-value: {b4[1]:.6f}")
    print("Critical Values:")
    for key, value in b4[4].items():
        print(f"\t{key}: {value:.3f}")
def fonk5():
    b5 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    b6 = fonk3(b5)
    b7 = b6.values
    a1 = 2
    a2 = 200
    fonk4(b7, a1, a2)
if b8 = = "__main__":
    fonk5()