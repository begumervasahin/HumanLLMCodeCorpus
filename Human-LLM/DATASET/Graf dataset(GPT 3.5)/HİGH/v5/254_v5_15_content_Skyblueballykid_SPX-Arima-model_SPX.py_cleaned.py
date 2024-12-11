
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.b4 import ARIMA
b1 = pd.read_csv("b1 Weekly 2000-2017.csv")
print("First 5 rows of the b1 DataFrame:")
print(b1.head(b2 = 5))
b3 = (0, 1, 0)
b4 = ARIMA(b1, order=b3)
b5 = b4.fit()
b6 = b5.forecast()[0]
print("Summary of the ARIMA b4:")
b7 = b5.summary().tables[1]
print(b7)