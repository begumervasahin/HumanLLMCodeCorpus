import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
import statsmodels.tsa.stattools as st
import seaborn as sns
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b1 = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b1 / len(y_true)
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b3 = [2, 3]
b4 = [0]
b5 = read_csv(b2, usecols=b3, header=0, parse_dates=b4,
                  b6 = 0, squeeze=True, date_parser=parse_datetime)
b7 = b5.values
a1 = 2
a2 = 200
b8 = b7[a1 : a1 + a2]
b9 = st.adfuller(b8)
print(b9)