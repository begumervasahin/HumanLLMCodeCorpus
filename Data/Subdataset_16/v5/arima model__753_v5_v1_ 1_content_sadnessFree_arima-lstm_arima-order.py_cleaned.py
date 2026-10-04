import math
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller
def fonk1(b6):
    return pd.to_datetime(b6, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    return sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true))) / len(y_true)
def fonk3(b8):
    return pd.read_csv(b8, b2 = [2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
def fonk4(b9):
    b3 = adfuller(b9)
    print("ADF Statistic:", b3[0])
    print("p-value:", b3[1])
    for key, value in b3[4].items():
        print(f'Critical Value ({key}): {value}')
def fonk5(b9, a1, a2):
    plt.figure(b4 = (10, 6))
    plt.plot(b9.index, b9.values, b5 = 'Series Data')
    plt.axvline(b6 = b9.index[a1 + a2], color='r', linestyle='--', b5='Training Cutoff')
    plt.legend()
    plt.title('Time Series Data')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.show()
if b7 = = "__main__":
    b8 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    b9 = fonk3(b8)
    b10 = b9.values
    a1 = 2
    a2 = 200
    b11 = b10[a1:a1 + a2]
    fonk4(b11)
    fonk5(b9, a1, a2)