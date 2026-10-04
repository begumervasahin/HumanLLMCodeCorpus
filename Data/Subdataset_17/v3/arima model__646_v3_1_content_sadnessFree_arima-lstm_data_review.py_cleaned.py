import math
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
def parser(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    total_error = sum(abs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return total_error / len(y_true)
def load_data(file_path, usecols, date_parser):
    return pd.read_csv(file_path, usecols=usecols, header=0, parse_dates=[0], index_col=0, date_parser=date_parser)
def plot_data(data, title, xlabel, ylabel, legend_label, figsize=(12, 6)):
    plt.figure(figsize=figsize)
    plt.plot(data, '-', label=legend_label)
    plt.legend(loc='upper right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
FILE_PATH = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
USECOLS = [2, 3]
DATE_PARSER = parser
series = load_data(FILE_PATH, USECOLS, DATE_PARSER)
data = series.values[:1000]
plot_data(data, title="Vehicle Volume Over Time", xlabel="Period (15-minute intervals)",
          ylabel="Volume (vehicles/period)", legend_label="Real Flow")