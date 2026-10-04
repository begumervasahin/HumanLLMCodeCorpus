import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set_style('darkgrid')
def fonk1(b11):
    b1 = pd.read_csv(b11)
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1 = b1.sort_values(by='Date', ascending=True)
    b1 = b1.set_index('Date')
    return b1
def fonk2(b1):
    b1['First Difference'] = b1['Close'] - b1['Close'].shift()
    b1['Natural Log'] = b1['Close'].apply(np.log)
    b1['Original Variance'] = b1['Close'].rolling(b2 = 30, center=True).var()
    b1['Log Variance'] = b1['Natural Log'].rolling(b2 = 30, center=True).var()
    b1['Logged First Difference'] = b1['Natural Log'] - b1['Natural Log'].shift(1)
    b1['Lag 20'] = b1['Logged First Difference'].shift(20)
    return b1
def fonk3(b1):
    b3 = b1['Logged First Difference'].dropna()
    b4 = sm.tsa.acf(b3)
    b5 = sm.tsa.pacf(b3)
    return b4, b5
def fonk4(b1):
    b6 = sm.tsa.seasonal.seasonal_decompose(b1['Natural Log'].dropna(), b7='additive', period=30)
    return b6
def fonk5(b1):
    b3 = b1['Logged First Difference'].dropna()
    b7 = sm.tsa.ARIMA(b3, order=(0, 0, 1))
    b8 = b7.fit(disp=-1)
    return b8
def fonk6(b1, b8):
    b1['Forecast'] = b8.fittedvalues
    plt.figure(b9 = (16, 12))
    plt.plot(b1['Logged First Difference'], b10 = 'Actual')
    plt.plot(b1['Forecast'], b10 = 'Forecast')
    plt.legend()
    plt.show()
def fonk7():
    b11 = os.path.join(os.getcwd(), 'q_table.csv')
    b1 = fonk1(b11)
    b1 = fonk2(b1)
    b4, b5 = fonk3(b1)
    b6 = fonk4(b1)
    b12 = fonk5(b1)
    fonk6(b1, b12)
if b13 = = "__main__":
    fonk7()