import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.b12 import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    return sum(abs(pred - true) / true for true, pred in zip(y_true, y_pred)) / len(y_true)
def fonk3(filepath):
    return read_csv(
        filepath,
        b2 = [2, 3],
        b3 = 0,
        b4 = [0],
        b5 = 0,
        b6 = True,
        b7 = parse_datetime
    ).values.astype('float32')
def fonk4(data, start_index, train_size, test_size):
    b8 = data[start_index:start_index + train_size]
    b9 = data[start_index + train_size:start_index + train_size + test_size]
    return b8, b9
def fonk5(b8, b9, arima_order):
    b10 = list(b8)
    b11 = []
    for t in range(len(b9)):
        b12 = ARIMA(b10, order=arima_order)
        b13 = b12.fit(disp=0)
        b14 = b13.forecast()[0]
        b11.append(b14)
        b15 = b9[t]
        b10.append(b15)
        print(f'Predicted: {b14}, Expected: {b15}')
    return b11
def fonk6(b9, b11):
    b16 = mean_squared_error(b9, b11)
    b17 = mean_absolute_error(b9, b11)
    b18 = fonk2(b9, b11)
    print(f'ARIMA Test - MAE: {b17:.3f}, MSE: {b16:.3f}, RMSE: {math.sqrt(b16):.3f}, MAPE: {b18:.3f}')
def fonk7(b9, b11, test_start):
    plt.figure(b19 = (12, 6))
    plt.plot(b9[test_start:], '-', b20 = "Real Flow")
    plt.plot(b11[test_start:], '--', b21 = 'red', b20="ARIMA Predictions")
    plt.legend(b22 = 'upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (Vehicle/Period)")
    plt.ylim(0, 800)
    plt.title("ARIMA Model Predictions vs Real Flow")
    plt.show()
b23 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
a1 = 2000
a2 = 1100
a3 = 500
a4 = 300
a5 = 10
b24 = a4 + a5 - 1
b25 = (4, 1, 0)
if b26 = = "__main__":
    b27 = fonk3(b23)
    b8, b9 = fonk4(b27, a1, a2, a3)
    b11 = fonk5(b8, b9, b25)
    fonk6(b9, b11)
    fonk7(b9, b11, b24)