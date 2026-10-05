
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
def fonk1(b5):
    b1 = pd.read_csv(b5, names=['id', 'Day', 'value'])
    b1['Day'] = pd.to_datetime(b1['Day'], b2 = True)
    b3 = b1.set_index(['Day'])
    b4 = b3['value'].resample('D').mean()
    return b4
b5 = 'C:/Users/PATH/DataSet/Milano_WeatherPhenomena/mi_meteo_2001.csv'
b4 = fonk1(b5)
def fonk2(data):
    plt.figure(b6 = (10, 6))
    plt.plot(data, b7 = 'Temperature')
    plt.xlabel('Date')
    plt.ylabel('Degree in Celsius')
    plt.title('Daily Average Temperature')
    plt.legend()
    plt.show()
fonk2(b4)
def fonk3(timeseries, b8 = 12):
    b9 = timeseries.rolling(b8=b8).mean()
    b10 = timeseries.rolling(b8=b8).std()
    plt.figure(b6 = (10, 6))
    plt.plot(timeseries, b11 = 'blue', b7='Original')
    plt.plot(b9, b11 = 'red', b7='Rolling Mean')
    plt.plot(b10, b11 = 'black', b7='Rolling Std')
    plt.legend(b12 = 'best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
def fonk4(timeseries):
    print('Results of Dickey-Fuller Test:')
    b13 = adfuller(timeseries.dropna(), autolag='AIC')
    b14 = pd.Series(b13[0:4], index=['Test Statistic', 'p-value', '
    for key, value in b13[4].items():
        b14[f'Critical Value ({key})'] = value
    print(b14)
fonk3(b4)
fonk4(b4)
