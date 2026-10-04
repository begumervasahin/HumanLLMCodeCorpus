import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.b8 import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    return sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true))) / len(y_true)
def fonk3(filepath, date_column, value_column, date_parser):
    b2 = read_csv(filepath, usecols=[date_column, value_column], header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=date_parser)
    return b2.values.astype('float32')
def fonk4(data, start_index, train_size, test_size):
    b3 = data[start_index:start_index + train_size]
    b4 = data[start_index + train_size:start_index + train_size + test_size]
    return b3, b4
def fonk5(b3, b4, b5 = (4, 1, 0)):
    b6 = list(b3)
    b7 = []
    for t in range(len(b4)):
        b8 = ARIMA(b6, b5=b5)
        b9 = b8.fit()
        b10 = b9.forecast()[0]
        b7.append(b10)
        b6.append(b4[t])
        print(f'Predicted: {b10}, Expected: {b4[t]}')
    return b7
def fonk6(b4, b7):
    b11 = mean_squared_error(b4, b7)
    b12 = mean_absolute_error(b4, b7)
    b13 = fonk2(b4, b7)
    b14 = math.sqrt(b11)
    print(f'ARIMA Test - MAE: {b12:.3f}, MSE: {b11:.3f}, RMSE: {b14:.3f}, MAPE: {b13:.3f}')
    return b11, b12, b13, b14
def fonk7(b4, b7, test_start, b23, b24, b25, b26, b15 = (12, 6)):
    plt.figure(b15 = b15)
    plt.plot(b4[test_start:], '-', b16 = "Real Flow")
    plt.plot(b7[test_start:], '--', b17 = 'red', b16="ARIMA")
    plt.legend(b18 = 'upper right')
    plt.b24(b24)
    plt.b25(b25)
    plt.b26(b26)
    plt.b23(b23)
    plt.show()
if b19 = = "__main__":
    b20 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    a1 = 2
    a2 = 3
    a3 = 2000
    a4 = 1100
    a5 = 500
    a6 = 300
    a7 = 10
    b21 = a6 + a7 - 1
    b22 = fonk3(b20, a1, a2, parse_date)
    b3, b4 = fonk4(b22, a3, a4, a5)
    b7 = fonk5(b3, b4)
    b11, b12, b13, b14 = fonk6(b4, b7)
    fonk7(
        b4, b7, b21,
        b23 = "ARIMA Model Predictions vs Real Data",
        b24 = "Period (15-minute intervals)",
        b25 = "Volume (Vehicle/Period)",
        b26 = (0, 800)
    )