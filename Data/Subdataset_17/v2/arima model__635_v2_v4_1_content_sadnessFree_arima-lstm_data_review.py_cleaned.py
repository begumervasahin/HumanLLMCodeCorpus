import math
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
def parse_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
def calculate_mape(actual, predicted):
    total_error = sum(abs(pred - act) / act for act, pred in zip(actual, predicted))
    return total_error / len(actual)
def read_traffic_data(file_path):
    data = pd.read_csv(file_path,
                       usecols=[2, 3],
                       header=0,
                       parse_dates=[0],
                       index_col=0,
                       squeeze=True,
                       date_parser=parse_date)
    return data
def plot_traffic_volume(data, title="Traffic Volume over Time"):
    plt.figure(figsize=(12, 6))
    plt.plot(data, '-', label="Real Flow")
    plt.legend(loc='upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicles/period)")
    plt.title(title)
    plt.show()
if __name__ == "__main__":
    csv_file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    traffic_series = read_traffic_data(csv_file_path)
    traffic_data_subset = traffic_series.values[0:1000]
    plot_traffic_volume(traffic_data_subset)