import numpy as np
from statsmodels.tsa.arima.model import ARIMA
SERIES = np.array([16, 20, 32, 40, 20, 18, 11, 21, 4, 6, 31, 48, 43, 49, 37])
model = ARIMA(SERIES, order=(4, 1, 1))
model_fit = model.fit(disp=0)
start_index = 16
end_index = 19
prediction = model_fit.predict(start=start_index, end=end_index, typ='levels')
print(prediction)