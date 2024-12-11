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
b2 = read_csv(b1, usecols=[2, 3], header=0, parse_dates=[0],
                  b3 = 0, squeeze=True, date_parser=parser)
b4 = b2.values
a2 = 2
a3 = 200
b5 = b4[a2:a2 + a3]
b6 = st.adfuller(b5)
print(b6)