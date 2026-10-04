import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
sb.set_style('darkgrid')
b1 = os.path.join(os.getcwd(), 'q_table.csv')
b2 = pd.read_csv(b1)
b2['Date'] = pd.to_datetime(b2['Date'])
b2.sort_values(b3 = 'Date', ascending=True, b4=True)
b2.set_index('Date', b4 = True)
b2['First Difference'] = b2['Close'].diff()
b2['Natural Log'] = b2['Close'].apply(np.log)
b2['Original Variance'] = b2['Close'].rolling(b5 = 30).var()
b2['Log Variance'] = b2['Natural Log'].rolling(b5 = 30).var()
b2['Logged First Difference'] = b2['Natural Log'].diff()
b2['Lag 20'] = b2['Logged First Difference'].shift(20)
b6 = acf(b2['Logged First Difference'].dropna())
b7 = pacf(b2['Logged First Difference'].dropna())
b8 = seasonal_decompose(b2['Natural Log'].dropna(), b9='additive', period=30)
b9 = sm.tsa.ARIMA(b2['Logged First Difference'].dropna(), order=(0, 0, 1))
b10 = b9.fit(disp=-1)
b2['Forecast'] = b10.fittedvalues
plt.figure(b11 = (16, 12))
plt.plot(b2['Logged First Difference'], b12 = 'Logged First Difference')
plt.plot(b2['Forecast'], b12 = 'Forecast', color='red')
plt.title('Logged First Difference and Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()