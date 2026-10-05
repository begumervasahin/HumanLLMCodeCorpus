from statsmodels.tsa.arima_model import ARIMA
SERIES = [16, 20, 32, 40, 20, 18, 11, 21, 4, 6, 31, 48, 43, 49, 37]
model = ARIMA(SERIES, order=(4,1,1))
model_fit = model.fit(disp=0)
prediction = model_fit.predict(16, 19, typ='levels')
print prediction