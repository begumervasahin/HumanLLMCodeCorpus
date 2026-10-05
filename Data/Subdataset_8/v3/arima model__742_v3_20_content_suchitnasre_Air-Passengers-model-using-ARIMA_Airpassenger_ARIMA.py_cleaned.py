import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import itertools
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from pyramid.arima import auto_arima
import statsmodels.api as sm
warnings.filterwarnings("ignore")
data = pd.read_csv("AirPassengers.csv")
data["Month"] = pd.to_datetime(data["Month"])
data.set_index("Month", inplace=True)
passenger_data = pd.Series(data["
def adf_test(timeseries):
    rolling_mean = timeseries.rolling(12).mean()
    rolling_std = timeseries.rolling(12).std()
    plt.plot(timeseries, color="blue", label="Original")
    plt.plot(rolling_mean, color="red", label="Rolling Mean")
    plt.plot(rolling_std, color="black", label="Rolling Std")
    plt.legend(loc="best")
    plt.title("Original, Rolling Mean, and Standard Deviation")
    plt.show()
    print("Results of Dickey-Fuller Test:")
    adf_result = adfuller(timeseries, autolag='AIC')
    adf_output = pd.Series(adf_result[0:4], index=['Test Statistic', 'P-value', '
    for key, value in adf_result[4].items():
        adf_output['Critical Value (%s)' % key] = value
    print(adf_output)
    if adf_result[1] < 0.05:
        print("Reject the null hypothesis.")
        print("Data is stationary.")
    else:
        print("Fail to reject the null hypothesis.")
        print("Data is non-stationary.")
adf_test(passenger_data)
passenger_data_log = np.log(passenger_data)
adf_test(passenger_data_log)
passenger_data_diff = passenger_data_log - passenger_data_log.shift()
passenger_data_diff.dropna(inplace=True)
adf_test(passenger_data_diff)
decomposition = seasonal_decompose(passenger_data_log)
decomposition.plot()
plt.show()
auto_arima_model = auto_arima(passenger_data, start_p=2, d=1, start_q=2, max_p=5, max_d=5, max_q=5, start_P=0,
                              D=1, start_Q=1, max_P=5, max_D=5, max_Q=5, seasonal=True, stationary=False, m=12,
                              trace=True, suppress_warnings=True, stepwise=True, information_criterion="aic",
                              error_action="ignore")
auto_arima_model.summary()
train_data = passenger_data.loc["1949-01-01":"1958-12-31"]
test_data = passenger_data.loc["1959-01-01":]
auto_arima_model.fit(train_data)
predictions = auto_arima_model.predict(n_periods=24)
mse = ((predictions - test_data) ** 2).mean()
print('Mean Squared Error of forecasts: {}'.format(round(mse, 2)))
predictions = pd.DataFrame(predictions, index=test_data.index, columns=["Predictions"])
pd.concat([test_data, predictions], axis=1).plot()
plt.show()
p = d = q = range(0, 3)
Non_seasonal_pdq = list(itertools.product(p, d, q))
Seasonal_PDQ = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
best_aic = float("inf")
best_param = None
best_seasonal_param = None
for param in Non_seasonal_pdq:
    for param_seasonal in Seasonal_PDQ:
        try:
            sarimax_model = sm.tsa.statespace.SARIMAX(passenger_data, order=param, seasonal_order=param_seasonal,
                                                      enforce_stationarity=False, enforce_invertibility=False)
            sarimax_results = sarimax_model.fit()
            aic = sarimax_results.aic
            if aic < best_aic:
                best_aic = aic
                best_param = param
                best_seasonal_param = param_seasonal
            print('ARIMA{} x {} - AIC: {}'.format(param, param_seasonal, aic))
        except:
            continue
print('\nBest SARIMAX Model: ARIMA{} x {} - AIC: {}'.format(best_param, best_seasonal_param, best_aic))
best_sarimax_model = sm.tsa.statespace.SARIMAX(passenger_data, order=best_param, seasonal_order=best_seasonal_param,
                                                enforce_stationarity=False, enforce_invertibility=False)
best_sarimax_results = best_sarimax_model.fit()
best_predictions = best_sarimax_results.predict(start=test_data.index[0], end=test_data.index[-1], dynamic=True)
mse = ((best_predictions - test_data) ** 2).mean()
print('Mean Squared Error of forecasts: {}'.format(round(mse, 2)))
best_predictions = pd.DataFrame(best_predictions, index=test_data.index, columns=["Predictions"])
pd.concat([test_data, best_predictions], axis=1).plot()
plt.show()