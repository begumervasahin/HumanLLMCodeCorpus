
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
file_path = 'C:/Users/PATH/DataSet/Milano_WeatherPhenomena/mi_meteo_2001.csv'
df = pd.read_csv(file_path, names=['id', 'Day', 'value'])
df['Day'] = pd.to_datetime(df['Day'], infer_datetime_format=True)
indexedDataset = df.set_index(['Day'])
daily_data = indexedDataset['value'].resample('D').mean()
plt.figure(figsize=(10, 6))
plt.plot(daily_data, label='Temperature')
plt.xlabel('Date')
plt.ylabel('Degree in Celsius')
plt.title('Daily Average Temperature')
plt.legend()
plt.show()
def plot_rolling_statistics(timeseries, window=12):
    rolmean = timeseries.rolling(window=window).mean()
    rolstd = timeseries.rolling(window=window).std()
    plt.figure(figsize=(10, 6))
    plt.plot(timeseries, color='blue', label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
def perform_dickey_fuller_test(timeseries):
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries.dropna(), autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '
    for key, value in dftest[4].items():
        dfoutput[f'Critical Value ({key})'] = value
    print(dfoutput)
plot_rolling_statistics(daily_data)
perform_dickey_fuller_test(daily_data)
