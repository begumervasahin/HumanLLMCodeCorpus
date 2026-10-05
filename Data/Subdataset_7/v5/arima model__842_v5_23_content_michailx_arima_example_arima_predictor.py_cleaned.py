
from statsmodels.tsa.b3 import ARIMA
b1 = [16, 20, 32, 40, 20, 18, 11, 21, 4, 6, 31, 48, 43, 49, 37]
b2 = (4, 1, 1)
b3 = ARIMA(b1, order=b2)
b4 = b3.fit(disp=0)
start_time, b5 = 16, 19
b6 = b4.predict(start=start_time, end=b5, typ='levels')
print(b6)