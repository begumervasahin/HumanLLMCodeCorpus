import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import statsmodels.api as sm
import seaborn as sb
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
sb.set_style('darkgrid')
b1 = os.getcwd() + '/q_table.csv'
b2 = pd.read_csv(b1)
b2['Date'] = pd.to_datetime(b2['Date'])
b2 = b2.sort_values(by='Date', ascending=True)
b2 = b2.set_index('Date')
b2['First Difference'] = b2['Close'] - b2['Close'].shift()
b2['Natural Log'] = b2['Close'].apply(lambda x: np.log(x))
b2['Original Variance'] = b2['Close'].rolling(b3 = 30, center=True).var()
b2['Log Variance'] = b2['Natural Log'].rolling(b3 = 30, center=True).var()
b2['Logged First Difference'] = b2['Natural Log'] - b2['Natural Log'].shift(1)
b2['Lag 20'] = b2['Logged First Difference'].shift(20)
b4 = acf(b2['Logged First Difference'].iloc[1:])
b5 = pacf(b2['Logged First Difference'].iloc[1:])
b6 = seasonal_decompose(b2['Natural Log'], b7='additive', period=30)
b7 = sm.tsa.ARIMA(b2['Logged First Difference'].iloc[1:], order=(0, 0, 1))
b8 = b7.fit(disp=-1)
b2['Forecast'] = b8.fittedvalues
plt.figure(b9 = (16, 12))
b2[['Logged First Difference', 'Forecast']].plot()
pylab.show()