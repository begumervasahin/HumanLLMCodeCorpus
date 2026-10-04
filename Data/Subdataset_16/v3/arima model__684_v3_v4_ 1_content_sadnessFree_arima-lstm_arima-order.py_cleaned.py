import math
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.tsa.stattools as st
import seaborn as sns
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    a1 = 0
    for i in range(len(y_true)):
        a1 += math.fabs(y_pred[i] - y_true[i]) / y_true[i]
    return a1 / len(y_true)
def fonk3(b9):
    return pd.read_csv(
        b9,
        b1 = [2, 3],
        b2 = 0,
        b3 = [0],
        b4 = 0,
        b5 = True,
        b6 = parser
    )
def fonk4(data):
    b7 = st.adfuller(data)
    fonk5(b7)
    return b7
def fonk5(b7):
    print('ADF Statistic: %f' % b7[0])
    print('p-value: %f' % b7[1])
    print('Critical Values:')
    for key, value in b7[4].items():
        print('\t%s: %.3f' % (key, value))
def fonk6(b10):
    plt.figure(b8 = (10, 6))
    plt.plot(b10.index, b10.values)
    plt.title('Time Series Data')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.show()
def fonk7():
    b9 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    b10 = fonk3(b9)
    b11 = b10.values
    a2 = 2
    a3 = 200
    b12 = b11[a2:a2 + a3]
    fonk4(b12)
    fonk6(b10)
if b13 = = "__main__":
    fonk7()