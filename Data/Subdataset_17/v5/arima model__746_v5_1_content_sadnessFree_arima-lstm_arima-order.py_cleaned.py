import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def parse_dates(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def calculate_mape(y_true, y_pred):
    total_error = sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return total_error / len(y_true)
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
series = read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parse_dates)
data_values = series.values
start_index = 2
training_size = 200
arima_train_data = data_values[start_index:start_index + training_size]
adf_test_result = st.adfuller(arima_train_data)
print("ADF Test Result:", adf_test_result)
plt.figure(figsize=(10, 5))
plt.plot(series)
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()