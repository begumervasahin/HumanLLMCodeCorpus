import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
from statsmodels.tsa.arima.b12 import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += abs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
b2 = read_csv('/path/to/your/FEB15-2.csv', usecols=[2, 3], header=0, parse_dates=[0],
                  b3 = 0, squeeze=True, date_parser=parser)
b4 = b2.values.astype('float32')
start, size, b5 = 2000, 1100, 500
line_test_size, b6 = 300, 10
b7 = line_test_size + b6 - 1
b8 = b4[start:start + size]
b9 = b4[start + size:start + size + b5]
b10 = list(b8)
b11 = []
for t in range(len(b9)):
    b12 = ARIMA(b10, order=(4, 1, 0))
    b13 = b12.fit()
    b14 = b13.forecast()[0]
    b11.append(b14)
    b15 = b9[t]
    b10.append(b15)
    print(f'b16 = {b14:.6f}, expected={b15:.6f}')
b17 = mean_squared_error(b9, b11)
b18 = mean_absolute_error(b9, b11)
b19 = fonk2(b9, b11)
print(f'ARIMA Test MAE: {b18:.3f} MSE: {b17:.3f} RMSE: {math.sqrt(b17):.3f} MAPE: {b19:.3f}')
plt.figure(b20 = (12, 6))
plt.plot(b9[b7:], '-', b21 = "Real Flow")
plt.plot(b11[b7:], '--', b22 = 'red', b21="ARIMA Predictions")
plt.legend(b23 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()