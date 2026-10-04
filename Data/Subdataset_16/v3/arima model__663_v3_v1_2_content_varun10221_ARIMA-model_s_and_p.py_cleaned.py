import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
sb.set_style('darkgrid')
def fonk1(b12):
    b1 = pd.read_csv(b12)
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1.sort_values(b2 = 'Date', ascending=True, b3=True)
    b1.set_index('Date', b3 = True)
    return b1
def fonk2(b1):
    b1['First Difference'] = b1['Close'].diff()
    b1['Natural Log'] = b1['Close'].apply(np.log)
    b1['Logged First Difference'] = b1['Natural Log'].diff()
    return b1
def fonk3(b1):
    b1['Original Variance'] = b1['Close'].rolling(b4 = 30).var()
    b1['Log Variance'] = b1['Natural Log'].rolling(b4 = 30).var()
    return b1
def fonk4(b1):
    b1['Lag 20'] = b1['Logged First Difference'].shift(20)
    return b1
def fonk5(b1):
    b5 = acf(b1['Logged First Difference'].dropna())
    b6 = pacf(b1['Logged First Difference'].dropna())
    return b5, b6
def fonk6(b1):
    b7 = seasonal_decompose(b1['Natural Log'].dropna(), b8='additive', period=30)
    return b7
def fonk7(b1):
    b8 = sm.tsa.ARIMA(b1['Logged First Difference'].dropna(), order=(0, 0, 1))
    b9 = b8.fit(disp=-1)
    return b9
def fonk8(b1, b9):
    b1['Forecast'] = b9.fittedvalues
    plt.figure(b10 = (16, 12))
    plt.plot(b1['Logged First Difference'], b11 = 'Logged First Difference')
    plt.plot(b1['Forecast'], b11 = 'Forecast', color='red')
    plt.title('Logged First Difference and Forecast')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
def fonk9():
    b12 = os.path.join(os.getcwd(), 'q_table.csv')
    b1 = fonk1(b12)
    b1 = fonk2(b1)
    b1 = fonk3(b1)
    b1 = fonk4(b1)
    b5, b6 = fonk5(b1)
    b7 = fonk6(b1)
    b9 = fonk7(b1)
    fonk8(b1, b9)
if b13 = = "__main__":
    fonk9()