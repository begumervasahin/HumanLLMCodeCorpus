import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sb
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
sb.set_style('darkgrid')
b1 = os.path.join(os.getcwd(), 'q_table.csv')
b2 = pd.read_csv(b1)
b2['Date'] = pd.to_datetime(b2['Date'])
b2.sort_values(b3 = 'Date', b4=True)
b2.set_index('Date', b4 = True)
b2['First Difference'] = b2['Close'].diff()
b2['Natural Log'] = np.log(b2['Close'])
b2['Original Variance'] = b2['Close'].rolling(b5 = 30, center=True).var()
b2['Log Variance'] = b2['Natural Log'].rolling(b5 = 30, center=True).var()
b2['Logged First Difference'] = b2['Natural Log'].diff()
b2['Lag 20'] = b2['Logged First Difference'].shift(20)
b6 = b2['Logged First Difference'].dropna()
b7 = acf(b6)
b8 = pacf(b6)
b9 = seasonal_decompose(b2['Natural Log'], model='additive', period=30)
b10 = (0, 0, 1)
b11 = sm.tsa.ARIMA(b6, order=b10)
b12 = b11.fit(disp=-1)
b2['Forecast'] = b12.fittedvalues
plt.figure(b13 = (16, 12))
b2[['Logged First Difference', 'Forecast']].plot()
plt.title('Logged First Difference and ARIMA Forecast')
plt.show()