import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.b4 import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(date_str):
    return to_datetime(date_str, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return b2 / len(y_true)
def fonk3(file_path, b3, date_col, parser_func):
    return read_csv(file_path, b3 = b3, header=0, parse_dates=[date_col], index_col=date_col, date_parser=parser_func)
def fonk4(b16, order):
    b4 = ARIMA(b16, order=order)
    return b4.fit()
def fonk5(real_data, b17, start_idx):
    plt.plot(real_data[start_idx:], '-', b5 = "Real Flow")
    plt.plot(b17[start_idx:], '--', b6 = 'red', b5="ARIMA")
    plt.legend(b7 = 'upper right')
    plt.xlabel("Period (15-minute intervals)")
    plt.ylabel("Volume (vehicle/period)")
    plt.ylim(0, 800)
    plt.gcf().set_size_inches(12, 6)
    plt.show()
b8 = 'path/to/your/FEB15-2.csv'
b9 = [2, 3]
a1 = 0
a2 = 2000
a3 = 1100
a4 = 500
a5 = 300
a6 = 10
b10 = a5 + a6 - 1
b11 = (4, 1, 0)
b12 = fonk3(b8, b9, a1, parse_dates)
b13 = b12.values.astype('float32')
b14 = b13[a2:a2 + a3]
b15 = b13[a2 + a3:a2 + a3 + a4]
b16 = list(b14)
b17 = []
for t in range(len(b15)):
    b18 = fonk4(b16, b11)
    b19 = b18.b19()
    b20 = b19[0]
    b17.append(b20)
    b21 = b15[t]
    b16.append(b21)
    print(f'b22 = {b20[0]:.6f}, expected={b21[0]:.6f}')
b23 = mean_squared_error(b15, b17)
b24 = mean_absolute_error(b15, b17)
b25 = fonk2(b15, b17)
b26 = math.sqrt(b23)
print(f'ARIMA Test MAE: {b24:.3f} MSE: {b23:.3f} RMSE: {b26:.3f} MAPE: {b25:.3f}')
fonk5(b15, b17, b10)