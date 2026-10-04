import math
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b1 = sum(abs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b1 / len(y_true)
def fonk3(file_path, b2, date_parser):
    return pd.read_csv(file_path, b2 = b2, header=0, parse_dates=[0], index_col=0, date_parser=date_parser)
def fonk4(b10, b11, xlabel, b12, legend_label, b3 = (12, 6)):
    plt.figure(b3 = b3)
    plt.plot(b10, '-', b4 = legend_label)
    plt.legend(b5 = 'upper right')
    plt.xlabel(xlabel)
    plt.b12(b12)
    plt.b11(b11)
    plt.show()
b6 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b7 = [2, 3]
b8 = parser
b9 = fonk3(b6, b7, b8)
b10 = b9.values[:1000]
fonk4(b10, b11 = "Vehicle Volume Over Time", xlabel="Period (15-minute intervals)",
          b12 = "Volume (vehicles/period)", legend_label="Real Flow")