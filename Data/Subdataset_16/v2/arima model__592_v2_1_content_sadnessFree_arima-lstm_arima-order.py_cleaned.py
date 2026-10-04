import math
import matplotlib.pyplot as plt
import pandas as pd
from pandas import to_datetime
import statsmodels.tsa.stattools as st
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += abs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b3 = pd.read_csv(b2, usecols=[2, 3], header=0,
                     b4 = [0], index_col=0, date_parser=parser)
b5 = b3.values
a2 = 2
a3 = 200
b6 = b5[a2:a2 + a3]
b7 = st.adfuller(b6)
print("ADF Statistic: %f" % b7[0])
print("p-value: %f" % b7[1])
print("Critical Values:")
for key, value in b7[4].items():
    print('\t%s: %.3f' % (key, value))
