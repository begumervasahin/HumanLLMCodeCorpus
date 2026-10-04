import math
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import to_datetime
import statsmodels.tsa.stattools as st
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += abs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
b3 = read_csv(b2, usecols=[2, 3], header=0, parse_dates=[0], index_col=0, date_parser=parser)
b4 = b3.values
a2 = 2
a3 = 200
b5 = b4[a2:a2 + a3]
b6 = st.adfuller(b5)
print(b6)
plt.plot(b3)
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()