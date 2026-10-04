import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
import seaborn as sns
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(abs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return total_error / len(y_true)
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
selected_columns = [2, 3]
date_column = 0
def parse_dates(date_str):
    return to_datetime(date_str, format='%Y-%m-%d %H:%M:%S')
series = read_csv(
    file_path,
    usecols=selected_columns,
    header=0,
    parse_dates=[date_column],
    index_col=0,
    squeeze=True,
    date_parser=parse_dates
)
data_values = series.values
start_index = 2
training_size = 200
arima_train_data = data_values[start_index : start_index + training_size]
adf_test_result = st.adfuller(arima_train_data)
print("Augmented Dickey-Fuller Test Result:", adf_test_result)