import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns
def fonk1(b10):
    b1 = pd.read_csv(b10)
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1.sort_values(b2 = 'Date', b3=True)
    b1.set_index('Date', b3 = True)
    return b1
def fonk2(b1):
    b1['First Difference'] = b1['Close'] - b1['Close'].shift()
    b1['Natural Log'] = np.log(b1['Close'])
    b1['Original Variance'] = b1['Close'].rolling(b4 = 30).var()
    b1['Log Variance'] = b1['Natural Log'].rolling(b4 = 30).var()
    b1['Logged First Difference'] = b1['Natural Log'].diff()
    b1['Lag 20'] = b1['Logged First Difference'].shift(20)
    return b1
def fonk3(b1):
    b5 = seasonal_decompose(b1['Natural Log'], b6='additive', period=30)
    b6 = sm.tsa.ARIMA(b1['Logged First Difference'].iloc[1:], order=(0, 0, 1))
    b7 = b6.fit(disp=-1)
    b1['Forecast'] = b7.fittedvalues
    plt.figure(b8 = (16, 12))
    plt.plot(b1['Logged First Difference'], b9 = 'Logged First Difference')
    plt.plot(b1['Forecast'], b9 = 'Forecast')
    plt.legend()
    plt.show()
def fonk4():
    sns.set_style('darkgrid')
    b10 = os.path.join(os.getcwd(), 'q_table.csv')
    b1 = fonk1(b10)
    b1 = fonk2(b1)
    fonk3(b1)
if b11 = = "__main__":
    fonk4()