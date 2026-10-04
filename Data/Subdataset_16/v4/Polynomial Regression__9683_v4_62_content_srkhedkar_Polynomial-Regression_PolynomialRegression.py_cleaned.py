import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
def fonk1(first, last, periods):
    return ((last / first) ** (1 / periods) - 1) * 100
b1 = pd.read_csv('D:\\python3\\data\\SensexHistoricalData.csv')
b1['Date'] = pd.to_datetime(b1['Date'])
b1.set_index('Date', b2 = True)
b1.b3 = (b1.b3 - pd.to_datetime('1970-01-01')).days
b4 = b1['Close'].values
b5 = b1.b3.values
b6 = LinearRegression()
b7 = PolynomialFeatures(5)
b8 = b7.fit_transform(b5.reshape(-1, 1))
b6.fit(b8, b4.reshape(-1, 1))
b9 = b6.predict(b8)
b10 = np.arange(b5[-1], b5[-1] + 3650)
b11 = b7.fit_transform(b10.reshape(-1, 1))
b12 = b6.predict(b11)
b13 = b12[-1][0]
print(f"Closing price at 2029 would be around {b13:.2f}")
b14 = fonk1(b4[-1], b13, 10)
print(f"Your investments will have a CAGR of {b14:.2f}%")
b15 = pd.to_datetime(b1.b3, origin='1970-01-01', unit='D')
b16 = pd.to_datetime(b10, origin='1970-01-01', unit='D')
plt.figure(b17 = (16, 8))
plt.plot(b15, b1['Close'], b18 = 'Close Price History')
plt.plot(b15, b9, b19 = 'r', b18='Mathematical Model')
plt.plot(b16, b12, b19 = 'g', b18='Future Predictions')
plt.suptitle('Stock Market Predictions', b20 = 16)
b21 = plt.gcf()
b21.canvas.manager.set_window_title('Stock Market Predictions')
plt.legend()
plt.show()