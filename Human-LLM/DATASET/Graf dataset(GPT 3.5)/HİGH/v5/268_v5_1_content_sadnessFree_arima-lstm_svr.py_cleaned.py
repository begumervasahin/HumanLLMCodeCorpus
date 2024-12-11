import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(y_true, y_pred):
    b1 = np.abs(y_true - y_pred)
    return np.mean(b1 / y_true) * 100
def fonk2(x):
    return pd.to_datetime(x, b2 = '%Y-%m-%d %H:%M:%S')
b3 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv',
                   b4 = [2, 3],
                   b5 = 0,
                   b6 = [0],
                   b7 = 0,
                   b8 = True,
                   b9 = parse_datetime)
b10 = b3.b10.astype('float32')
train_start_index, b11 = 4500, 6000
test_start_index, b12 = 6409, 6600
b13 = b10[train_start_index:b11]
b14 = b10[test_start_index - 1:b12 - 1]
b15 = b10[test_start_index:b12].reshape(-1, 1)
b13 = b13.reshape(-1, 1)
b14 = b14.reshape(-1, 1)
b16 = svm.SVR()
b16.fit(b13[:-1], b13[1:])
b17 = b16.predict(b14)
b18 = mean_squared_error(b15, b14)
b19 = math.sqrt(b18)
b20 = mean_absolute_error(b15, b14)
b21 = fonk1(b15, b14)
print('SVR Test MAE: %.3f, MSE: %.3f, RMSE: %.3f, MAPE: %.3f%%' % (b20, b18, b19, b21))
plt.plot(b15, b22 = "Real Flow")
plt.plot(b17, '--', b23 = 'red', b22="SVR Predictions")
plt.legend(b24 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicles/period)")
plt.ylim(0, 800)
plt.show()
a1 = 31
plt.figure(b25 = (12, 6))
plt.plot(b10[a1:a1 + 96*7], b22 = "Real Traffic Flow", b23='r')
plt.legend(b24 = 'upper right')
plt.xlabel("Period (15 minutes)")
plt.ylabel("Traffic Volume (vehicles/period)")
plt.show()