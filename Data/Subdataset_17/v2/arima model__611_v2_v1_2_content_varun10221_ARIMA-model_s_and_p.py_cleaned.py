import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
sb.set_style('darkgrid')
file_path = os.path.join(os.getcwd(), 'q_table.csv')
stock_data = pd.read_csv(file_path)
stock_data['Date'] = pd.to_datetime(stock_data['Date'])
stock_data.sort_values(by='Date', ascending=True, inplace=True)
stock_data.set_index('Date', inplace=True)
stock_data['First Difference'] = stock_data['Close'].diff()
stock_data['Natural Log'] = stock_data['Close'].apply(np.log)
stock_data['Original Variance'] = stock_data['Close'].rolling(window=30).var()
stock_data['Log Variance'] = stock_data['Natural Log'].rolling(window=30).var()
stock_data['Logged First Difference'] = stock_data['Natural Log'].diff()
stock_data['Lag 20'] = stock_data['Logged First Difference'].shift(20)
lag_corr = acf(stock_data['Logged First Difference'].dropna())
lag_partial_corr = pacf(stock_data['Logged First Difference'].dropna())
decomposition = seasonal_decompose(stock_data['Natural Log'].dropna(), model='additive', period=30)
model = sm.tsa.ARIMA(stock_data['Logged First Difference'].dropna(), order=(0, 0, 1))
results = model.fit(disp=-1)
stock_data['Forecast'] = results.fittedvalues
plt.figure(figsize=(16, 12))
plt.plot(stock_data['Logged First Difference'], label='Logged First Difference')
plt.plot(stock_data['Forecast'], label='Forecast', color='red')
plt.title('Logged First Difference and Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()