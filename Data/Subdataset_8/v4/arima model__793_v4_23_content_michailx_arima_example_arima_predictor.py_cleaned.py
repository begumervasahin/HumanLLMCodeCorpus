
from statsmodels.tsa.arima_model import ARIMA
time_series = [16, 20, 32, 40, 20, 18, 11, 21, 4, 6, 31, 48, 43, 49, 37]
arima_model = ARIMA(time_series, order=(4, 1, 1))
model_fit = arima_model.fit(disp=0)
predictions = model_fit.predict(start=16, end=19, typ='levels')
print(predictions)