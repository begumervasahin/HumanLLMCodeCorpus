import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set_style('darkgrid')
def main():
    stock_data = load_stock_data('q_table.csv')
    stock_data = calculate_additional_columns(stock_data)
    lag_corr, lag_partial_corr = calculate_autocorrelations(stock_data['Logged First Difference'].iloc[1:])
    decomposition = decompose_seasonal(stock_data['Natural Log'])
    stock_data = fit_arima_and_forecast(stock_data)
    plot_forecast(stock_data)
def load_stock_data(filename):
    path = os.path.join(os.getcwd(), filename)
    stock_data = pd.read_csv(path)
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data = stock_data.sort_values(by='Date', ascending=True).set_index('Date')
    return stock_data
def calculate_additional_columns(stock_data):
    stock_data['First Difference'] = stock_data['Close'] - stock_data['Close'].shift()
    stock_data['Natural Log'] = stock_data['Close'].apply(np.log)
    stock_data['Original Variance'] = stock_data['Close'].rolling(window=30, center=True).var()
    stock_data['Log Variance'] = stock_data['Natural Log'].rolling(window=30, center=True).var()
    stock_data['Logged First Difference'] = stock_data['Natural Log'] - stock_data['Natural Log'].shift(1)
    stock_data['Lag 20'] = stock_data['Logged First Difference'].shift(20)
    return stock_data
def calculate_autocorrelations(logged_diff):
    lag_corr = sm.tsa.acf(logged_diff)
    lag_partial_corr = sm.tsa.pacf(logged_diff)
    return lag_corr, lag_partial_corr
def decompose_seasonal(natural_log):
    decomposition = sm.tsa.seasonal_decompose(natural_log, model='additive', period=30)
    return decomposition
def fit_arima_and_forecast(stock_data):
    model = sm.tsa.ARIMA(stock_data['Logged First Difference'].iloc[1:], order=(0, 0, 1))
    results = model.fit(disp=-1)
    stock_data['Forecast'] = results.fittedvalues
    return stock_data
def plot_forecast(stock_data):
    plt.figure(figsize=(16, 12))
    plt.plot(stock_data['Logged First Difference'], label='Actual')
    plt.plot(stock_data['Forecast'], label='Forecast')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()