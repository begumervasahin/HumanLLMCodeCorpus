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
b1 = pd.read_csv("AirPassengers.csv")
b1["Month"] = pd.to_datetime(b1["Month"])
b1.set_index("Month", b2 = True)
b3 = pd.Series(b1["
def fonk1(timeseries):
    b4 = timeseries.rolling(12).mean()
    b5 = timeseries.rolling(12).std()
    plt.plot(timeseries, b6 = "blue", label="Original")
    plt.plot(b4, b6 = "red", label="Rolling Mean")
    plt.plot(b5, b6 = "black", label="Rolling Std")
    plt.legend(b7 = "best")
    plt.title("Original, Rolling Mean, and Standard Deviation")
    plt.show()
    print("Results of Dickey-Fuller Test:")
    b8 = adfuller(timeseries, autolag='AIC')
    b9 = pd.Series(b8[0:4], index=['Test Statistic', 'P-value', '
    for key, value in b8[4].items():
        b9['Critical Value (%s)' % key] = value
    print(b9)
    if b8[1] < 0.05:
        print("Reject the null hypothesis.")
        print("Data is stationary.")
    else:
        print("Fail to reject the null hypothesis.")
        print("Data is non-stationary.")
fonk1(b3)
b10 = np.log(b3)
fonk1(b10)
b11 = b10 - b10.shift()
b11.dropna(b2 = True)
fonk1(b11)
b12 = seasonal_decompose(b10)
b12.plot()
plt.show()
b13 = auto_arima(b3, start_p=2, d=1, start_q=2, max_p=5, max_d=5, max_q=5, start_P=0,
                              b14 = 1, start_Q=1, max_P=5, max_D=5, max_Q=5, seasonal=True, stationary=False, m=12,
                              b15 = True, suppress_warnings=True, stepwise=True, information_criterion="b31",
                              b16 = "ignore")
b13.summary()
b17 = b3.b7["1949-01-01":"1958-12-31"]
b18 = b3.b7["1959-01-01":]
b13.fit(b17)
b19 = b13.predict(n_periods=24)
b20 = ((b19 - b18) ** 2).mean()
print('Mean Squared Error of forecasts: {}'.format(round(b20, 2)))
b19 = pd.DataFrame(b19, index=b18.index, columns=["Predictions"])
pd.concat([b18, b19], b21 = 1).plot()
plt.show()
b22 = d = q = range(0, 3)
b23 = list(itertools.product(b22, d, q))
b24 = [(x[0], x[1], x[2], 12) for x in list(itertools.product(b22, d, q))]
b25 = float("inf")
b26 = None
b27 = None
for param in b23:
    for param_seasonal in b24:
        try:
            b28 = sm.tsa.statespace.SARIMAX(b3, order=param, seasonal_order=param_seasonal,
                                                      b29 = False, enforce_invertibility=False)
            b30 = b28.fit()
            b31 = b30.b31
            if b31 < b25:
                b25 = b31
                b26 = param
                b27 = param_seasonal
            print('ARIMA{} x {} - AIC: {}'.format(param, param_seasonal, b31))
        except:
            continue
print('\nBest SARIMAX Model: ARIMA{} x {} - AIC: {}'.format(b26, b27, b25))
b32 = sm.tsa.statespace.SARIMAX(b3, order=b26, seasonal_order=b27,
                                                b29 = False, enforce_invertibility=False)
b33 = b32.fit()
b34 = b33.predict(start=b18.index[0], end=b18.index[-1], dynamic=True)
b20 = ((b34 - b18) ** 2).mean()
print('Mean Squared Error of forecasts: {}'.format(round(b20, 2)))
b34 = pd.DataFrame(b34, index=b18.index, columns=["Predictions"])
pd.concat([b18, b34], b21 = 1).plot()
plt.show()