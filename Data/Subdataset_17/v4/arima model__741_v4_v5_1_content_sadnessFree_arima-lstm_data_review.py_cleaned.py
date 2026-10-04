import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def parse_date(date_string):
    return to_datetime(date_string, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return total_error / len(y_true)
def load_and_prepare_data(file_path, selected_columns, date_column):
    return read_csv(file_path, usecols=selected_columns, header=0,
                    parse_dates=[date_column], index_col=date_column,
                    squeeze=True, date_parser=parse_date)
def plot_data(data, title="Volume Over Time", xlabel="Period (15-minute intervals)", ylabel="Volume (vehicles/period)"):
    plt.plot(data, '-', label="Real Flow")
    plt.legend(loc='upper right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
if __name__ == "__main__":
    FILE_PATH = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    SELECTED_COLUMNS = [2, 3]
    DATE_COLUMN = 'DateColumn'
    series = load_and_prepare_data(FILE_PATH, SELECTED_COLUMNS, DATE_COLUMN)
    data_subset = series.head(1000)
    plot_data(data_subset)