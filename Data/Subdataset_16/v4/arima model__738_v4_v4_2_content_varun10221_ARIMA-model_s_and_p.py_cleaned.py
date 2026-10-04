import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set_style('darkgrid')
def fonk1():
    b1 = fonk2('q_table.csv')
    b1 = fonk3(b1)
    b6, b2 = fonk4(b1['Logged First Difference'].iloc[1:])
    b3 = fonk5(b1['Natural Log'])
    b1 = fonk6(b1)
    fonk7(b1)
def fonk2(filename):
    b4 = os.b4.join(os.getcwd(), filename)
    b1 = pd.read_csv(b4)
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1 = b1.sort_values(by='Date', ascending=True).set_index('Date')
    return b1
def fonk3(b1):
    b1['First Difference'] = b1['Close'] - b1['Close'].shift()
    b1['Natural Log'] = b1['Close'].apply(np.log)
    b1['Original Variance'] = b1['Close'].rolling(b5 = 30, center=True).var()
    b1['Log Variance'] = b1['Natural Log'].rolling(b5 = 30, center=True).var()
    b1['Logged First Difference'] = b1['Natural Log'] - b1['Natural Log'].shift(1)
    b1['Lag 20'] = b1['Logged First Difference'].shift(20)
    return b1
def fonk4(logged_diff):
    b6 = sm.tsa.acf(logged_diff)
    b2 = sm.tsa.pacf(logged_diff)
    return b6, b2
def fonk5(natural_log):
    b3 = sm.tsa.seasonal_decompose(natural_log, b7='additive', period=30)
    return b3
def fonk6(b1):
    b7 = sm.tsa.ARIMA(b1['Logged First Difference'].iloc[1:], order=(0, 0, 1))
    b8 = b7.fit(disp=-1)
    b1['Forecast'] = b8.fittedvalues
    return b1
def fonk7(b1):
    plt.figure(b9 = (16, 12))
    plt.plot(b1['Logged First Difference'], b10 = 'Actual')
    plt.plot(b1['Forecast'], b10 = 'Forecast')
    plt.legend()
    plt.show()
if b11 = = "__main__":
    fonk1()