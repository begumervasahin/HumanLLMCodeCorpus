import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
from datetime import datetime
def fonk1(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true))
def fonk2(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
b1 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b2 = pd.read_csv(b1, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=date_parser)
b3 = b2.values.astype('float32')
TRAIN_START, b4 = 4500, 6000
TEST_START, b5 = 6409, 6600
b6 = b3[TRAIN_START:b4].reshape(-1, 1)
b7 = b3[TEST_START-1:b5-1].reshape(-1, 1)
b8 = b3[TEST_START:b5].reshape(-1, 1)
b9 = svm.SVR()
b9.fit(b6[:-1], b6[1:])
b10 = b9.predict(b7)
b11 = mean_squared_error(b8, b7)
b12 = math.sqrt(b11)
b13 = mean_absolute_error(b8, b7)
b14 = fonk1(b8, b7)
print(f'SVR Test MAE: {b13:.3f} MSE: {b11:.3f} RMSE: {b12:.3f} MAPE: {b14:.3f}')
plt.figure(b15 = (12, 6))
plt.plot(b8, '-', b16 = "Real Flow")
plt.plot(b7, '--', b17 = 'red', b16="SVR")
plt.legend(b18 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()
a1 = 31
plt.figure(b15 = (12, 6))
plt.plot(b3[a1:a1 + 96*7], '-', b17 = 'r', b16="Real Flow")
plt.legend(b18 = 'upper right')
plt.xlabel("Period (15min)")
plt.ylabel("Traffic Volume (vehicles/period)")
plt.show()