import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def parse_datetime(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def calculate_mape(y_true, y_pred):
    total_error = sum(math.fabs((predicted - actual) / actual) for actual, predicted in zip(y_true, y_pred))
    return (total_error / len(y_true)) * 100
def load_time_series_data(csv_file_path, n_values=1000):
    series = read_csv(
        csv_file_path,
        usecols=[2, 3],
        header=0,
        parse_dates=[0],
        index_col=0,
        squeeze=True,
        date_parser=parse_datetime
    )
    return series.values[:n_values]
def plot_time_series(data):
    plt.plot(data, '-', label="Real Flow")
    plt.legend(loc='upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicle/period)")
    plt.title("Traffic Flow Time Series")
    plt.show()
def main():
    csv_file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    time_series_data = load_time_series_data(csv_file_path)
    plot_time_series(time_series_data)
    actual_values = [1, 2, 3, 4, 5]
    predicted_values = [0.9, 2.1, 3.2, 4.3, 5.1]
    mape = calculate_mape(actual_values, predicted_values)
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
if __name__ == "__main__":
    main()