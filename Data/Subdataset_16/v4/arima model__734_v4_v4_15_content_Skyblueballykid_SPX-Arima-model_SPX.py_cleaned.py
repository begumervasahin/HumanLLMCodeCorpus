
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
b1 = pd.read_csv("b1 Weekly 2000-2017.csv")
print("First 5 rows of the b1 DataFrame:")
print(b1.head(b2 = 5))
b3 = (0, 1, 0)
b4 = ARIMA(b1, order=b3)
b5 = b4.fit()
b6 = b5.forecast()[0]
print("Forecasted next data point:", b6)
print("First 5 rows of the ARIMA model summary:")
print(b5.summary().tables[1].as_html())