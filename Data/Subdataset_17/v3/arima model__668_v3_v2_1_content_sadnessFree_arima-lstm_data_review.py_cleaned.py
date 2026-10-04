import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def parse_datetime(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(math.fabs((y_p - y_t) / y_t) for y_t, y_p in zip(y_true, y_pred))
    return (total_error / len(y_true)) * 100
def plot_time_series(data, title="Traffic Volume Over Time", xlabel="Period (15-minute intervals)", ylabel="Volume (vehicle/period)", label="Real Flow"):
    plt.plot(data, '-', label=label)
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
    X = series.values[:1000]
    plot_time_series(X)
    y_true = [1, 2, 3, 4, 5]
    y_pred = [0.9, 2.1, 3.2, 4.3, 5.1]
    mape = mean_absolute_percentage_error(y_true, y_pred)
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
if __name__ == "__main__":
    main()