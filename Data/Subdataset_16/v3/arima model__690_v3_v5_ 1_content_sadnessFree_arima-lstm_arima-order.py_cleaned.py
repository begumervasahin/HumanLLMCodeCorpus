import math
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.tsa.stattools as st
from pandas import read_csv, to_datetime
def fonk1(date_string):
    return to_datetime(date_string, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(actual_values, predicted_values):
    b2 = sum(abs(predicted - actual) / actual for actual, predicted in zip(actual_values, predicted_values))
    return b2 / len(actual_values)
def fonk3():
    b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv'
    b4 = read_csv(b3, usecols=[2, 3], header=0, parse_dates=[0],
                      b5 = 0, squeeze=True, date_parser=parse_datetime)
    b6 = b4.values
    a1 = 2
    a2 = 200
    b7 = b6[a1:a1 + a2]
    b8 = st.adfuller(b7)
    print(f'ADF Statistic: {b8[0]:.6f}')
    print(f'p-value: {b8[1]:.6f}')
    print('Critical Values:')
    for key, value in b8[4].items():
        print(f'{key}: {value:.3f}')
if b9 = = "__main__":
    fonk3()