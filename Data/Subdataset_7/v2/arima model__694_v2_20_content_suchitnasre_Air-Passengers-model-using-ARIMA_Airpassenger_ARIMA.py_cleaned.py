import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import itertools
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from pyramid.arima import auto_arima
from statsmodels.tsa.stattools import adfuller
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
    plt.legend(b7 = 'best')
    plt.title("Original, Rolling Mean, and Standard Deviation")
    plt.show()
    print("Results of Dickey-Fuller Test:")
    b8 = adfuller(timeseries, autolag='AIC')
    b9 = pd.Series(b8[0:4], index=['Test Statistic', 'P-value', '
    for key, value in b8[4].items():
        b9['Critical Value (%s)' % key] = value
    print(b9)
    if b8[1] < 0.05:
        print("We reject the null hypothesis.")
        print("Data is stationary.")
    else:
        print("We fail to reject the null hypothesis.")
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
                              b15 = True, suppress_warnings=True, stepwise=True, information_criterion="aic",
                              b16 = "ignore")
b13.summary()
b17 = b3.b7["1949-01-01":"1958-12-31"]
b18 = b3.b7["1959-01-01":]
b13.fit(b17)
b19 = b13.predict(n_periods=24)
b20 = ((b19 - b18) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(b20, 2)))
b19 = pd.DataFrame(b19, index=b18.index, columns=["Predictions"])
pd.concat([b18, b19], b21 = 1).plot()
plt.show()
b22 = d = q = range(0, 3)
b23 = list(itertools.product(b22, d, q))
b24 = [(x[0], x[1], x[2], 12) for x in list(itertools.product(b22, d, q))]
warnings.filterwarnings("ignore")
b25 = [0, 0, 10000000]
for param in b23:
    for param_seasonal in b24:
        try:
            b26 = sm.tsa.statespace.SARIMAX(b3, order=param, b30=param_seasonal,
                                                      b27 = False, b31=False)
            b28 = b26.fit()
            print('ARIMA{} x {} - AIC: {}'.format(param, param_seasonal, b28.aic))
            if b28.aic < b25[2]:
                b25 = [param, param_seasonal, b28.aic]
        except:
            continue
print('\nBest Result:', b25)
b29 = sm.tsa.statespace.SARIMAX(b3, order=(b25[0][0], b25[0][1], b25[0][2]),
                                                b30 = (b25[1][0], b25[1][1], b25[1][2],
                                                                b25[1][3]), b27 = False,
                                                b31 = False)
b32 = b29.fit()
b33 = b32.predict(start=b18.index[0], end=b18.index[-1], dynamic=True)
b20 = ((b33 - b18) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(b20, 2)))
b33 = pd.DataFrame(b33, index=b18.index, columns=["Predictions"])
pd.concat([b18, b33], b21 = 1).plot()
plt.show()