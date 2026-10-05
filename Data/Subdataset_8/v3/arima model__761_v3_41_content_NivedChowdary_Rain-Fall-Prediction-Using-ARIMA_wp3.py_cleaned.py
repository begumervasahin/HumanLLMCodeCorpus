import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
def read_and_preprocess_data(file_path):
    dataset = pd.read_csv(file_path, parse_dates=['YEAR'])
    dataset['YEAR'] = pd.date_range(start='1901', end='2017', freq='AS')
    indexedDataset = dataset.set_index(['YEAR'])
    return indexedDataset
def plot_rolling_statistics(data):
    rolmean = data.rolling(window=1).mean()
    rolstd = data.rolling(window=1).std()
    plt.plot(data, color='blue', label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling mean vs Standard deviation')
    plt.show(block=False)
def perform_dickey_fuller_test(data):
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(data['ANNUAL'], autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistics', 'p-value'])
    for key, value in dftest[4].items():
        dfoutput['Critical value (%s)' % key] = value
    print(dfoutput)
def plot_data_and_transformations(data):
    plt.xlabel("Date")
    plt.ylabel("Rainfall")
    plt.plot(data)
    indexedDataset_logScale = np.log(data)
    plt.plot(indexedDataset_logScale)
    return indexedDataset_logScale
def decompose_data(data):
    decomposition = seasonal_decompose(data)
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    plt.subplot(411)
    plt.plot(data, label='Original')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend, label='Trend')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal, label='Seasonality')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual, label='Residual')
    plt.legend(loc='best')
    plt.tight_layout()
    return residual.dropna()
def plot_acf_pacf(data):
    lag_acf = acf(data, nlags=20)
    lag_pacf = pacf(data, nlags=20, method='ols')
    plt.subplot(121)
    plt.plot(lag_acf)
    plt.axhline(y=0, linestyle='--', color='gray')
    plt.axhline(y=-1.96 / np.sqrt(len(data)), linestyle='--', color='gray')
    plt.axhline(y=1.96 / np.sqrt(len(data)), linestyle='--', color='gray')
    plt.title('Autocorrelation Function')
    plt.subplot(122)
    plt.plot(lag_pacf)
    plt.axhline(y=0, linestyle='--', color='gray')
    plt.axhline(y=-1.96 / np.sqrt(len(data)), linestyle='--', color='gray')
    plt.axhline(y=1.96 / np.sqrt(len(data)), linestyle='--', color='gray')
    plt.title('Partial Autocorrelation Function')
    plt.tight_layout()
def fit_arima_model(data):
    model = ARIMA(data, order=(1, 1, 1))
    results_ARIMA = model.fit(disp=-1)
    plt.plot(data)
    plt.plot(results_ARIMA.fittedvalues, color='red')
    plt.title('RSS: %.4f' % sum((results_ARIMA.fittedvalues - data['ANNUAL']) ** 2))
    return results_ARIMA.forecast(steps=90)
def main():
    indexedDataset = read_and_preprocess_data('annual.csv')
    plot_rolling_statistics(indexedDataset)
    perform_dickey_fuller_test(indexedDataset)
    indexedDataset_logScale = plot_data_and_transformations(indexedDataset)
    decomposed_data = decompose_data(indexedDataset_logScale)
    plot_acf_pacf(decomposed_data)
    forecast = fit_arima_model(decomposed_data)
    print("Forecast:", forecast)
if __name__ == "__main__":
    main()