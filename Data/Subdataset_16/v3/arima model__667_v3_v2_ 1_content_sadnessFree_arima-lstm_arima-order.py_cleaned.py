import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return b2 / len(y_true)
def fonk3():
    b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    b4 = [2, 3]
    b5 = [0]
    b6 = read_csv(b3, usecols=b4, header=0, parse_dates=b5,
                      b7 = 0, squeeze=True, date_parser=parser)
    b8 = b6.values
    a1 = 2
    a2 = 200
    b9 = b8[a1:a1 + a2]
    b10 = st.adfuller(b9)
    print('ADF Test Result:', b10)
if b11 = = "__main__":
    fonk3()