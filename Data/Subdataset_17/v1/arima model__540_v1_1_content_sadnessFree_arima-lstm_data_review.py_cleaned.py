import math
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
def parser(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def mean_a_p_e(y_true, y_pred):
    sum = 0
    for i in range(len(y_true)):
        sum += abs(y_pred[i] - y_true[i]) / y_true[i]
    return sum / len(y_true)
series = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv', usecols=[2, 3], header=0, parse_dates=[0],
                     index_col=0, date_parser=parser)
X = series.values[0:1000]
plt.figure(figsize=(12, 6))
plt.plot(X, '-', label="real flow")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.show()