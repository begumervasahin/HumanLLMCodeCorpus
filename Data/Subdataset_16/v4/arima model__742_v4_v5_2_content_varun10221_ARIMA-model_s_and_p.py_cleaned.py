import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set_style('darkgrid')
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1 = b1.sort_values(by='Date')
    b1.set_index('Date', b2 = True)
    return b1
def fonk2(b1):
    b1['First Difference'] = b1['Close'].diff()
    b1['Natural Log'] = np.log(b1['Close'])
    b1['Original Variance'] = b1['Close'].rolling(b3 = 30, min_periods=1, center=True).var()
    b1['Log Variance'] = b1['Natural Log'].rolling(b3 = 30, min_periods=1, center=True).var()
    b1['Logged First Difference'] = b1['Natural Log'].diff()
    b1['Lag 20'] = b1['Logged First Difference'].shift(20)
    return b1
def fonk3(data):
    b4 = sm.tsa.acf(data.iloc[1:])
    b5 = sm.tsa.pacf(data.iloc[1:])
    return b4, b5
def fonk4(data, b6 = 30):
    b7 = sm.tsa.seasonal.seasonal_decompose(data, b9='additive', period=b6)
    return b7
def fonk5(data, b8 = (0, 0, 1)):
    b9 = sm.tsa.ARIMA(data.iloc[1:], b8=b8)
    b10 = b9.fit(disp=-1)
    return b10
def fonk6(actual, forecasted):
    plt.figure(b11 = (16, 12))
    plt.plot(actual, b12 = 'Actual')
    plt.plot(forecasted, b12 = 'Forecast')
    plt.legend()
    plt.show()
def fonk7():
    b13 = os.path.join(os.getcwd(), 'q_table.csv')
    b1 = fonk1(b13)
    b1 = fonk2(b1)
    b4, b5 = fonk3(b1['Logged First Difference'])
    b7 = fonk4(b1['Natural Log'])
    b14 = fonk5(b1['Logged First Difference'])
    b1['Forecast'] = b14.fittedvalues
    fonk6(b1['Logged First Difference'], b1['Forecast'])
if b15 = = "__main__":
    fonk7()