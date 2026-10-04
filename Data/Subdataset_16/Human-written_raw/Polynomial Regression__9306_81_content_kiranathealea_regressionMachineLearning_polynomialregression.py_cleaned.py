import numpy as np
import matplotlib.pyplot as plt
import operator
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
b1 = np.array([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014])
b2 = np.array([1.4, 1.4, 1.426, 1.4257, 1.44, 1.44, 1.4144, 1.7064, 1.7177, 1.4757, 1.34, 1.5652, 1.617, 1.617, 1.6116, 1.6598, 1.5833, 1.6183, 1.6102, 1.6711, 1.669, 1.6658, 1.6641, 1.6612, 1.6652, 1.6875, 1.702, 1.7034, 1.6963, 1.7582, 1.68, 1.5, 1.6786, 1.6667, 1.6563, 1.6364, 1.5, 1.65, 1.5, 1.1979, 2, 2.98, 0.84, 1.6, 1.2069, 2.6204, 2.6277, 2.6277, 2.1429, 1.6448, 1.64, 2.1986, 2.1972, 2.4882])
b3 = b1[:, np.newaxis]
b2 = b2[:, np.newaxis]
b4 = PolynomialFeatures(degree=2)
b5 = b4.fit_transform(b3)
b6 = LinearRegression()
b6.fit(b5, b2)
b7 = b6.predict(b5)
b8 = b6.coef_
b9 = mean_squared_error(b2, b7)
b10 = r2_score(b2, b7)
print('The RMSE of the linear regression b6 is {}'.format(b9))
print('The R2 score of the linear regression b6 is {}'.format(b10))
b11 = np.array([2015, 2016, 2017, 2018, 2019])
b12 = b11[:, np.newaxis]
b12 = b4.fit_transform(b12)
b13 = b6.predict(b12)
print(b13)
b14 = np.concatenate((b1, b11))
b15 = np.concatenate((b7, b13))
b16 = b11
b17 = b13
plt.scatter(b3, b2, b18 = 10, b21='c')
plt.scatter(b16, b17, b18 = 10, b21='r')
b19 = operator.itemgetter(0)
b20 = sorted(zip(b14,b15), key=b19)
b14, b15 = zip(*b20)
plt.plot(b14, b15, b21 = 'm')
plt.show()