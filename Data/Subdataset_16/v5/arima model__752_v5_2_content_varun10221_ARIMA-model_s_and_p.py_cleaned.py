import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sb
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
sb.set_style('darkgrid')
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1 = b1.sort_values(by='Date').set_index('Date')
    return b1
def fonk2(b1):
    b1['First Difference'] = b1['Close'] - b1['Close'].shift()
    b1['Natural Log'] = np.log(b1['Close'])
    b1['Original Variance'] = b1['Close'].rolling(b2 = 30, center=True).var()
    b1['Log Variance'] = b1['Natural Log'].rolling(b2 = 30, center=True).var()
    b1['Logged First Difference'] = b1['Natural Log'].diff()
    b1['Lag 20'] = b1['Logged First Difference'].shift(20)
    return b1
def fonk3(logged_diff):
    b3 = acf(logged_diff.dropna())
    b4 = pacf(logged_diff.dropna())
    return b3, b4
def fonk4(series, b5 = 30):
    b6 = seasonal_decompose(series, b7='additive', b5=b5)
    return b6
def fonk5(logged_diff):
    b7 = sm.tsa.ARIMA(logged_diff.dropna(), order=(0, 0, 1))
    b8 = b7.fit(disp=-1)
    return b8
def fonk6(b1):
    plt.figure(b9 = (16, 12))
    b1[['Logged First Difference', 'Forecast']].plot()
    plt.show()
def fonk7():
    b10 = os.b10.join(os.getcwd(), 'q_table.csv')
    b1 = fonk1(b10)
    b1 = fonk2(b1)
    b3, b4 = fonk3(b1['Logged First Difference'])
    b6 = fonk4(b1['Natural Log'])
    b8 = fonk5(b1['Logged First Difference'])
    b1['Forecast'] = b8.fittedvalues
    fonk6(b1)
if b11 = = "__main__":
    fonk7()