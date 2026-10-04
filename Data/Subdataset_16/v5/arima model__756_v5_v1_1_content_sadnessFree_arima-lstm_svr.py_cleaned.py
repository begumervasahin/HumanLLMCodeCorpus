import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(y_true, y_pred):
    b1 = np.sum(np.abs((y_true - y_pred) / y_true))
    return b1 / len(y_true)
def fonk2(x):
    return pd.to_datetime(x, b2 = '%Y-%m-%d %H:%M:%S')
def fonk3(file_path, b3, date_col):
    return pd.read_csv(file_path, b3 = b3, header=0, parse_dates=[date_col],
                       b4 = 0, squeeze=True, date_parser=parse_dates).values.astype('float32')
def fonk4(train_data):
    b5 = svm.SVR()
    b5.fit(train_data[:-1], train_data[1:])
    return b5
def fonk5(y_true, y_pred):
    b6 = mean_squared_error(y_true, y_pred)
    b7 = math.sqrt(b6)
    b8 = mean_absolute_error(y_true, y_pred)
    b9 = fonk1(y_true.flatten(), y_pred.flatten()) * 100
    return b8, b6, b7, b9
def fonk6(real, predicted, title, xlabel, ylabel, ylim, b10 = 'upper right'):
    plt.figure(b11 = (10, 5))
    plt.plot(real, '-', b12 = "Real Flow")
    plt.plot(predicted, '--', b13 = 'red', b12="Predicted Flow")
    plt.legend(b14 = b10)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(ylim)
    plt.title(title)
    plt.show()
b15 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b16 = [2, 3]
a1 = 0
TRAIN_START, b17 = 4500, 6000
TEST_START, b18 = 6409, 6600
b19 = fonk3(b15, b16, a1)
b20 = b19[TRAIN_START:b17].reshape(-1, 1)
b21 = b19[TEST_START - 1:b18 - 1].reshape(-1, 1)
b22 = b19[TEST_START:b18].reshape(-1, 1)
b5 = fonk4(b20)
b23 = b5.predict(b21)
b8, b6, b7, b9 = fonk5(b22, b21)
print(f'SVR Test MAE: {b8:.3f}, MSE: {b6:.3f}, RMSE: {b7:.3f}, MAPE: {b9:.3f}%')
fonk6(b22, b21, "SVR Prediction vs Real Values", "Period (15-minute intervals)",
             "Volume (vehicle/period)", (0, 800))
a2 = 31
plt.figure(b11 = (12, 6))
plt.plot(b19[a2:a2 + 96 * 7], '-', b13 = 'r', b12="Real Flow")
plt.legend(b14 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Real Flow for a Week")
plt.show()