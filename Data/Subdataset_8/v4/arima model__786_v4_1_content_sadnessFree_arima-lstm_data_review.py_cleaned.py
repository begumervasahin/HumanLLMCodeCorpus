import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
def parser(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = 0
    for i in range(len(y_true)):
        total_error += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return total_error / len(y_true)
series = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv',
                  usecols=[2, 3],
                  header=0,
                  parse_dates=[0],
                  index_col=0,
                  squeeze=True,
                  date_parser=parser)
X = series.values[0:1000]
plt.plot(X, '-', label="Real Flow")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicles/period)")
plt.show(figsize=(12, 6))