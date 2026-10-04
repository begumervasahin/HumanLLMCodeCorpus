import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
import statsmodels.tsa.stattools as st
import seaborn as sns
def parse_datetime(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def calculate_mape(y_true, y_pred):
    total_error = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return total_error / len(y_true)
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
series = read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0],
                  index_col=0, squeeze=True, date_parser=parse_datetime)
data_values = series.values
start_index = 2
training_size = 200
arima_training_data = data_values[start_index:start_index + training_size]
adf_result = st.adfuller(arima_training_data)
print(adf_result)