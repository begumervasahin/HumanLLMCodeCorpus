import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.b7 import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(date_string):
    return to_datetime(date_string, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
def fonk3(filepath, date_col, value_cols):
    b2 = read_csv(filepath, usecols=value_cols, header=0, parse_dates=[date_col], index_col=0, squeeze=True, date_parser=parser)
    return b2.values.astype('float32')
def fonk4(b23, start_idx, train_size, test_size):
    b3 = b23[start_idx:start_idx + train_size]
    b4 = b23[start_idx + train_size:start_idx + train_size + test_size]
    return b3, b4
def fonk5(b3, b4, order):
    b5 = list(b3)
    b6 = []
    for t in range(len(b4)):
        b7 = ARIMA(b5, order=order)
        b8 = b7.fit()
        b9 = b8.forecast()[0]
        b6.append(b9)
        b10 = b4[t]
        b5.append(b10)
        print(f'Predicted: {b9}, Expected: {b10}')
    return b6
def fonk6(b4, b6):
    b11 = mean_squared_error(b4, b6)
    b12 = mean_absolute_error(b4, b6)
    b13 = fonk2(b4, b6)
    return b12, b11, b13
def fonk7(b4, b6, test_start, b14 = 'ARIMA Model Results'):
    plt.figure(b15 = (12, 6))
    plt.plot(b4[test_start:], '-', b16 = "Real Flow")
    plt.plot(b6[test_start:], '--', b17 = 'red', b16="ARIMA")
    plt.legend(b18 = 'upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (Vehicle/Period)")
    plt.ylim(0, 800)
    plt.b14(b14)
    plt.show()
def fonk8():
    b19 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    a2 = 2
    b20 = [2, 3]
    a3 = 2000
    a4 = 1100
    a5 = 500
    a6 = 300
    a7 = 10
    b21 = a6 + a7 - 1
    b22 = (4, 1, 0)
    b23 = fonk3(b19, a2, b20)
    b3, b4 = fonk4(b23, a3, a4, a5)
    b6 = fonk5(b3, b4, b22)
    b12, b11, b13 = fonk6(b4, b6)
    print(f'ARIMA Test - MAE: {b12:.3f}, MSE: {b11:.3f}, RMSE: {math.sqrt(b11):.3f}, MAPE: {b13:.3f}')
    fonk7(b4, b6, b21)
if b24 = = "__main__":
    fonk8()