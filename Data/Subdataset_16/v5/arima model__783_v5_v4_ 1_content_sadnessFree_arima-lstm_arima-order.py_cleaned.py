import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
import seaborn as sns
def fonk1(date_str):
    return to_datetime(date_str, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(math.fabs(pred - true) / true for pred, true in zip(y_pred, y_true))
    return b2 / len(y_true)
b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b4 = read_csv(b3, usecols=[2, 3], header=0, parse_dates=[0],
                       b5 = 0, date_parser=parse_datetime)
b6 = b4.b6
a1 = 2
a2 = 200
b7 = b6[a1:a1 + a2]
b8 = st.adfuller(b7)
print("Augmented Dickey-Fuller Test Results:")
print(f"ADF Statistic: {b8[0]:.6f}")
print(f"p-value: {b8[1]:.6f}")
print("Critical Values:")
for key, value in b8[4].items():
    print(f"\t{key}: {value:.3f}")