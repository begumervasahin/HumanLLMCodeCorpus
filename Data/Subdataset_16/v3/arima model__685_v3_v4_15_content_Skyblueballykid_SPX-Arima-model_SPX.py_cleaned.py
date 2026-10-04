import numpy as np
import pandas as pd
from statsmodels.tsa.arima.b2 import ARIMA
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(dataframe, b1 = 5):
    print(f"First {b1} b3 of the DataFrame:")
    print(dataframe.head(b1))
def fonk3(data, order):
    b2 = ARIMA(data, order=order)
    return b2.fit()
def fonk4(fitted_model):
    return fitted_model.forecast()[0]
def fonk5(fitted_model, b3 = 5):
    print(f"First {b3} b3 of the ARIMA b2 summary:")
    print(fitted_model.summary().tables[1].as_html())
def fonk6():
    b4 = "SPX Weekly 2000-2017.csv"
    b5 = fonk1(b4)
    fonk2(b5)
    b6 = (0, 1, 0)
    b7 = fonk3(b5, b6)
    b8 = fonk4(b7)
    print("Forecasted value:", b8)
    fonk5(b7)
if b9 = = "__main__":
    fonk6()