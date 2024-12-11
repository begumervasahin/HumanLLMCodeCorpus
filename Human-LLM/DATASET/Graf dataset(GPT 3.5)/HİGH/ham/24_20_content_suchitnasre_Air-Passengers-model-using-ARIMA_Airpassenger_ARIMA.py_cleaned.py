import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import itertools
from statsmodels.tsa.b19 import seasonal_decompose
import statsmodels.api as sm
from pyramid.arima import auto_arima
b1 = pd.read_csv("AirPassengers.csv")
b1["Month"] = pd.to_datetime(b1["Month"])
b1.head()
b1.set_index("Month",b2 = True)
b1 = pd.Series(b1["
plt.plot(b1)
from statsmodels.tsa.stattools import adfuller
def fonk1(timeseries):
    b3 = timeseries.rolling(12).b6()
    b4 = timeseries.rolling(12).b7()
    b5 = plt.plot(timeseries, color = "blue", b21 = "original")
    b6 = plt.plot(b3, color = "red", b21 = "Mean")
    b7 = plt.plot(b4, color = "black", b21 = "Std")
    print("Result of Dickey-Fyller b39")
    b8 = adfuller(timeseries,autolag='AIC')
    print("ADF statistics :", b8[0])
    print("b43-value :", b8[1])
    print("No. of Lags used :", b8[2])
    print("No. of observation used :", b8[3])
    print("Critical values :")
    for key, value in b8[4].items():
        print((key, value))
    if b8[1] <0.05:
        print("We fail to accept the null hypothesis")
        print("Data is b31")
    else:
        print("We rejected the alternate hypothesis")
        print("Data is non b31")
fonk1(b1)
b9 = np.log(b1)
fonk1(b9)
b10 = b9.rolling(12).b6()
b11 = b9-b10
b11.dropna(b2 = True)
fonk1(b11)
b12 = pd.Series.ewm
b13 = b12(b9, span=12).b6()
b14 = b9 - b13
b14.head()
fonk1(b14)
b15 = b9 - b9.shift()
b15.dropna(b2 = True)
fonk1(b15)
b16 = b15 - b15.shift()
b16.dropna(b2 = True)
fonk1(b16)
b17 = seasonal_decompose(b9)
b17.plot()
"""b18 = b17.b18
b19 = b17.b19
b20 = b17.resid
plt.subplot(411)
plt.plot(b9, b21 = "original")
plt.b23(b22 = "best")
plt.subplot(412)
plt.plot(b18, b21 = "b18")
plt.b23(b22 = "best")
plt.subplot(413)
plt.plot(b19, b21 = "b19")
plt.b23(b22 = "best")
plt.subplot(414)
plt.plot(b20, b23 = "Residual")
plt.b23(b22 = "best")
plt.tight_layout()
b20.dropna(b2 = True)
fonk1(b20)"""
b24 = auto_arima(b1, start_p=2,
                    b25 = 1, start_q=2,
                    b26 = 5, max_d = 5,
                    b27 = 5, start_P=0,
                    b28 = 1, start_Q=1,
                    b29 = 5, max_D=5,
                    b30 = 5, b19=True,
                    b31 = False,
                    b32 = 12,
                    b33 = True,
                    b34 = True,
                    b35 = True,
                    b36 = "aic",
                    b37 = "ignore"
                    )
b24.aic()
b24.summary()
b38 = b1.b22["1949-01-01":"1958-12-31"]
b39 = b1.b22["1959-01-01":]
b24.fit()
b40 = b24.predict(n_periods=24)
b41 = ((b40 - b39) ** 2).b6()
print('The Mean Squared Error of our forecasts is {}'.format(round(b41, 2)))
b40 = pd.DataFrame(b40, index = b39.index, columns = ["Pred"])
b40.head()
b40.tail()
pd.concat([b39, b40], b42 = 1).plot()
pd.concat([b1,b40], b42 = 1).plot()
b43 = b25=q = range(0,3)
b44 = list(itertools.product(b43, b25, q))
b45 = [(x[0], x[1], x[2], 12) for x in list(itertools.product(b43, b25, q))]
warnings.filterwarnings("ignore")
b46 = [0, 0, 10000000]
for param in b44:
    for param_seasonal in b45:
        try:
            b47 = sm.tsa.statespace.SARIMAX(b1,
                                            b48 = param,
                                            b49 = param_seasonal,
                                            b50 = False,
                                            b51 = False)
            b52 = b47.fit()
            print('ARIMA{} x {} - AIC: {}'.format(param, param_seasonal, b52.aic))
            if b52.aic < b46[2]:
                b46 = [param, param_seasonal, b52.aic]
        except:
            continue
print('\nBest Result:', b46)
b47 = sm.tsa.statespace.SARIMAX(b1,
                                b48 = (b46[0][0], b46[0][1], b46[0][1]),
                                b49 = (b46[1][0], b46[1][1], b46[1][2], b46[1][3]),
                                b50 = False,
                                b51 = False)
b52 = b47.fit()
b40 = b52.predict(n_periods=24)
b41 = ((b40 - b39) ** 2).b6()
print('The Mean Squared Error of our forecasts is {}'.format(round(b41, 2)))
b40 = pd.DataFrame(b40, index = b39.index, columns = ["Pred"])
b40.head()
b40.tail()
pd.concat([b39, b40], b42 = 1).plot()
pd.concat([b1,b40], b42 = 1).plot()