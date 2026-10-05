
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set_style('darkgrid')
file_path = os.getcwd() + '/q_table.csv'
stock_data = pd.read_csv(file_path)
stock_data['Date'] = pd.to_datetime(stock_data['Date'])
stock_data = stock_data.sort_values(by='Date', ascending=True)
stock_data.set_index('Date', inplace=True)
stock_data['First Difference'] = stock_data['Close'] - stock_data['Close'].shift()
stock_data['Natural Log'] = stock_data['Close'].apply(lambda x: np.log(x))
stock_data['Original Variance'] = stock_data['Close'].rolling(window=30).var()
stock_data['Log Variance'] = stock_data['Natural Log'].rolling(window=30).var()
stock_data['Logged First Difference'] = stock_data['Natural Log'] - stock_data['Natural Log'].shift(1)
stock_data['Lag 20'] = stock_data['Logged First Difference'].shift(20)
from statsmodels.tsa.stattools import acf, pacf
autocorrelation = acf(stock_data['Logged First Difference'].iloc[1:])
partial_autocorrelation = pacf(stock_data['Logged First Difference'].iloc[1:])
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(stock_data['Natural Log'], model='additive', freq=30)
model = sm.tsa.ARIMA(stock_data['Logged First Difference'].iloc[1:], order=(0, 0, 1))
results = model.fit(disp=-1)
stock_data['Forecast'] = results.fittedvalues
plt.figure(figsize=(16, 12))
plt.plot(stock_data['Logged First Difference'], label='Logged First Difference')
plt.plot(stock_data['Forecast'], label='Forecast')
plt.legend()
plt.show()