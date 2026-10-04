import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def fonk1(date_string):
    return to_datetime(date_string, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b2 / len(y_true)
def fonk3(file_path, selected_columns, date_column):
    return read_csv(file_path, b3 = selected_columns, header=0,
                    b4 = [date_column], index_col=date_column,
                    b5 = True, date_parser=parse_date)
def fonk4(data, b6 = "Volume Over Time", xlabel="Period (15-minute intervals)", ylabel="Volume (vehicles/period)"):
    plt.plot(data, '-', b7 = "Real Flow")
    plt.legend(b8 = 'upper right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.b6(b6)
    plt.show()
if b9 = = "__main__":
    b10 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
    b11 = [2, 3]
    b12 = 'DateColumn'
    b13 = fonk3(b10, b11, b12)
    b14 = b13.head(1000)
    fonk4(b14)