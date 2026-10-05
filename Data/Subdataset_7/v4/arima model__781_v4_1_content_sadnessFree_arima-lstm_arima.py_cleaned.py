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
b2 = read_csv(b1, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
b3 = b2.values.astype('float32')
a2 = 2000
a3 = 1100
a4 = 500
a5 = 300
a6 = 10
b4 = a5 + a6 - 1
arima_train, b5 = b3[a2:a2 + a3], b3[a2 + a3:a2 + a3 + a4]
b6 = list(arima_train)
b7 = []
for t in range(len(b5)):
    b8 = ARIMA(b6, order=(4, 1, 0))
    b9 = b8.fit(disp=0)
    b10 = b9.forecast()[0]
    b7.append(b10)
    b11 = b5[t]
    b6.append(b11)
    print(f'Predicted: {b10}, Expected: {b11}')
b12 = mean_squared_error(b5, b7)
b13 = mean_absolute_error(b5, b7)
b14 = fonk2(b5, b7)
print(f'ARIMA Test - MAE: {b13:.3f}, MSE: {b12:.3f}, RMSE: {math.sqrt(b12):.3f}, MAPE: {b14:.3f}')
plt.plot(b5[b4:], '-', b15 = "Real Flow")
plt.plot(b7[b4:], '--', b16 = 'red', b15="ARIMA")
plt.legend(b17 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show(b18 = (12, 6))