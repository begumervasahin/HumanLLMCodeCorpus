import math
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import datetime
import statsmodels.tsa.stattools as st
import seaborn as sns
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
b1 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0, parse_dates=[0],
                  b2 = 0, squeeze=True, date_parser=parser)
b3 = b1.values
a2 = 2
a3 = 200
b4 = b3[a2:a2 + a3]
print(st.adfuller(b4))