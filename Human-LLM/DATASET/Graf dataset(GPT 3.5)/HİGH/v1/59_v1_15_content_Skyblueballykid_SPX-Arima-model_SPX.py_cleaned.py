import numpy as np
import pandas as pd
from statsmodels.tsa.arima.b3 import ARIMA
b1 = pd.read_csv("b1 Weekly 2000-2017.csv")
print(b1.head(b2 = 5))
b3 = ARIMA(b1['Close'], order=(0, 1, 0))
b4 = b3.fit()
b5 = b4.forecast()[0]
print("Forecasted value:", b5)
print(b4.summary())