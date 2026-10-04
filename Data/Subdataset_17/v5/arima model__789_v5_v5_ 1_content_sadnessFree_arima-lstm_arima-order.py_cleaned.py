import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def parse_datetime(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def calculate_mape(y_true, y_pred):
    total_error = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return total_error / len(y_true)
def load_data(file_path):
    return read_csv(
        file_path,
        usecols=[2, 3],
        header=0,
        parse_dates=[0],
        index_col=0,
        squeeze=True,
        date_parser=parse_datetime
    )
def perform_adf_test(data):
    adf_result = st.adfuller(data)
    return adf_result[0], adf_result[1], adf_result[4]
def main():
    file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    series = load_data(file_path)
    data_values = series.values
    start_index = 2
    training_size = 200
    arima_training_data = data_values[start_index:start_index + training_size]
    adf_stat, p_value, critical_values = perform_adf_test(arima_training_data)
    print("ADF Statistic:", adf_stat)
    print("p-value:", p_value)
    for key, value in critical_values.items():
        print(f'Critical Value ({key}): {value}')
if __name__ == "__main__":
    main()