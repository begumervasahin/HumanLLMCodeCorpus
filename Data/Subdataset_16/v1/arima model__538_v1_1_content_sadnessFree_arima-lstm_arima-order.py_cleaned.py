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
b2 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0,
                     b3 = [0], index_col=0, date_parser=parser)
b4 = b2.values
a2 = 2
a3 = 200
b5 = b4[a2:a2 + a3]
b6 = st.adfuller(b5)
print("ADF Statistic: %f" % b6[0])
print("p-value: %f" % b6[1])
print("Critical Values:")
for key, value in b6[4].items():
    print('\t%s: %.3f' % (key, value))