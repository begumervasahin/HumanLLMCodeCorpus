
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
SPX = pd.read_csv("SPX Weekly 2000-2017.csv")
print("First 5 rows of the SPX dataset:")
print(SPX.head(n=5))
p, d, q = 0, 1, 0
model = ARIMA(SPX['Close'], order=(p, d, q))
model_fit = model.fit()
forecasted_value = model_fit.forecast()[0]
print("Forecasted value:", forecasted_value)
print("\nARIMA Model Summary:")
print(model_fit.summary())