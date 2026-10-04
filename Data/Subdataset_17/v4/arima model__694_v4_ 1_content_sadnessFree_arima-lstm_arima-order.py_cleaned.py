import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
import statsmodels.tsa.stattools as st
import seaborn as sns
def parser(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = 0
    for i in range(len(y_true)):
        total_error += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return total_error / len(y_true)
file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
series = read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0],
                  index_col=0, squeeze=True, date_parser=parser)
X = series.values
start = 2
size = 200
arima_train_data = X[start:start + size]
adf_result = st.adfuller(arima_train_data)
print(adf_result)