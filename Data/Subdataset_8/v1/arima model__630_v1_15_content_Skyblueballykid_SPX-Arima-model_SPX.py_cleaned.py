import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
SPX = pd.read_csv("SPX Weekly 2000-2017.csv")
print(SPX.head(n=5))
model = ARIMA(SPX['Close'], order=(0, 1, 0))
model_fit = model.fit()
outcome = model_fit.forecast()[0]
print("Forecasted value:", outcome)
print(model_fit.summary())