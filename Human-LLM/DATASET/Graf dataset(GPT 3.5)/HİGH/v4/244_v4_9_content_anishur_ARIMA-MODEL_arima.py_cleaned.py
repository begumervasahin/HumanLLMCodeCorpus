
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
b1 = 'C:/Users/PATH/DataSet/Milano_WeatherPhenomena/mi_meteo_2001.csv'
b2 = pd.read_csv(b1, names=['id', 'Day', 'value'])
b2['Day'] = pd.to_datetime(b2['Day'], b3 = True)
b4 = b2.set_index(['Day'])
b5 = b4['value'].resample('D').mean()
plt.figure(b6 = (10, 6))
plt.plot(b5, b7 = 'Temperature')
plt.xlabel('Date')
plt.ylabel('Degree in Celsius')
plt.title('Daily Average Temperature')
plt.legend()
plt.show()
def fonk1(timeseries, b8 = 12):
    b9 = timeseries.rolling(b8=b8).mean()
    b10 = timeseries.rolling(b8=b8).std()
    plt.figure(b6 = (10, 6))
    plt.plot(timeseries, b11 = 'blue', b7='Original')
    plt.plot(b9, b11 = 'red', b7='Rolling Mean')
    plt.plot(b10, b11 = 'black', b7='Rolling Std')
    plt.legend(b12 = 'best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
def fonk2(timeseries):
    print('Results of Dickey-Fuller Test:')
    b13 = adfuller(timeseries.dropna(), autolag='AIC')
    b14 = pd.Series(b13[0:4], index=['Test Statistic', 'p-value', '
    for key, value in b13[4].items():
        b14[f'Critical Value ({key})'] = value
    print(b14)
fonk1(b5)
fonk2(b5)
