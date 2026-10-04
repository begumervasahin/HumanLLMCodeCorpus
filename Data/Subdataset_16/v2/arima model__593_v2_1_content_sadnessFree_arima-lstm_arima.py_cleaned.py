import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.b10 import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return b2 / len(y_true)
b3 = 'path/to/your/FEB15-2.csv'
b4 = read_csv(b3, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
b5 = b4.values.astype('float32')
a1 = 2000
a2 = 1100
a3 = 500
a4 = 300
a5 = 10
b6 = a4 + a5 - 1
train_data, b7 = b5[a1:a1 + a2], b5[a1 + a2:a1 + a2 + a3]
b8 = list(train_data)
b9 = []
for t in range(len(b7)):
    b10 = ARIMA(b8, order=(4, 1, 0))
    b11 = b10.fit()
    b12 = b11.b12()
    b13 = b12[0]
    b9.append(b13)
    b14 = b7[t]
    b8.append(b14)
    print(f'b15 = {b13[0]:.6f}, expected={b14[0]:.6f}')
b16 = mean_squared_error(b7, b9)
b17 = mean_absolute_error(b7, b9)
b18 = fonk2(b7, b9)
b19 = math.sqrt(b16)
print(f'ARIMA Test MAE: {b17:.3f} MSE: {b16:.3f} RMSE: {b19:.3f} MAPE: {b18:.3f}')
plt.plot(b7[b6:], '-', b20 = "Real Flow")
plt.plot(b9[b6:], '--', b21 = 'red', b20="ARIMA")
plt.legend(b22 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.gcf().set_size_inches(12, 6)
plt.show()