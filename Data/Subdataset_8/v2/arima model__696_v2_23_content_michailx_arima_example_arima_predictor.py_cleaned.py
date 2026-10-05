import numpy as np
from statsmodels.tsa.arima.model import ARIMA
historical_data = np.array([16, 20, 32, 40, 20, 18, 11, 21, 4, 6, 31, 48, 43, 49, 37])
arima_model = ARIMA(historical_data, order=(4, 1, 1))
fitted_model = arima_model.fit(disp=0)
start_index = 16
end_index = 19
future_predictions = fitted_model.predict(start=start_index, end=end_index, typ='levels')
print("Predicted values for the next 4 time points:", future_predictions)