import math
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import datetime
import statsmodels.tsa.stattools as st
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
b1 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0, parse_dates=[0],
                  b2 = 0,
                  b3 = True,
                  b4 = parser)
b5 = b1.values
b5 = b5.astype('float32')
a2 = 2000
a3 = 1100
a4 = 500
a5 = 300
a6 = 10
b6 = a5 + a6 - 1
arima_train, b7 = b5[a2:a2 + a3], b5[a2 + a3:a2 + a3 + a4]
b8 = [x for x in arima_train]
b9 = list()
for t in range(len(b7)):
    b10 = ARIMA(b8, order=(4, 1, 0))
    b11 = b10.fit(disp=0)
    b12 = b11.forecast()
    b13 = b12[0]
    b9.append(b13)
    b14 = b7[t]
    b8.append(b14)
    print('b15 = %f, expected=%f' % (b13, b14))
b16 = mean_squared_error(b7, b9)
b17 = mean_absolute_error(b7, b9)
b18 = fonk2(b7, b9)
print('ARIMA Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b17, b16, math.sqrt(b16), b18))
plt.plot(b7[b6:], '-', b19 = "real flow")
plt.plot(b9[b6:], '--', b20 = 'red', b19="ARIMA")
plt.legend(b21 = 'upper right')
plt.xlabel("period(15-minute intervals)")
plt.ylabel("volume(vehicle/period)")
plt.ylim(0, 800)
plt.show(b22 = (12, 6))