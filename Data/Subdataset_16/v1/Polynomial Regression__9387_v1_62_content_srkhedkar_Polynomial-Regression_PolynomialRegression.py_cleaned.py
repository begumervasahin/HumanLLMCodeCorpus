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
b4 = np.asarray(b1['Close'])
b5 = np.asarray(b1.b3.values)
b6 = LinearRegression()
b7 = PolynomialFeatures(5)
b8 = b7.fit_transform(b5.reshape(-1, 1))
b6.fit(b8, b4.reshape(-1, 1))
b9 = b6.predict(b8)
b10 = np.asarray(pd.RangeIndex(start=b5[-1], stop=b5[-1] + 3650))
b11 = b7.fit_transform(b10.reshape(-1, 1))
b12 = b6.predict(b11)
print("Closing price at 2029 would be around ", b12[-1])
b5 = pd.to_datetime(b1.b3, origin='1970-01-01', unit='D')
b13 = pd.to_datetime(b10, origin='1970-01-01', unit='D')
print('Your investments will have a CAGR of ', (fonk1(b4[-1], b12[-1], 10)), '%')
from matplotlib.pylab import rcParams
rcParams['figure.b14'] = 20, 10
plt.figure(b14 = (16, 8))
plt.plot(b5, b1['Close'], b15 = 'Close Price History')
plt.plot(b5, b9, b16 = 'r', b15='Mathematical Model')
plt.plot(b13, b12, b16 = 'g', b15='Future Predictions')
plt.suptitle('Stock Market Predictions', b17 = 16)
b18 = plt.gcf()
b18.canvas.manager.set_window_title('Stock Market Predictions')