
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set_style('darkgrid')
b1 = os.getcwd() + '/q_table.csv'
b2 = pd.read_csv(b1)
b2['Date'] = pd.to_datetime(b2['Date'])
b2 = b2.sort_values(by='Date', ascending=True)
b2.set_index('Date', b3 = True)
b2['First Difference'] = b2['Close'] - b2['Close'].shift()
b2['Natural Log'] = b2['Close'].apply(lambda x: np.log(x))
b2['Original Variance'] = b2['Close'].rolling(b4 = 30).var()
b2['Log Variance'] = b2['Natural Log'].rolling(b4 = 30).var()
b2['Logged First Difference'] = b2['Natural Log'] - b2['Natural Log'].shift(1)
b2['Lag 20'] = b2['Logged First Difference'].shift(20)
from statsmodels.tsa.stattools import acf, pacf
b5 = acf(b2['Logged First Difference'].iloc[1:])
b6 = pacf(b2['Logged First Difference'].iloc[1:])
from statsmodels.tsa.seasonal import seasonal_decompose
b7 = seasonal_decompose(b2['Natural Log'], b8='additive', freq=30)
b8 = sm.tsa.ARIMA(b2['Logged First Difference'].iloc[1:], order=(0, 0, 1))
b9 = b8.fit(disp=-1)
b2['Forecast'] = b9.fittedvalues
plt.figure(b10 = (16, 12))
plt.plot(b2['Logged First Difference'], b11 = 'Logged First Difference')
plt.plot(b2['Forecast'], b11 = 'Forecast')
plt.legend()
plt.show()