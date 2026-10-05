import numpy as np
from statsmodels.tsa.arima.model import ARIMA
def generate_arima_predictions(historical_data, order=(4, 1, 1), start_index=16, end_index=19):
    arima_model = ARIMA(historical_data, order=order)
    fitted_model = arima_model.fit(disp=0)
    future_predictions = fitted_model.predict(start=start_index, end=end_index, typ='levels')
    return future_predictions
if __name__ == "__main__":
    historical_data = np.array([16, 20, 32, 40, 20, 18, 11, 21, 4, 6, 31, 48, 43, 49, 37])
    arima_order = (4, 1, 1)
    predictions = generate_arima_predictions(historical_data, order=arima_order)
    print("Predicted values for the next 4 time points:", predictions)