import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
def load_stock_data(csv_file_path: str) -> pd.DataFrame:
    stock_data = pd.read_csv(csv_file_path)
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data = stock_data.sort_values(by='Date')
    stock_data.set_index('Date', inplace=True)
    return stock_data
def preprocess_stock_data(stock_data: pd.DataFrame) -> pd.DataFrame:
    stock_data['First Difference'] = stock_data['Close'].diff()
    stock_data['Natural Log'] = np.log(stock_data['Close'])
    stock_data['Original Variance'] = stock_data['Close'].rolling(window=30, min_periods=1, center=True).var()
    stock_data['Log Variance'] = stock_data['Natural Log'].rolling(window=30, min_periods=1, center=True).var()
    stock_data['Logged First Difference'] = stock_data['Natural Log'].diff()
    stock_data['Lag 20'] = stock_data['Logged First Difference'].shift(20)
    return stock_data
def calculate_autocorrelation(stock_data: pd.DataFrame) -> (np.ndarray, np.ndarray):
    logged_diff = stock_data['Logged First Difference'].dropna()
    lag_corr = sm.tsa.acf(logged_diff)
    lag_partial_corr = sm.tsa.pacf(logged_diff)
    return lag_corr, lag_partial_corr
def perform_seasonal_decomposition(stock_data: pd.DataFrame):
    decomposition = sm.tsa.seasonal_decompose(stock_data['Natural Log'], model='additive', period=30)
    return decomposition
def fit_arima_model(stock_data: pd.DataFrame):
    logged_diff = stock_data['Logged First Difference'].dropna()
    model = sm.tsa.ARIMA(logged_diff, order=(0, 0, 1))
    results = model.fit(disp=-1)
    return results
def plot_forecast(stock_data: pd.DataFrame, results):
    stock_data['Forecast'] = results.fittedvalues
    plt.figure(figsize=(16, 12))
    plt.plot(stock_data['Logged First Difference'], label='Actual')
    plt.plot(stock_data['Forecast'], label='Forecast')
    plt.legend()
    plt.title('Actual vs Forecasted Values')
    plt.xlabel('Date')
    plt.ylabel('Logged First Difference')
    plt.show()
def main():
    sns.set_style('darkgrid')
    csv_file_path = os.path.join(os.getcwd(), 'q_table.csv')
    stock_data = load_stock_data(csv_file_path)
    stock_data = preprocess_stock_data(stock_data)
    lag_corr, lag_partial_corr = calculate_autocorrelation(stock_data)
    decomposition = perform_seasonal_decomposition(stock_data)
    results = fit_arima_model(stock_data)
    plot_forecast(stock_data, results)
if __name__ == "__main__":
    main()