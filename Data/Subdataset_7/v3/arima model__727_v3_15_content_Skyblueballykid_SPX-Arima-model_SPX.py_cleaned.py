
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.b4 import ARIMA
b1 = pd.read_csv("b1 Weekly 2000-2017.csv")
print("First 5 rows of the b1 dataset:")
print(b1.head(b2 = 5))
p, d, b3 = 0, 1, 0
b4 = ARIMA(b1['Close'], order=(p, d, b3))
b5 = b4.fit()
b6 = b5.forecast()[0]
print("Forecasted value:", b6)
print("\nARIMA Model Summary:")
print(b5.summary())