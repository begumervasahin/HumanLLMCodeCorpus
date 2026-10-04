
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.b2 import ARIMA
def fonk1(b3):
    return pd.read_csv(b3)
def fonk2(df, b1 = 5):
    print(f"First {b1} rows of the DataFrame:")
    print(df.head(b1))
def fonk3(df, order):
    b2 = ARIMA(df, order=order)
    return b2.fit()
def fonk4(fitted_model):
    return fitted_model.forecast()[0]
def fonk5(fitted_model):
    print("ARIMA Model Summary:")
    print(fitted_model.summary().tables[1].as_html())
def fonk6():
    b3 = "SPX Weekly 2000-2017.csv"
    b4 = fonk1(b3)
    fonk2(b4)
    b5 = (0, 1, 0)
    b6 = fonk3(b4, b5)
    b7 = fonk4(b6)
    print("Forecasted next data point:", b7)
    fonk5(b6)
if b8 = = "__main__":
    fonk6()