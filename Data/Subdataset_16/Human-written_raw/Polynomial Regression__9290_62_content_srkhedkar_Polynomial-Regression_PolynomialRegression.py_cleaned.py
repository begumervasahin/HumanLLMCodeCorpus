import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
def fonk1(first, last, periods):
    return ((last/first)**(1/periods)-1) * 100
b1 = pd.read_csv('D:\\python3\\data\\SensexHistoricalData.csv')
b1['Date'] = pd.to_datetime(b1.Date)
b1.b2 = b1['Date']
b1.b2 = (b1.b2 - pd.to_datetime('1970-01-01')).days
b3 = np.asarray(b1['Close'])
b4 = np.asarray(b1.b2.values)
b5 = LinearRegression()
b6 = PolynomialFeatures(5)
b7 = b6.fit_transform(b4.reshape(-1, 1))
b5.fit(b7, b3.reshape(-1, 1))
b8 = b5.predict(b7)
b9 = np.asarray(pd.RangeIndex(start=b4[-1], stop=b4[-1] + 3650))
b10 = b6.fit_transform(b9.reshape(-1, 1))
b11 = b5.predict(b10)
print ("Closing price at 2029 would be around ", b11[-1])
b4 = pd.to_datetime(b1.b2, origin='1970-01-01', unit='D')
b12 = pd.to_datetime(b9, origin='1970-01-01', unit='D')
print ('Your investments will have a CAGR of ',(fonk1(b3[-1], b11[-1], 10)), '%')
from matplotlib.pylab import rcParams
rcParams['figure.b13'] = 20,10
plt.figure(b13 = (16,8))
plt.plot(b4,b1['Close'], b14 = 'Close Price History')
plt.plot(b4,b8, b15 = 'r', b14='Mathematical Model')
plt.plot(b12,b11, b15 = 'g', b14='Future Predictions')
plt.suptitle('Stock Market Predictions', b16 = 16)
b17 = plt.gcf()
b17.canvas.set_window_title('Stock Market Predictions')
plt.legend()
plt.show()