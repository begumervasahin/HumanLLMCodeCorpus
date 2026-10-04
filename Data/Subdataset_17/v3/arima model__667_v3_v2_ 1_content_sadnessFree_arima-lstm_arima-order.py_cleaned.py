import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def parser(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return total_error / len(y_true)
def main():
    file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    selected_columns = [2, 3]
    date_columns = [0]
    series = read_csv(file_path, usecols=selected_columns, header=0, parse_dates=date_columns,
                      index_col=0, squeeze=True, date_parser=parser)
    data_values = series.values
    start_index = 2
    training_size = 200
    arima_train_data = data_values[start_index:start_index + training_size]
    adf_test_result = st.adfuller(arima_train_data)
    print('ADF Test Result:', adf_test_result)
if __name__ == "__main__":
    main()