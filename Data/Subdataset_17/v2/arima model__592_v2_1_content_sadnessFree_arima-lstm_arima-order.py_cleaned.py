import math
import matplotlib.pyplot as plt
import pandas as pd
from pandas import to_datetime
import statsmodels.tsa.stattools as st
def parser(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    sum_error = 0
    for i in range(len(y_true)):
        sum_error += abs(y_pred[i] - y_true[i]) / y_true[i]
    return sum_error / len(y_true)
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
series = pd.read_csv(file_path, usecols=[2, 3], header=0,
                     parse_dates=[0], index_col=0, date_parser=parser)
X = series.values
start = 2
size = 200
arima_train = X[start:start + size]
adf_result = st.adfuller(arima_train)
print("ADF Statistic: %f" % adf_result[0])
print("p-value: %f" % adf_result[1])
print("Critical Values:")
for key, value in adf_result[4].items():
    print('\t%s: %.3f' % (key, value))
