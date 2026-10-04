import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
import statsmodels.tsa.stattools as st
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(abs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b2 / len(y_true)
def fonk3(b5):
    b3 = st.adfuller(b5)
    print(f'ADF Statistic: {b3[0]:.6f}')
    print(f'p-value: {b3[1]:.6f}')
    print('Critical Values:')
    for key, value in b3[4].items():
        print(f'\t{key}: {value:.3f}')
def fonk4(b5):
    plt.plot(b5)
    plt.title('Time Series Data')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.show()
def fonk5():
    b4 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    b5 = read_csv(
        b4,
        b6 = [2, 3],
        b7 = 0,
        b8 = [0],
        b9 = 0,
        b10 = parse_date
    )
    b11 = b5.b11
    a1 = 2
    a2 = 200
    b12 = b11[a1:a1 + a2]
    fonk3(b12)
    fonk4(b5)
if b13 = = "__main__":
    fonk5()