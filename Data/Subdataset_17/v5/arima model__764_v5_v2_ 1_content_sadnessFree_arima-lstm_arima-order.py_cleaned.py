import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def parser(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(math.fabs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return total_error / len(y_true)
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
selected_columns = [2, 3]
date_column = [0]
series = read_csv(file_path, usecols=selected_columns, header=0,
                  parse_dates=date_column, index_col=0, date_parser=parser)
data_values = series.values
start_index = 2
training_size = 200
arima_train_data = data_values[start_index:start_index + training_size]
adf_test_result = st.adfuller(arima_train_data)
print('ADF Statistic: %f' % adf_test_result[0])
print('p-value: %f' % adf_test_result[1])
print('Critical Values:')
for key, value in adf_test_result[4].items():
    print('\t%s: %.3f' % (key, value))