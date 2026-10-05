import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error
df = pd.read_csv('Shampoo-Sales.csv')
df = df.iloc[:-1, :]
df['Month'] = '190' + df['Month']
df['Month'] = pd.to_datetime(df['Month'], format='%Y-%m')
df.rename(columns={'Sales of shampoo over a three year period': 'Shampoo Sales'}, inplace=True)
series = df.set_index('Month')['Shampoo Sales']
plt.figure(figsize=(20, 10))
plt.title('Shampoo Sales over a 3-year period')
plt.xlabel('Month')
plt.ylabel('Shampoo Sales')
series.plot()
decomposition = seasonal_decompose(series, model='additive')
decomposition.plot()
plt.show()
def adf_check(time_series):
    adfuller_result = adfuller(time_series)
    print('Augmented Dickey-Fuller Test:')
    labels = ['ADF Test Statistic', 'p-value']
    for value, label in zip(adfuller_result, labels):
        print(label + ": " + str(value))
    return adfuller_result
def find_stationarity_and_difference(time_series):
    for i in range(10):
        if i == 0:
            print('Actual Time Series')
        else:
            print(str(i)+'-Differenced Time Series')
        print('-' * 60)
        p_stationarity = adf_check(time_series)[1]
        print("\nStationarity:")
        if p_stationarity <= 0.05:
            print('Data is Stationary')
            break
        else:
            print('Data is Non-Stationary\n')
            time_series = (time_series - time_series.shift(1))
            time_series.dropna(inplace=True)
    return i, time_series
d, stationary_series = find_stationarity_and_difference(series)
print('No. of times differenced = ', d)
stationary_series.plot()
fig_first_acf = plot_acf(stationary_series)
fig_first_acf.set_size_inches(20, 10)
fig_first_pacf = plot_pacf(stationary_series)
fig_first_pacf.set_size_inches(20, 10)
model = ARIMA(series, order=(4, 1, 2))
arima_results = model.fit()
print(arima_results.summary())
residuals = pd.DataFrame(arima_results.resid)
residuals.plot(figsize=(10, 10))
residuals.plot(kind='kde', figsize=(10, 10))
residuals.describe()
predictions = arima_results.forecast(steps=len(series))[0]
error = mean_squared_error(series, predictions)
print('Test MSE: %.3f' % error)
plt.plot(series, color='blue', label='Actuals')
plt.plot(predictions, color='red', label='Rolling forecast')
plt.legend()
plt.show()
aic = []
pdq = []
for p in range(6):
    for q in range(4):
        try:
            model = ARIMA(series, (p, 1, q)).fit()
            aic.append(model.aic)
            pdq.append((p, 1, q))
        except:
            pass
d = dict(zip(pdq, aic))
minaic = min(d, key=d.get)
p, d, q = minaic
print("Best Model is:", (p, d, q))
best_model = ARIMA(series, (p, d, q)).fit()
predictions = best_model.forecast(steps=len(series))[0]
error = mean_squared_error(series, predictions)
print('Test MSE: %.3f' % error)
plt.plot(series, color='blue', label='Actuals')
plt.plot(predictions, color='red', label='Rolling forecast')
plt.legend()
plt.show()
print('The model has the parameters: (p, d, q) = (5, 1, 0). It is an autoregressive model.')