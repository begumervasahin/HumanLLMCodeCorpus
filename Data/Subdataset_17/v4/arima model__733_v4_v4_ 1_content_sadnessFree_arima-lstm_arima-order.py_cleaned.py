import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
import seaborn as sns
def parse_datetime(date_str):
    return to_datetime(date_str, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(math.fabs(pred - true) / true for pred, true in zip(y_pred, y_true))
    return total_error / len(y_true)
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
data_series = read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0],
                       index_col=0, date_parser=parse_datetime)
values = data_series.values
start_index = 2
train_size = 200
arima_train_data = values[start_index:start_index + train_size]
adf_result = st.adfuller(arima_train_data)
print("ADF Statistic: %f" % adf_result[0])
print("p-value: %f" % adf_result[1])
print("Critical Values:")
for key, value in adf_result[4].items():
    print('\t%s: %.3f' % (key, value))