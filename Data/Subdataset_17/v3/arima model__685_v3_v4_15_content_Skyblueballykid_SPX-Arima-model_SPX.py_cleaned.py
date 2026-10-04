import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
def load_data(file_path):
    return pd.read_csv(file_path)
def display_head(dataframe, n=5):
    print(f"First {n} rows of the DataFrame:")
    print(dataframe.head(n))
def create_arima_model(data, order):
    model = ARIMA(data, order=order)
    return model.fit()
def forecast_next_value(fitted_model):
    return fitted_model.forecast()[0]
def display_model_summary(fitted_model, rows=5):
    print(f"First {rows} rows of the ARIMA model summary:")
    print(fitted_model.summary().tables[1].as_html())
def main():
    csv_file_path = "SPX Weekly 2000-2017.csv"
    spx_data = load_data(csv_file_path)
    display_head(spx_data)
    arima_order = (0, 1, 0)
    fitted_arima_model = create_arima_model(spx_data, arima_order)
    forecasted_value = forecast_next_value(fitted_arima_model)
    print("Forecasted value:", forecasted_value)
    display_model_summary(fitted_arima_model)
if __name__ == "__main__":
    main()