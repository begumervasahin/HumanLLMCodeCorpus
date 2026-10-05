
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import warnings
from statsmodels.tsa.b12 import seasonal_decompose
import statsmodels.api as sm
from pyramid.arima import auto_arima
from statsmodels.tsa.stattools import adfuller
b1 = pd.read_csv("AirPassengers.csv")
b1["Month"] = pd.to_datetime(b1["Month"])
b1.set_index("Month", b2 = True)
plt.plot(b1)
def fonk1(timeseries):
    b3 = timeseries.rolling(12).mean()
    b4 = timeseries.rolling(12).std()
    plt.plot(timeseries, b5 = "blue", label="Original")
    plt.plot(b3, b5 = "red", label="Mean")
    plt.plot(b4, b5 = "black", label="Std")
    print("Result of Dickey-Fuller b16:")
    b6 = adfuller(timeseries, autolag='AIC')
    print("ADF statistics:", b6[0])
    print("b19-value:", b6[1])
    print("No. of Lags used:", b6[2])
    print("No. of observation used:", b6[3])
    print("Critical values:")
    for key, value in b6[4].items():
        print((key, value))
    if b6[1] < 0.05:
        print("We fail to accept the null hypothesis.")
        print("Data is stationary.")
    else:
        print("We reject the null hypothesis.")
        print("Data is non-stationary.")
fonk1(b1)
b7 = np.log(b1)
fonk1(b7)
b8 = b7 - b7.shift()
b8.dropna(b2 = True)
fonk1(b8)
b9 = seasonal_decompose(b7)
b9.plot()
b10 = auto_arima(b1, start_p=2, d=1, start_q=2, max_p=5, max_d=5, max_q=5,
                    b11 = 0, D=1, start_Q=1, max_P=5, max_D=5, max_Q=5,
                    b12 = True, stationary=False, m=12, trace=True,
                    b13 = True, stepwise=True, information_criterion="aic",
                    b14 = "ignore")
b10.aic()
b10.summary()
b15 = b1.loc["1949-01-01":"1958-12-31"]
b16 = b1.loc["1959-01-01":]
b10.fit()
b17 = b10.predict(n_periods=24)
b18 = ((b17 - b16) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(b18, 2)))
b19 = d = q = range(0, 3)
b20 = list(itertools.product(b19, d, q))
b21 = [(x[0], x[1], x[2], 12) for x in list(itertools.product(b19, d, q))]
warnings.filterwarnings("ignore")
b22 = [0, 0, 10000000]
for param in b20:
    for param_seasonal in b21:
        try:
            b23 = sm.tsa.statespace.SARIMAX(b1, order=param, b26=param_seasonal,
                                            b24 = False, enforce_invertibility=False)
            b25 = b23.fit()
            print('ARIMA{} x {} - AIC: {}'.format(param, param_seasonal, b25.aic))
            if b25.aic < b22[2]:
                b22 = [param, param_seasonal, b25.aic]
        except:
            continue
print('\nBest Result:', b22)
b23 = sm.tsa.statespace.SARIMAX(b1, order=(b22[0][0], b22[0][1], b22[0][2]),
                                b26 = (b22[1][0], b22[1][1], b22[1][2],
                                                b22[1][3]),
                                b24 = False, enforce_invertibility=False)
b25 = b23.fit()
b17 = b25.predict(n_periods=24)
b18 = ((b17 - b16) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(b18, 2)))
b17 = pd.DataFrame(b17, index=b16.index, columns=["Pred"])
pd.concat([b16, b17], b27 = 1).plot()
pd.concat([b1, b17], b27 = 1).plot()