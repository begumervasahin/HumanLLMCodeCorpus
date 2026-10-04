
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
SPX = pd.read_csv("SPX Weekly 2000-2017.csv")
print("First 5 rows of the SPX DataFrame:")
print(SPX.head(n=5))
arima_order = (0, 1, 0)
arima_model = ARIMA(SPX, order=arima_order)
fitted_model = arima_model.fit()
forecasted_value = fitted_model.forecast()[0]
print("Forecasted next data point:", forecasted_value)
print("First 5 rows of the ARIMA model summary:")
print(fitted_model.summary().tables[1].as_html())