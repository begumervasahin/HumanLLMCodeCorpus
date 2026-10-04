import math
import matplotlib.pyplot as plt
import pandas as pd
def parse_date(date_string):
    return pd.to_datetime(date_string, format='%Y-%m-%d %H:%M:%S')
def calculate_mape(y_true, y_pred):
    total_error = sum(abs(y_p - y_t) / y_t for y_t, y_p in zip(y_true, y_pred))
    return total_error / len(y_true)
def plot_traffic_volume(data, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    plt.plot(data, '-', label="Real Flow")
    plt.legend(loc='upper right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
def main():
    data_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    series = pd.read_csv(
        data_path,
        usecols=[2, 3],
        header=0,
        parse_dates=[0],
        index_col=0,
        date_parser=parse_date
    )
    data_subset = series.values[0:1000]
    plot_traffic_volume(
        data=data_subset,
        title="Traffic Volume Over Time",
        xlabel="Period (15-minute intervals)",
        ylabel="Volume (vehicles/period)"
    )
if __name__ == "__main__":
    main()