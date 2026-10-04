import math
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller
def fonk1(b9):
    return pd.to_datetime(b9, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    return sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true))) / len(y_true)
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b3 = pd.read_csv(b2, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
b4 = b3.values
a1 = 2
a2 = 200
b5 = b4[a1:a1 + a2]
b6 = adfuller(b5)
print("ADF Statistic:", b6[0])
print("p-value:", b6[1])
for key, value in b6[4].items():
    print(f'Critical Value ({key}): {value}')
plt.figure(b7 = (10, 6))
plt.plot(b3.index, b3.values, b8 = 'Series Data')
plt.axvline(b9 = b3.index[a1 + a2], color='r', linestyle='--', b8='Training Cutoff')
plt.legend()
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Values')
plt.show()