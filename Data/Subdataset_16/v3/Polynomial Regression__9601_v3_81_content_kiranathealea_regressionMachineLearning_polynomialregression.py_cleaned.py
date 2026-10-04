import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
def fonk1():
    b1 = np.array([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014])
    b2 = np.array([1.4, 1.4, 1.426, 1.4257, 1.44, 1.44, 1.4144, 1.7064, 1.7177, 1.4757, 1.34, 1.5652, 1.617, 1.617, 1.6116, 1.6598, 1.5833, 1.6183, 1.6102, 1.6711, 1.669, 1.6658, 1.6641, 1.6612, 1.6652, 1.6875, 1.702, 1.7034, 1.6963, 1.7582, 1.68, 1.5, 1.6786, 1.6667, 1.6563, 1.6364, 1.5, 1.65, 1.5, 1.1979, 2, 2.98, 0.84, 1.6, 1.2069, 2.6204, 2.6277, 2.6277, 2.1429, 1.6448, 1.64, 2.1986, 2.1972, 2.4882])
    return b1, b2
def fonk2(b1, b2):
    b3 = b1[:, np.newaxis]
    b4 = b2[:, np.newaxis]
    b5 = PolynomialFeatures(degree=2)
    b6 = b5.fit_transform(b3)
    return b3, b4, b6, b5
def fonk3(b6, b4):
    b7 = LinearRegression()
    b7.fit(b6, b4)
    b8 = b7.predict(b6)
    return b7, b8
def fonk4(b4, b8):
    b9 = mean_squared_error(b4, b8)
    b10 = r2_score(b4, b8)
    print(f'The RMSE of the polynomial regression b7 is {b9}')
    print(f'The R2 score of the polynomial regression b7 is {b10}')
def fonk5(b7, b5):
    b11 = np.array([2015, 2016, 2017, 2018, 2019])
    b12 = b5.fit_transform(b11[:, np.newaxis])
    b13 = b7.predict(b12)
    print(f'Predicted b2 for future b1: {b13.flatten()}')
    return b11, b13
def fonk6(b3, b4, b11, b13, b8):
    b14 = np.concatenate((b3.flatten(), b11))
    b15 = np.concatenate((b8.flatten(), b13.flatten()))
    plt.scatter(b3, b4, b16 = 10, b17='c', label='Observed Data')
    plt.scatter(b11, b13, b16 = 10, b17='r', label='Predicted Data')
    plt.plot(b14, b15, b17 = 'm', label='Polynomial Regression (degree 2)')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Polynomial Regression')
    plt.legend()
    plt.show()
def fonk7():
    b1, b2 = fonk1()
    b3, b4, b6, b5 = fonk2(b1, b2)
    b7, b8 = fonk3(b6, b4)
    fonk4(b4, b8)
    b11, b13 = fonk5(b7, b5)
    fonk6(b3, b4, b11, b13, b8)
if b18 = = "__main__":
    fonk7()