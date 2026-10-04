
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
def read_csv_to_dataframe(file_path):
    return pd.read_csv(file_path)
def display_dataframe_head(df, n=5):
    print(f"First {n} rows of the DataFrame:")
    print(df.head(n))
def create_and_fit_arima_model(df, order):
    model = ARIMA(df, order=order)
    return model.fit()
def forecast_next_value(fitted_model):
    return fitted_model.forecast()[0]
def display_arima_model_summary(fitted_model):
    print("ARIMA Model Summary:")
    print(fitted_model.summary().tables[1].as_html())
def main():
    file_path = "SPX Weekly 2000-2017.csv"
    spx_data = read_csv_to_dataframe(file_path)
    display_dataframe_head(spx_data)
    arima_order = (0, 1, 0)
    fitted_arima_model = create_and_fit_arima_model(spx_data, arima_order)
    next_forecasted_value = forecast_next_value(fitted_arima_model)
    print("Forecasted next data point:", next_forecasted_value)
    display_arima_model_summary(fitted_arima_model)
if __name__ == "__main__":
    main()