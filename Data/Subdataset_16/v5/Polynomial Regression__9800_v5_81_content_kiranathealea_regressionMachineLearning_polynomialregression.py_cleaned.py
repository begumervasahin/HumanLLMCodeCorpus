import numpy as np
import matplotlib.pyplot as plt
import operator
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
b1 = np.array([
    1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973,
    1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986,
    1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
    2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,
    2013, 2014
])
b2 = np.array([
    1.4, 1.4, 1.426, 1.4257, 1.44, 1.44, 1.4144, 1.7064, 1.7177, 1.4757, 1.34,
    1.5652, 1.617, 1.617, 1.6116, 1.6598, 1.5833, 1.6183, 1.6102, 1.6711, 1.669,
    1.6658, 1.6641, 1.6612, 1.6652, 1.6875, 1.702, 1.7034, 1.6963, 1.7582, 1.68,
    1.5, 1.6786, 1.6667, 1.6563, 1.6364, 1.5, 1.65, 1.5, 1.1979, 2, 2.98, 0.84,
    1.6, 1.2069, 2.6204, 2.6277, 2.6277, 2.1429, 1.6448, 1.64, 2.1986, 2.1972, 2.4882
])
b3 = b1[:, np.newaxis]
b4 = b2[:, np.newaxis]
a1 = 2
b5 = PolynomialFeatures(a1=a1)
b6 = b5.fit_transform(b3)
b7 = LinearRegression()
b7.fit(b6, b4)
b8 = b7.predict(b6)
b9 = mean_squared_error(b4, b8)
b10 = r2_score(b4, b8)
print(f'The RMSE of the polynomial regression b7 is {b9}')
print(f'The R2 score of the polynomial regression b7 is {b10}')
b11 = np.array([2015, 2016, 2017, 2018, 2019])
b12 = b5.fit_transform(b11[:, np.newaxis])
b13 = b7.predict(b12)
print(b13)
b14 = np.concatenate((b1, b11))
b15 = np.concatenate((b8, b13))
b16 = sorted(zip(b14, b15), key=operator.itemgetter(0))
x_sorted, b17 = zip(*b16)
plt.scatter(b3, b4, b18 = 10, b19='c', label='Actual Data')
plt.scatter(b11, b13, b18 = 10, b19='r', label='Predicted Future Data')
plt.plot(x_sorted, b17, b19 = 'm', label='Polynomial Regression')
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Polynomial Regression and Prediction')
plt.legend()
plt.show()