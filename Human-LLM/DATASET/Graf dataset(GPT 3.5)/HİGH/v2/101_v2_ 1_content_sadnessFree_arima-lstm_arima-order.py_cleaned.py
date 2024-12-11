import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
import statsmodels.tsa.stattools as st
import seaborn as sns
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
b1 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b2 = [2, 3]
b3 = [0]
b4 = read_csv(b1, usecols=b2, header=0, parse_dates=b3,
                  b5 = 0, squeeze=True, date_parser=parser)
b6 = b4.values
a2 = 2
a3 = 200
b7 = b6[a2:a2 + a3]
b8 = st.adfuller(b7)
print(b8)