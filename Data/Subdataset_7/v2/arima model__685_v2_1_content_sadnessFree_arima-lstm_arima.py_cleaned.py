import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
import statsmodels.tsa.stattools as st
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
b1 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b2 = read_csv(b1, usecols=[2, 3], header=0, parse_dates=[0],
                  b3 = 0, squeeze=True, date_parser=parser)
b4 = b2.values.astype('float32')
a2 = 2000
a3 = 1100
a4 = 500
a5 = 300
a6 = 10
b5 = a5 + a6 - 1
train_data, b6 = b4[a2:a2 + a3], b4[a2 + a3:a2 + a3 + a4]
b7 = [x for x in train_data]
b8 = []
for t in range(len(b6)):
    b9 = ARIMA(b7, order=(4, 1, 0))
    b10 = b9.fit(disp=0)
    b11 = b10.b11()
    b12 = b11[0]
    b8.append(b12)
    b13 = b6[t]
    b7.append(b13)
    print(f'Predicted: {b12}, Expected: {b13}')
b14 = mean_squared_error(b6, b8)
b15 = mean_absolute_error(b6, b8)
b16 = fonk2(b6, b8)
print(f'ARIMA Test MAE: {b15:.3f}, MSE: {b14:.3f}, RMSE: {math.sqrt(b14):.3f}, MAPE: {b16:.3f}')
plt.plot(b6[b5:], '-', b17 = "Real Flow")
plt.plot(b8[b5:], '--', b18 = 'red', b17="ARIMA Predictions")
plt.legend(b19 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show(b20 = (12, 6))