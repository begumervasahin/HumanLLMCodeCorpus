import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += abs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
def fonk2(x):
    return pd.to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk3(b16):
    return pd.read_csv(b16, b2 = [2, 3], header=0, parse_dates=[0], index_col=0, date_parser=date_parser)
def fonk4(b17, train_start, b18, test_start, b19):
    b3 = b17.values.astype('float32')
    b4 = b3[train_start:b18].reshape(-1, 1)
    b5 = b3[test_start - 1:b19 - 1].reshape(-1, 1)
    b6 = b3[test_start:b19].reshape(-1, 1)
    return b4, b5, b6
def fonk5(b4):
    b7 = svm.SVR()
    b7.fit(b4[:-1], b4[1:])
    return b7
def fonk6(y_true, y_pred):
    b8 = mean_squared_error(y_true, y_pred)
    b9 = math.sqrt(b8)
    b10 = mean_absolute_error(y_true, y_pred)
    b11 = fonk1(y_true.flatten(), y_pred.flatten()) * 100
    return b8, b9, b10, b11
def fonk7(b6, b5):
    plt.figure(b12 = (10, 6))
    plt.plot(b6, '-', b13 = "Real Flow")
    plt.plot(b5, '--', b14 = 'red', b13="SVR Prediction")
    plt.legend(b15 = 'upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicle/period)")
    plt.ylim(0, 800)
    plt.title("SVR Prediction vs Real Values")
    plt.show()
def fonk8(b3, b21, num_periods):
    plt.figure(b12 = (12, 6))
    plt.plot(b3[b21:b21 + num_periods], '-', b14 = 'r', b13="Real Flow")
    plt.legend(b15 = 'upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicle/period)")
    plt.title("Real Flow for a Week")
    plt.show()
def fonk9():
    b16 = '/path/to/your/dataset/FEB15-2.csv'
    b17 = fonk3(b16)
    train_start, b18 = 4500, 6000
    test_start, b19 = 6409, 6600
    b4, b5, b6 = fonk4(b17, train_start, b18, test_start, b19)
    b7 = fonk5(b4)
    b20 = b7.predict(b5)
    b8, b9, b10, b11 = fonk6(b6, b5)
    print(f'SVR Test MAE: {b10:.3f}, MSE: {b8:.3f}, RMSE: {b9:.3f}, MAPE: {b11:.3f}%')
    fonk7(b6, b5)
    fonk8(b17.values, b21 = 31, num_periods=96*7)
if b22 = = "__main__":
    fonk9()