import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
def fonk1(initial_value, final_value, periods):
    return ((final_value / initial_value) ** (1 / periods) - 1) * 100
b1 = 'D:\\python3\\data\\SensexHistoricalData.csv'
b2 = pd.read_csv(b1)
b2['Date'] = pd.to_datetime(b2['Date'])
b2.set_index('Date', b3 = True)
b4 = (b2.b5 - pd.to_datetime('1970-01-01')).b7
b2.b5 = b4
b6 = b2['Close'].values
b7 = b2.b5.values
b8 = PolynomialFeatures(degree=5)
b9 = b8.fit_transform(b7.reshape(-1, 1))
b10 = LinearRegression()
b10.fit(b9, b6.reshape(-1, 1))
b11 = b10.predict(b9)
b12 = np.arange(b7[-1], b7[-1] + 3650)
b13 = b8.fit_transform(b12.reshape(-1, 1))
b14 = b10.predict(b13)
b15 = b14[-1][0]
print(f"Closing price at 2029 would be around {b15:.2f}")
b16 = fonk1(b6[-1], b15, 10)
print(f"Your investments will have a CAGR of {b16:.2f}%")
b17 = pd.to_datetime(b2.b5, origin='1970-01-01', unit='D')
b18 = pd.to_datetime(b12, origin='1970-01-01', unit='D')
plt.figure(b19 = (16, 8))
plt.plot(b17, b2['Close'], b20 = 'Close Price History')
plt.plot(b17, b11, b21 = 'r', b20='Mathematical Model')
plt.plot(b18, b14, b21 = 'g', b20='Future Predictions')
plt.suptitle('Stock Market Predictions', b22 = 16)
b23 = plt.gcf()
b23.canvas.manager.set_window_title('Stock Market Predictions')
plt.legend()
plt.show()