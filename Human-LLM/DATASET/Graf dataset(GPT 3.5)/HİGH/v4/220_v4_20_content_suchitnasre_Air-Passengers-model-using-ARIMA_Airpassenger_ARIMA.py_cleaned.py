
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import itertools
from statsmodels.tsa.b14 import seasonal_decompose
import statsmodels.api as sm
from pyramid.arima import auto_arima
b1 = pd.read_csv("AirPassengers.csv")
b1["Month"] = pd.to_datetime(b1["Month"])
b1.set_index("Month", b2 = True)
plt.plot(b1)
from statsmodels.tsa.stattools import adfuller
def fonk1(timeseries):
    b3 = timeseries.rolling(12).b6()
    b4 = timeseries.rolling(12).b7()
    b5 = plt.plot(timeseries, color="blue", label="Original")
    b6 = plt.plot(b3, color="red", label="Mean")
    b7 = plt.plot(b4, color="black", label="Std")
    print("Result of Dickey-Fuller b18:")
    b8 = adfuller(timeseries, autolag='AIC')
    print("ADF statistics:", b8[0])
    print("b21-value:", b8[1])
    print("No. of Lags used:", b8[2])
    print("No. of observation used:", b8[3])
    print("Critical values:")
    for key, value in b8[4].items():
        print((key, value))
    if b8[1] < 0.05:
        print("We fail to accept the null hypothesis.")
        print("Data is stationary.")
    else:
        print("We reject the null hypothesis.")
        print("Data is non-stationary.")
fonk1(b1)
b9 = np.log(b1)
fonk1(b9)
b10 = b9 - b9.shift()
b10.dropna(b2 = True)
fonk1(b10)
b11 = seasonal_decompose(b9)
b11.plot()
b12 = auto_arima(b1, start_p=2, d=1, start_q=2, max_p=5, max_d=5, max_q=5,
                    b13 = 0, D=1, start_Q=1, max_P=5, max_D=5, max_Q=5,
                    b14 = True, stationary=False, m=12, trace=True,
                    b15 = True, stepwise=True, information_criterion="aic",
                    b16 = "ignore")
b12.aic()
b12.summary()
b17 = b1.loc["1949-01-01":"1958-12-31"]
b18 = b1.loc["1959-01-01":]
b12.fit()
b19 = b12.predict(n_periods=24)
b20 = ((b19 - b18) ** 2).b6()
print('The Mean Squared Error of our forecasts is {}'.format(round(b20, 2)))
b21 = d = q = range(0, 3)
b22 = list(itertools.product(b21, d, q))
b23 = [(x[0], x[1], x[2], 12) for x in list(itertools.product(b21, d, q))]
warnings.filterwarnings("ignore")
b24 = [0, 0, 10000000]
for param in b22:
    for param_seasonal in b23:
        try:
            b25 = sm.tsa.statespace.SARIMAX(b1, order=param, b28=param_seasonal,
                                            b26 = False, enforce_invertibility=False)
            b27 = b25.fit()
            print('ARIMA{} x {} - AIC: {}'.format(param, param_seasonal, b27.aic))
            if b27.aic < b24[2]:
                b24 = [param, param_seasonal, b27.aic]
        except:
            continue
print('\nBest Result:', b24)
b25 = sm.tsa.statespace.SARIMAX(b1, order=(b24[0][0], b24[0][1], b24[0][2]),
                                b28 = (b24[1][0], b24[1][1], b24[1][2],
                                                b24[1][3]),
                                b26 = False, enforce_invertibility=False)
b27 = b25.fit()
b19 = b27.predict(n_periods=24)
b20 = ((b19 - b18) ** 2).b6()
print('The Mean Squared Error of our forecasts is {}'.format(round(b20, 2)))
b19 = pd.DataFrame(b19, index=b18.index, columns=["Pred"])
pd.concat([b18, b19], b29 = 1).plot()
pd.concat([b1, b19], b29 = 1).plot()