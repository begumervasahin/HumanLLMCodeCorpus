import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
def fonk1(first, last, periods):
    return ((last / first) ** (1 / periods) - 1) * 100
def fonk2(b19):
    b1 = pd.read_csv(b19)
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1.set_index('Date', b2 = True)
    b1.b3 = (b1.b3 - pd.to_datetime('1970-01-01')).days
    return b1
def fonk3(b1):
    b4 = np.asarray(b1['Close'])
    b5 = np.asarray(b1.b3.values)
    return b5, b4
def fonk4(b5, b4, b6 = 5):
    b7 = PolynomialFeatures(b6)
    b8 = b7.fit_transform(b5.reshape(-1, 1))
    b9 = LinearRegression()
    b9.fit(b8, b4.reshape(-1, 1))
    return b9, b7
def fonk5(b9, b7, b5, b10 = 3650):
    b11 = np.asarray(pd.RangeIndex(start=b5[-1], stop=b5[-1] + b10))
    b12 = b7.fit_transform(b11.reshape(-1, 1))
    b13 = b9.predict(b12)
    return b13, b11
def fonk6(b22, y_actual, b20, b23, b13):
    plt.figure(b14 = (16, 8))
    plt.plot(b22, y_actual, b15 = 'Close Price History')
    plt.plot(b22, b20, b16 = 'r', b15='Mathematical Model')
    plt.plot(b23, b13, b16 = 'g', b15='Future Predictions')
    plt.suptitle('Stock Market Predictions', b17 = 16)
    plt.legend()
    b18 = plt.gcf()
    b18.canvas.manager.set_window_title('Stock Market Predictions')
    plt.show()
def fonk7():
    b19 = 'D:\\python3\\data\\SensexHistoricalData.csv'
    b1 = fonk2(b19)
    b5, b4 = fonk3(b1)
    b9, b7 = fonk4(b5, b4)
    b20 = b9.predict(b7.fit_transform(b5.reshape(-1, 1)))
    b13, b11 = fonk5(b9, b7, b5)
    print("Closing price at 2029 would be around ", b13[-1][0])
    b21 = fonk1(b4[-1], b13[-1][0], 10)
    print('Your investments will have a CAGR of ', b21, '%')
    b22 = pd.to_datetime(b1.b3, origin='1970-01-01', unit='D')
    b23 = pd.to_datetime(b11, origin='1970-01-01', unit='D')
    fonk6(b22, b1['Close'], b20, b23, b13)
if b24 = = "__main__":
    fonk7()