
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
SPX = pd.read_csv("SPX Weekly 2000-2017.csv")
print("First 5 rows of the SPX DataFrame:")
print(SPX.head(n=5))
arima_order = (0, 1, 0)
model = ARIMA(SPX, order=arima_order)
model_fit = model.fit()
forecasted_value = model_fit.forecast()[0]
print("Summary of the ARIMA model:")
model_summary = model_fit.summary().tables[1]
print(model_summary)