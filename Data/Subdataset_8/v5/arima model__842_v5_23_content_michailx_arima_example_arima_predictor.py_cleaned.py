
from statsmodels.tsa.arima_model import ARIMA
time_series = [16, 20, 32, 40, 20, 18, 11, 21, 4, 6, 31, 48, 43, 49, 37]
order_params = (4, 1, 1)
arima_model = ARIMA(time_series, order=order_params)
model_fit = arima_model.fit(disp=0)
start_time, end_time = 16, 19
predicted_values = model_fit.predict(start=start_time, end=end_time, typ='levels')
print(predicted_values)