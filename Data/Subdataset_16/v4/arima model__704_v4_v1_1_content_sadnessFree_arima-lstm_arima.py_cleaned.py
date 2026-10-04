import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.b11 import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    return sum(math.fabs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true))) / len(y_true)
b2 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv',
                  b3 = [2, 3], header=0, parse_dates=[0], index_col=0,
                  b4 = True, date_parser=parser)
b5 = b2.values.astype('float32')
a1 = 2000
a2 = 1100
a3 = 500
a4 = 300
a5 = 10
b6 = a4 + a5 - 1
b7 = b5[a1:a1 + a2]
b8 = b5[a1 + a2:a1 + a2 + a3]
b9 = [x for x in b7]
b10 = []
for t in range(len(b8)):
    b11 = ARIMA(b9, order=(4, 1, 0))
    b12 = b11.fit()
    b13 = b12.forecast()[0]
    b10.append(b13)
    b14 = b8[t]
    b9.append(b14)
    print(f'b15 = {b13:.6f}, expected={b14:.6f}')
b16 = mean_squared_error(b8, b10)
b17 = mean_absolute_error(b8, b10)
b18 = fonk2(b8, b10)
print(f'ARIMA Test MAE: {b17:.3f} MSE: {b16:.3f} RMSE: {math.sqrt(b16):.3f} MAPE: {b18:.3f}')
plt.figure(b19 = (12, 6))
plt.plot(b8[b6:], '-', b20 = "Real Flow")
plt.plot(b10[b6:], '--', b21 = 'red', b20="ARIMA")
plt.legend(b22 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()