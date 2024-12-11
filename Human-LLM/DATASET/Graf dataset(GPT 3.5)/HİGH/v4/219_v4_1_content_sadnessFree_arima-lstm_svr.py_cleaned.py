
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
def fonk1(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += abs(y_pred[i] - y_true[i]) / y_true[i]
    return (a1 / len(y_true)) * 100
def fonk2(x):
    return pd.to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
b2 = pd.read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv', usecols=[2, 3], header=0,
                   b3 = [0], index_col=0, squeeze=True, date_parser=parse_datetime)
b4 = b2.b4.astype('float32')
train_start_index, b5 = 4500, 6000
test_start_index, b6 = 6409, 6600
b9, b7 = b4[train_start_index:b5], b4[test_start_index - 1:b6 - 1]
b8 = np.array(b4[test_start_index:b6]).reshape(-1, 1)
b9 = np.array(b9).reshape(-1, 1)
b7 = np.array(b7).reshape(-1, 1)
b10 = svm.SVR()
b10.fit(b9[0:b5 - train_start_index - 1], b9[1:b5 - train_start_index])
b11 = b10.predict(b7)
b12 = mean_squared_error(b8, b7)
b13 = math.sqrt(b12)
b14 = mean_absolute_error(b8, b7)
b15 = fonk1(b8, b7)
print('SVR Test MAE: %.3f MSE: %.3f RMSE: %.3f MAPE: %.3f%%' % (b14, b12, b13, b15))
plt.plot(b8, '-', b16 = "Real Flow")
plt.plot(b11, '--', b17 = 'red', b16="SVR Predictions")
plt.legend(b18 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicles/period)")
plt.ylim(0, 800)
plt.show()
a2 = 31
plt.figure(b19 = (12, 6))
plt.plot(b4[a2:a2 + 96*7], '-', b17 = 'r', b16="Real Traffic Flow")
plt.legend(b18 = 'upper right')
plt.xlabel("Period (15 minutes)")
plt.ylabel("Traffic Volume (vehicles/period)")
plt.show()