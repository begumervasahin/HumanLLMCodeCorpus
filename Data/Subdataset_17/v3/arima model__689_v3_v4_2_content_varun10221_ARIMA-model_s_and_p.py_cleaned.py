import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set_style('darkgrid')
def load_and_prepare_data(file_path):
    stock_data = pd.read_csv(file_path)
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data = stock_data.sort_values(by='Date', ascending=True)
    stock_data = stock_data.set_index('Date')
    return stock_data
def calculate_statistics(stock_data):
    stock_data['First Difference'] = stock_data['Close'] - stock_data['Close'].shift()
    stock_data['Natural Log'] = stock_data['Close'].apply(np.log)
    stock_data['Original Variance'] = stock_data['Close'].rolling(window=30, center=True).var()
    stock_data['Log Variance'] = stock_data['Natural Log'].rolling(window=30, center=True).var()
    stock_data['Logged First Difference'] = stock_data['Natural Log'] - stock_data['Natural Log'].shift(1)
    stock_data['Lag 20'] = stock_data['Logged First Difference'].shift(20)
    return stock_data
def calculate_autocorrelation(stock_data):
    logged_first_diff = stock_data['Logged First Difference'].dropna()
    autocorr = sm.tsa.acf(logged_first_diff)
    partial_autocorr = sm.tsa.pacf(logged_first_diff)
    return autocorr, partial_autocorr
def perform_seasonal_decomposition(stock_data):
    decomposition = sm.tsa.seasonal_decompose(stock_data['Natural Log'].dropna(), model='additive', period=30)
    return decomposition
def fit_arima_model(stock_data):
    logged_first_diff = stock_data['Logged First Difference'].dropna()
    model = sm.tsa.ARIMA(logged_first_diff, order=(0, 0, 1))
    results = model.fit(disp=-1)
    return results
def plot_forecast(stock_data, arima_results):
    stock_data['Forecast'] = arima_results.fittedvalues
    plt.figure(figsize=(16, 12))
    plt.plot(stock_data['Logged First Difference'], label='Actual')
    plt.plot(stock_data['Forecast'], label='Forecast')
    plt.legend()
    plt.title('Actual vs Forecasted Values')
    plt.xlabel('Date')
    plt.ylabel('Logged First Difference')
    plt.show()
def main():
    file_path = os.path.join(os.getcwd(), 'q_table.csv')
    stock_data = load_and_prepare_data(file_path)
    stock_data = calculate_statistics(stock_data)
    autocorr, partial_autocorr = calculate_autocorrelation(stock_data)
    decomposition = perform_seasonal_decomposition(stock_data)
    arima_results = fit_arima_model(stock_data)
    plot_forecast(stock_data, arima_results)
if __name__ == "__main__":
    main()