import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.b4 import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    return sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true))) / len(y_true)
def fonk3(b14):
    return read_csv(b14, b2 = [2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser).values.astype('float32')
def fonk4(b18, b3 = (4, 1, 0)):
    b4 = ARIMA(b18, b3=b3)
    b5 = b4.fit()
    return b5.forecast()[0]
def fonk5(y_true, y_pred):
    b6 = mean_squared_error(y_true, y_pred)
    b7 = mean_absolute_error(y_true, y_pred)
    b8 = fonk2(y_true, y_pred)
    print(f'ARIMA Test MAE: {b7:.3f}, MSE: {b6:.3f}, RMSE: {math.sqrt(b6):.3f}, MAPE: {b8:.3f}')
    return b7, b6, math.sqrt(b6), b8
def fonk6(real, b22, b16, b9 = "Volume (vehicle/period)"):
    plt.figure(b10 = (12, 6))
    plt.plot(real[b16:], '-', b11 = "Real flow")
    plt.plot(b22[b16:], '--', b12 = 'red', b11="ARIMA")
    plt.legend(b13 = 'upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.b9(b9)
    plt.ylim(0, 800)
    plt.show()
def fonk7():
    b14 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    b15 = fonk3(b14)
    a1 = 2000
    a2 = 1100
    a3 = 500
    a4 = 300
    a5 = 10
    b16 = a4 + a5 - 1
    arima_train, b17 = b15[a1:a1 + a2], b15[a1 + a2:a1 + a2 + a3]
    b18 = list(arima_train)
    b19 = []
    for t in range(len(b17)):
        b20 = fonk4(b18)
        b19.append(b20)
        b21 = b17[t]
        b18.append(b21)
        print(f'b22 = {b20:.6f}, expected={b21:.6f}')
    fonk5(b17, b19)
    fonk6(b17, b19, b16)
if b23 = = "__main__":
    fonk7()