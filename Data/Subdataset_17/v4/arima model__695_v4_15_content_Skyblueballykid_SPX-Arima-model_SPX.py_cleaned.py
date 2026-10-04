
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
SPX = pd.read_csv("SPX Weekly 2000-2017.csv")
print("First 5 rows of the SPX DataFrame:")
print(SPX.head(n=5))
model = ARIMA(SPX, order=(0, 1, 0))
model_fit = model.fit()
forecasted_value = model_fit.forecast()[0]
print("First 5 rows of the ARIMA model summary:")
print(model_fit.summary().tables[1])