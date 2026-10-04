import math
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.tsa.stattools as st
import seaborn as sns
def parser(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = 0
    for i in range(len(y_true)):
        total_error += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return total_error / len(y_true)
def read_series(file_path):
    return pd.read_csv(
        file_path,
        usecols=[2, 3],
        header=0,
        parse_dates=[0],
        index_col=0,
        squeeze=True,
        date_parser=parser
    )
def perform_adf_test(data):
    adf_result = st.adfuller(data)
    print_adf_result(adf_result)
    return adf_result
def print_adf_result(adf_result):
    print('ADF Statistic: %f' % adf_result[0])
    print('p-value: %f' % adf_result[1])
    print('Critical Values:')
    for key, value in adf_result[4].items():
        print('\t%s: %.3f' % (key, value))
def plot_time_series(series):
    plt.figure(figsize=(10, 6))
    plt.plot(series.index, series.values)
    plt.title('Time Series Data')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.show()
def main():
    file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    series = read_series(file_path)
    X = series.values
    start = 2
    size = 200
    arima_train_data = X[start:start + size]
    perform_adf_test(arima_train_data)
    plot_time_series(series)
if __name__ == "__main__":
    main()