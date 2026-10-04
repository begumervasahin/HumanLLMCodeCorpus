import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def parse_datetime(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(abs((y_p - y_t) / y_t) for y_t, y_p in zip(y_true, y_pred))
    return (total_error / len(y_true)) * 100
def plot_time_series(data, title="Time Series of Traffic Volume", xlabel="Period (15-minute intervals)", ylabel="Volume (vehicle/period)"):
    plt.plot(data, '-', label="Real Flow")
    plt.legend(loc='upper right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
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
        date_parser=parse_datetime
    )
    data_to_plot = series.values[:1000]
    plot_time_series(data_to_plot)
    y_true = [1, 2, 3, 4, 5]
    y_pred = [0.9, 2.1, 3.2, 4.3, 5.1]
    mape = mean_absolute_percentage_error(y_true, y_pred)
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
if __name__ == "__main__":
    main()