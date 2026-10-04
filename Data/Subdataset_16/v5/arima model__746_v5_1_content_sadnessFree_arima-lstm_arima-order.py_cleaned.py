import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true)))
    return b2 / len(y_true)
b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b4 = read_csv(b3, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parse_dates)
b5 = b4.values
a1 = 2
a2 = 200
b6 = b5[a1:a1 + a2]
b7 = st.adfuller(b6)
print("ADF Test Result:", b7)
plt.figure(b8 = (10, 5))
plt.plot(b4)
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()