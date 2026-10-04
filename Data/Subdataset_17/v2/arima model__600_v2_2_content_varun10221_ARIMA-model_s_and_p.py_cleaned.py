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
data_path = os.path.join(os.getcwd(), 'q_table.csv')
stock_data = pd.read_csv(data_path)
stock_data['Date'] = pd.to_datetime(stock_data['Date'])
stock_data = stock_data.sort_values(by='Date').set_index('Date')
stock_data['First Difference'] = stock_data['Close'] - stock_data['Close'].shift()
stock_data['Natural Log'] = stock_data['Close'].apply(np.log)
stock_data['Original Variance'] = stock_data['Close'].rolling(window=30, center=True).var()
stock_data['Log Variance'] = stock_data['Natural Log'].rolling(window=30, center=True).var()
stock_data['Logged First Difference'] = stock_data['Natural Log'] - stock_data['Natural Log'].shift()
stock_data['Lag 20'] = stock_data['Logged First Difference'].shift(20)
lag_corr = acf(stock_data['Logged First Difference'].iloc[1:])
lag_partial_corr = pacf(stock_data['Logged First Difference'].iloc[1:])
decomposition = seasonal_decompose(stock_data['Natural Log'], model='additive', period=30)
arima_model = sm.tsa.ARIMA(stock_data['Logged First Difference'].iloc[1:], order=(0, 0, 1))
arima_results = arima_model.fit(disp=-1)
stock_data['Forecast'] = arima_results.fittedvalues
plt.figure(figsize=(16, 12))
stock_data[['Logged First Difference', 'Forecast']].plot()
plt.title('Logged First Difference and ARIMA Forecast')
plt.show()