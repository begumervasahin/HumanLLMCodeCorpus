
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.b3 import ARIMA
b1 = pd.read_csv("b1 Weekly 2000-2017.csv")
print("First 5 rows of the b1 DataFrame:")
print(b1.head(b2 = 5))
b3 = ARIMA(b1, order=(0, 1, 0))
b4 = b3.fit()
b5 = b4.forecast()[0]
print("First 5 rows of the ARIMA b3 summary:")
print(b4.summary().tables[1])