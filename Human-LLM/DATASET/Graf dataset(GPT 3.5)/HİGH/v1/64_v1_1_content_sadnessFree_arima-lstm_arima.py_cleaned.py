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
b1 = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0, parse_dates=[0],
                  b2 = 0, squeeze=True, date_parser=parser)
b3 = b1.values
b3 = b3.astype('float32')
a2 = 2000
a3 = 1100
a4 = 500
a5 = 300
a6 = 10
b4 = a5 + a6 - 1
arima_train, b5 = b3[a2:a2 + a3], b3[a2 + a3:a2 + a3 + a4]
b6 = [x for x in arima_train]
b7 = list()
for t in range(len(b5)):
    b8 = ARIMA(b6, order=(4, 1, 0))
    b9 = b8.fit(disp=0)
    b10 = b9.forecast()
    b11 = b10[0]
    b7.append(b11)
    b12 = b5[t]
    b6.append(b12)
    print('b13 = %f, expected=%f' % (b11, b12))
b14 = mean_squared_error(b5, b7)
b15 = mean_absolute_error(b5, b7)
b16 = fonk2(b5, b7)
print('ARIMA Test MAE:%.3f MSE: %.3f RMSE:%.3f MAPE:%.3f' % (b15, b14, math.sqrt(b14), b16))
plt.plot(b5[b4:], '-', b17 = "real flow")
plt.plot(b7[b4:], '--', b18 = 'red', b17="ARIMA")
plt.legend(b19 = 'upper right')
plt.xlabel("period(15-minute intervals)")
plt.ylabel("volume(vehicle/period)")
plt.ylim(0, 800)
plt.show(b20 = (12, 6))