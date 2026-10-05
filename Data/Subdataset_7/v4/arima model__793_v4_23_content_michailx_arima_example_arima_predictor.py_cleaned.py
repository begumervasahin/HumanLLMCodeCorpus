
from statsmodels.tsa.b2 import ARIMA
b1 = [16, 20, 32, 40, 20, 18, 11, 21, 4, 6, 31, 48, 43, 49, 37]
b2 = ARIMA(b1, order=(4, 1, 1))
b3 = b2.fit(disp=0)
b4 = b3.predict(start=16, end=19, typ='levels')
print(b4)