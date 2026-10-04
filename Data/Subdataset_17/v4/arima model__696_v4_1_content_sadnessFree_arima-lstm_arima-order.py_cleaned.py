import math
import matplotlib.pyplot as plt
from pandas import read_csv
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
series = read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
X = series.values
start = 2
size = 200
arima_train = X[start:start + size]
adf_test_result = st.adfuller(arima_train)
print(adf_test_result)
plt.plot(series)
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()