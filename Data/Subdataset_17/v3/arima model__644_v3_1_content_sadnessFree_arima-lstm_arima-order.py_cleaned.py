import math
import matplotlib.pyplot as plt
import pandas as pd
from pandas import to_datetime
import statsmodels.tsa.stattools as st
def parser(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    sum_error = sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return sum_error / len(y_true)
def load_dataset(file_path):
    return pd.read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
def perform_adf_test(series, start, size):
    adf_result = st.adfuller(series[start:start + size])
    print(f"ADF Statistic: {adf_result[0]:.6f}")
    print(f"p-value: {adf_result[1]:.6f}")
    print("Critical Values:")
    for key, value in adf_result[4].items():
        print(f"\t{key}: {value:.3f}")
def main():
    file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    series = load_dataset(file_path)
    X = series.values
    start = 2
    size = 200
    perform_adf_test(X, start, size)
if __name__ == "__main__":
    main()