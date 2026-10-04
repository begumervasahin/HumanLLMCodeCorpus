import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(math.fabs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return b2 / len(y_true)
b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b4 = [2, 3]
b5 = [0]
b6 = read_csv(b3, usecols=b4, header=0,
                  b7 = b5, index_col=0, date_parser=parser)
b8 = b6.values
a1 = 2
a2 = 200
b9 = b8[a1:a1 + a2]
b10 = st.adfuller(b9)
print(b10)