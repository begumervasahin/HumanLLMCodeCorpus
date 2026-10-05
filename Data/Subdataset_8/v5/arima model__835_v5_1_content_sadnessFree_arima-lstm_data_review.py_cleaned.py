import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
def parse_date(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return total_error / len(y_true)
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
selected_columns = [2, 3]
date_column = 'DateColumn'
series = read_csv(file_path, usecols=selected_columns, header=0,
                  parse_dates=[date_column], index_col=date_column,
                  squeeze=True, date_parser=parse_date)
data_subset = series.head(1000)
plt.plot(data_subset, '-', label="Real Flow")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicles/period)")
plt.show()