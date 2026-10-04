import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.b16 import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    return sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred)) / len(y_true)
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b3 = read_csv(
    b2,
    b4 = [2, 3],
    b5 = 0,
    b6 = [0],
    b7 = 0,
    b8 = True,
    b9 = parse_datetime
)
b10 = b3.values.astype('float32')
a1 = 2000
a2 = 1100
a3 = 500
a4 = 300
a5 = 10
b11 = a4 + a5 - 1
b12 = b10[a1:a1 + a2]
b13 = b10[a1 + a2:a1 + a2 + a3]
b14 = list(b12)
b15 = []
for t in range(len(b13)):
    b16 = ARIMA(b14, order=(4, 1, 0))
    b17 = b16.fit(disp=0)
    b18 = b17.forecast()[0]
    b15.append(b18)
    b19 = b13[t]
    b14.append(b19)
    print(f'Predicted: {b18}, Expected: {b19}')
b20 = mean_squared_error(b13, b15)
b21 = mean_absolute_error(b13, b15)
b22 = fonk2(b13, b15)
print(f'ARIMA Test - MAE: {b21:.3f}, MSE: {b20:.3f}, RMSE: {math.sqrt(b20):.3f}, MAPE: {b22:.3f}')
plt.figure(b23 = (12, 6))
plt.plot(b13[b11:], '-', b24 = "Real Flow")
plt.plot(b15[b11:], '--', b25 = 'red', b24="ARIMA Predictions")
plt.legend(b26 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.title("ARIMA Model Predictions vs Real Flow")
plt.show()