import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
import statsmodels.tsa.stattools as st
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b1 = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b1 / len(y_true)
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b3 = read_csv(b2, usecols=[2, 3], header=0, parse_dates=[0],
                  b4 = 0, squeeze=True, date_parser=parse_datetime)
b5 = b3.values.astype('float32')
a1 = 2000
a2 = 1100
a3 = 500
a4 = 300
a5 = 10
b6 = a4 + a5 - 1
train_data, b7 = b5[a1:a1 + a2], b5[a1 + a2:a1 + a2 + a3]
b8 = train_data.copy()
b9 = []
for observed_value in b7:
    b10 = ARIMA(b8, order=(4, 1, 0))
    b11 = b10.fit(disp=0)
    b12 = b11.forecast()[0]
    b9.append(b12)
    b8.append(observed_value)
    print(f'Predicted: {b12}, Expected: {observed_value}')
b13 = mean_squared_error(b7, b9)
b14 = mean_absolute_error(b7, b9)
b15 = fonk2(b7, b9)
print(f'ARIMA Test MAE: {b14:.3f}, MSE: {b13:.3f}, RMSE: {math.sqrt(b13):.3f}, MAPE: {b15:.3f}')
plt.plot(b7[b6:], '-', b16 = "Real Flow")
plt.plot(b9[b6:], '--', b17 = 'red', b16="ARIMA Predictions")
plt.legend(b18 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (Vehicle/Period)")
plt.ylim(0, 800)
plt.show(b19 = (12, 6))