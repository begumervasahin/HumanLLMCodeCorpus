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
b1 = pd.Series(b1["
def fonk1(timeseries):
    b3 = timeseries.rolling(12).b6()
    b4 = timeseries.rolling(12).b7()
    b5 = plt.plot(timeseries, color="blue", label="original")
    b6 = plt.plot(b3, color="red", label="Mean")
    b7 = plt.plot(b4, color="black", label="Std")
    print("Result of Dickey-Fuller b22")
    b8 = adfuller(timeseries, autolag='AIC')
    print("ADF statistics:", b8[0])
    print("b26-value:", b8[1])
    print("No. of Lags used:", b8[2])
    print("No. of observation used:", b8[3])
    print("Critical values:")
    for key, value in b8[4].items():
        print((key, value))
    if b8[1] < 0.05:
        print("We fail to accept the null hypothesis")
        print("Data is stationary")
    else:
        print("We rejected the alternate hypothesis")
        print("Data is non-stationary")
fonk1(b1)
b9 = np.log(b1)
fonk1(b9)
b10 = b9.rolling(12).b6()
b11 = b9 - b10
b11.dropna(b2 = True)
fonk1(b11)
b12 = b9.ewm(span=12).b6()
b13 = b9 - b12
fonk1(b13)
b14 = b9 - b9.shift()
b14.dropna(b2 = True)
fonk1(b14)
b15 = b14 - b14.shift()
b15.dropna(b2 = True)
fonk1(b15)
b16 = seasonal_decompose(b9)
b16.plot()
b17 = auto_arima(b1, start_p=2, d=1, start_q=2, max_p=5, max_d=5, max_q=5, start_P=0,
                    b18 = 1, start_Q=1, max_P=5, max_D=5, max_Q=5, seasonal=True, stationary=False, m=12,
                    b19 = True, suppress_warnings=True, stepwise=True, information_criterion="aic",
                    b20 = "ignore")
b17.aic()
b17.summary()
b21 = b1.loc["1949-01-01":"1958-12-31"]
b22 = b1.loc["1959-01-01":]
b17.fit()
b23 = b17.predict(n_periods=24)
b24 = ((b23 - b22) ** 2).b6()
print('The Mean Squared Error of our forecasts is {}'.format(round(b24, 2)))
b23 = pd.DataFrame(b23, index=b22.index, columns=["Pred"])
b23.head()
b23.tail()
pd.concat([b22, b23], b25 = 1).plot()
b26 = d = q = range(0, 3)
b27 = list(itertools.product(b26, d, q))
b28 = [(x[0], x[1], x[2], 12) for x in list(itertools.product(b26, d, q))]
warnings.filterwarnings("ignore")
b29 = [0, 0, 10000000]
for param in b27:
    for param_seasonal in b28:
        try:
            b30 = sm.tsa.statespace.SARIMAX(b1, order=param, b33=param_seasonal,
                                            b31 = False, b34=False)
            b32 = b30.fit()
            print('ARIMA{} x {} - AIC: {}'.format(param, param_seasonal, b32.aic))
            if b32.aic < b29[2]:
                b29 = [param, param_seasonal, b32.aic]
        except:
            continue
print('\nBest Result:', b29)
b30 = sm.tsa.statespace.SARIMAX(b1, order=(b29[0][0], b29[0][1], b29[0][1]),
                                b33 = (b29[1][0], b29[1][1], b29[1][2],
                                                b29[1][3]), b31 = False,
                                b34 = False)
b32 = b30.fit()
b23 = b32.predict(n_periods=24)
b24 = ((b23 - b22) ** 2).b6()
print('The Mean Squared Error of our forecasts is {}'.format(round(b24, 2)))
b23 = pd.DataFrame(b23, index=b22.index, columns=["Pred"])
b23.head()
b23.tail()
pd.concat([b22, b23], b25 = 1).plot()
plt.show()