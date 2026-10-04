import math
import matplotlib.pyplot as plt
import pandas as pd
def parser(x):
    return pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = 0
    for true, pred in zip(y_true, y_pred):
        total_error += abs(pred - true) / true
    return total_error / len(y_true)
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
series = pd.read_csv(
    file_path,
    usecols=[2, 3],
    header=0,
    parse_dates=[0],
    index_col=0,
    date_parser=parser
)
data = series.values[0:1000]
plt.figure(figsize=(12, 6))
plt.plot(data, '-', label="Real Flow")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Vehicle Flow Over Time")
plt.show()