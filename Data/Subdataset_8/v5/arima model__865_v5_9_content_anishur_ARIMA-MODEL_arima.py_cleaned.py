
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path, names=['id', 'Day', 'value'])
    df['Day'] = pd.to_datetime(df['Day'], infer_datetime_format=True)
    indexed_dataset = df.set_index(['Day'])
    daily_data = indexed_dataset['value'].resample('D').mean()
    return daily_data
file_path = 'C:/Users/PATH/DataSet/Milano_WeatherPhenomena/mi_meteo_2001.csv'
daily_data = load_and_preprocess_data(file_path)
def plot_daily_temperature(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data, label='Temperature')
    plt.xlabel('Date')
    plt.ylabel('Degree in Celsius')
    plt.title('Daily Average Temperature')
    plt.legend()
    plt.show()
plot_daily_temperature(daily_data)
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
