import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
from statsmodels.tsa.arima.b10 import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    return sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true))) / len(y_true)
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b3 = read_csv(b2, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parse_date)
b4 = b3.values.astype('float32')
a1 = 2000
a2 = 1100
a3 = 500
a4 = 300
a5 = 10
b5 = a4 + a5 - 1
b6 = b4[a1:a1 + a2]
b7 = b4[a1 + a2:a1 + a2 + a3]
b8 = list(b6)
b9 = []
for t in range(len(b7)):
    b10 = ARIMA(b8, order=(4, 1, 0))
    b11 = b10.fit()
    b12 = b11.forecast()[0]
    b9.append(b12)
    b8.append(b7[t])
    print(f'Predicted: {b12}, Expected: {b7[t]}')
b13 = mean_squared_error(b7, b9)
b14 = mean_absolute_error(b7, b9)
b15 = fonk2(b7, b9)
print(f'ARIMA Test - MAE: {b14:.3f}, MSE: {b13:.3f}, RMSE: {math.sqrt(b13):.3f}, MAPE: {b15:.3f}')
plt.figure(b16 = (12, 6))
plt.plot(b7[b5:], '-', b17 = "Real Flow")
plt.plot(b9[b5:], '--', b18 = 'red', b17="ARIMA")
plt.legend(b19 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.title("ARIMA Model Predictions vs Real Data")
plt.show()