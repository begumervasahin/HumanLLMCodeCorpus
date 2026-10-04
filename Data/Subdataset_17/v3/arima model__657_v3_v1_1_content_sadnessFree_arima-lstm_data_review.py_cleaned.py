import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def parser(date_str):
    return to_datetime(date_str, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    sum_error = 0
    for true, pred in zip(y_true, y_pred):
        sum_error += abs((pred - true) / true)
    return (sum_error / len(y_true)) * 100
def plot_time_series(data, title, x_label, y_label):
    plt.plot(data, '-', label="Real Flow")
    plt.legend(loc='upper right')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
def main():
    csv_file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    series = read_csv(
        csv_file_path,
        usecols=[2, 3],
        header=0,
        parse_dates=[0],
        index_col=0,
        squeeze=True,
        date_parser=parser
    )
    data_to_plot = series.values[:1000]
    plot_time_series(
        data=data_to_plot,
        title="Vehicle Volume Over Time",
        x_label="Period (15-minute intervals)",
        y_label="Volume (vehicle/period)"
    )
    y_true = [1, 2, 3, 4, 5]
    y_pred = [0.9, 2.1, 3.2, 4.3, 5.1]
    mape = mean_absolute_percentage_error(y_true, y_pred)
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
if __name__ == "__main__":
    main()