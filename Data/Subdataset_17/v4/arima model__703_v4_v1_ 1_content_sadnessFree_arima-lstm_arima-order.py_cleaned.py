import math
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller
def parser(x):
    return pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_a_p_e(y_true, y_pred):
    return sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true))) / len(y_true)
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
series = pd.read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
X = series.values
start = 2
size = 200
arima_train = X[start:start + size]
adf_result = adfuller(arima_train)
print("ADF Statistic:", adf_result[0])
print("p-value:", adf_result[1])
for key, value in adf_result[4].items():
    print(f'Critical Value ({key}): {value}')
plt.figure(figsize=(10, 6))
plt.plot(series.index, series.values, label='Series Data')
plt.axvline(x=series.index[start + size], color='r', linestyle='--', label='Training Cutoff')
plt.legend()
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Values')
plt.show()