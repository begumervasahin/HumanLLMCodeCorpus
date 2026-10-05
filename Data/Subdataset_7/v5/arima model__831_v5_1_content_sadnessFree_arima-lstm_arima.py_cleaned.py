import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b1 = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b1 / len(y_true)
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b3 = read_csv(b2, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parse_datetime)
b4 = b3.values.astype('float32')
a1 = 2000
a2 = 1100
a3 = 500
a4 = 300
a5 = 10
b5 = a4 + a5 - 1
arima_train, b6 = b4[a1:a1 + a2], b4[a1 + a2:a1 + a2 + a3]
b7 = list(arima_train)
b8 = []
for t in range(len(b6)):
    b9 = ARIMA(b7, order=(4, 1, 0))
    b10 = b9.fit(disp=0)
    b11 = b10.forecast()[0]
    b8.append(b11)
    b12 = b6[t]
    b7.append(b12)
    print(f'Predicted: {b11}, Expected: {b12}')
b13 = mean_squared_error(b6, b8)
b14 = mean_absolute_error(b6, b8)
b15 = fonk2(b6, b8)
print(f'ARIMA Test - MAE: {b14:.3f}, MSE: {b13:.3f}, RMSE: {math.sqrt(b13):.3f}, MAPE: {b15:.3f}')
plt.plot(b6[b5:], '-', b16 = "Real Flow")
plt.plot(b8[b5:], '--', b17 = 'red', b16="ARIMA")
plt.legend(b18 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show(b19 = (12, 6))