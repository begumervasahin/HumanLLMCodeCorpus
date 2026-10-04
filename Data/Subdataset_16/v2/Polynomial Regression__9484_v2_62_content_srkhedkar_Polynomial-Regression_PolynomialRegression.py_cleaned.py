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
print("Closing price at 2029 would be around ", b12[-1][0])
b13 = pd.to_datetime(b1.b3, origin='1970-01-01', unit='D')
b14 = pd.to_datetime(b10, origin='1970-01-01', unit='D')
print('Your investments will have a CAGR of ', (fonk1(b4[-1], b12[-1][0], 10)), '%')
from matplotlib.pylab import rcParams
rcParams['figure.b15'] = 20, 10
plt.figure(b15 = (16, 8))
plt.plot(b13, b1['Close'], b16 = 'Close Price History')
plt.plot(b13, b9, b17 = 'r', b16='Mathematical Model')
plt.plot(b14, b12, b17 = 'g', b16='Future Predictions')
plt.suptitle('Stock Market Predictions', b18 = 16)
b19 = plt.gcf()
b19.canvas.manager.set_window_title('Stock Market Predictions')
plt.legend()
plt.show()