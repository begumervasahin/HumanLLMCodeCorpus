import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set_style('darkgrid')
def load_and_preprocess_stock_data(file_path):
    stock_data = pd.read_csv(file_path)
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data = stock_data.sort_values(by='Date')
    stock_data.set_index('Date', inplace=True)
    return stock_data
def calculate_additional_features(stock_data):
    stock_data['First Difference'] = stock_data['Close'].diff()
    stock_data['Natural Log'] = np.log(stock_data['Close'])
    stock_data['Original Variance'] = stock_data['Close'].rolling(window=30, min_periods=1, center=True).var()
    stock_data['Log Variance'] = stock_data['Natural Log'].rolling(window=30, min_periods=1, center=True).var()
    stock_data['Logged First Difference'] = stock_data['Natural Log'].diff()
    stock_data['Lag 20'] = stock_data['Logged First Difference'].shift(20)
    return stock_data
def calculate_autocorrelations(data):
    lag_corr = sm.tsa.acf(data.iloc[1:])
    lag_partial_corr = sm.tsa.pacf(data.iloc[1:])
    return lag_corr, lag_partial_corr
def perform_seasonal_decomposition(data, frequency=30):
    decomposition = sm.tsa.seasonal.seasonal_decompose(data, model='additive', period=frequency)
    return decomposition
def fit_arima_model(data, order=(0, 0, 1)):
    model = sm.tsa.ARIMA(data.iloc[1:], order=order)
    results = model.fit(disp=-1)
    return results
def plot_forecasted_values(actual, forecasted):
    plt.figure(figsize=(16, 12))
    plt.plot(actual, label='Actual')
    plt.plot(forecasted, label='Forecast')
    plt.legend()
    plt.show()
def main():
    csv_file_path = os.path.join(os.getcwd(), 'q_table.csv')
    stock_data = load_and_preprocess_stock_data(csv_file_path)
    stock_data = calculate_additional_features(stock_data)
    lag_corr, lag_partial_corr = calculate_autocorrelations(stock_data['Logged First Difference'])
    decomposition = perform_seasonal_decomposition(stock_data['Natural Log'])
    arima_results = fit_arima_model(stock_data['Logged First Difference'])
    stock_data['Forecast'] = arima_results.fittedvalues
    plot_forecasted_values(stock_data['Logged First Difference'], stock_data['Forecast'])
if __name__ == "__main__":
    main()