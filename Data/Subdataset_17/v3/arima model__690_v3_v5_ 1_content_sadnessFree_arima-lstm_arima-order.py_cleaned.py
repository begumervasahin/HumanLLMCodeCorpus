import math
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.tsa.stattools as st
from pandas import read_csv, to_datetime
def parse_datetime(date_string):
    return to_datetime(date_string, format='%Y-%m-%d %H:%M:%S')
def calculate_mape(actual_values, predicted_values):
    total_error = sum(abs(predicted - actual) / actual for actual, predicted in zip(actual_values, predicted_values))
    return total_error / len(actual_values)
def main():
    file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    series = read_csv(file_path, usecols=[2, 3], header=0, parse_dates=[0],
                      index_col=0, squeeze=True, date_parser=parse_datetime)
    data_values = series.values
    start_index = 2
    training_size = 200
    arima_training_data = data_values[start_index:start_index + training_size]
    adf_result = st.adfuller(arima_training_data)
    print(f'ADF Statistic: {adf_result[0]:.6f}')
    print(f'p-value: {adf_result[1]:.6f}')
    print('Critical Values:')
    for key, value in adf_result[4].items():
        print(f'{key}: {value:.3f}')
if __name__ == "__main__":
    main()