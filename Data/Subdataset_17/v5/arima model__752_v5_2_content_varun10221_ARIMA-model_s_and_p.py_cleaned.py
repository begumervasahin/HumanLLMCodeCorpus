import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sb
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
sb.set_style('darkgrid')
def load_stock_data(file_path):
    stock_data = pd.read_csv(file_path)
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data = stock_data.sort_values(by='Date').set_index('Date')
    return stock_data
def calculate_stock_statistics(stock_data):
    stock_data['First Difference'] = stock_data['Close'] - stock_data['Close'].shift()
    stock_data['Natural Log'] = np.log(stock_data['Close'])
    stock_data['Original Variance'] = stock_data['Close'].rolling(window=30, center=True).var()
    stock_data['Log Variance'] = stock_data['Natural Log'].rolling(window=30, center=True).var()
    stock_data['Logged First Difference'] = stock_data['Natural Log'].diff()
    stock_data['Lag 20'] = stock_data['Logged First Difference'].shift(20)
    return stock_data
def calculate_acf_pacf(logged_diff):
    lag_corr = acf(logged_diff.dropna())
    lag_partial_corr = pacf(logged_diff.dropna())
    return lag_corr, lag_partial_corr
def perform_seasonal_decomposition(series, period=30):
    decomposition = seasonal_decompose(series, model='additive', period=period)
    return decomposition
def fit_arima_model(logged_diff):
    model = sm.tsa.ARIMA(logged_diff.dropna(), order=(0, 0, 1))
    results = model.fit(disp=-1)
    return results
def plot_forecast(stock_data):
    plt.figure(figsize=(16, 12))
    stock_data[['Logged First Difference', 'Forecast']].plot()
    plt.show()
def main():
    path = os.path.join(os.getcwd(), 'q_table.csv')
    stock_data = load_stock_data(path)
    stock_data = calculate_stock_statistics(stock_data)
    lag_corr, lag_partial_corr = calculate_acf_pacf(stock_data['Logged First Difference'])
    decomposition = perform_seasonal_decomposition(stock_data['Natural Log'])
    results = fit_arima_model(stock_data['Logged First Difference'])
    stock_data['Forecast'] = results.fittedvalues
    plot_forecast(stock_data)
if __name__ == "__main__":
    main()