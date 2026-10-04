import math
import matplotlib.pyplot as plt
import pandas as pd
def parse_date(date_str):
    return pd.to_datetime(date_str, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(abs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return total_error / len(y_true)
def read_and_process_data(file_path, date_column, selected_columns):
    return pd.read_csv(
        file_path,
        usecols=selected_columns,
        header=0,
        parse_dates=[date_column],
        index_col=date_column,
        date_parser=parse_date
    )
def plot_data(data, title="Real Flow", xlabel="Period (15-minute intervals)", ylabel="Volume (vehicles/period)"):
    plt.plot(data, '-', label=title)
    plt.legend(loc='upper right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
if __name__ == "__main__":
    file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    selected_columns = [2, 3]
    date_column = 'DateColumn'
    series = read_and_process_data(file_path, date_column, selected_columns)
    data_subset = series.head(1000)
    plot_data(data_subset)