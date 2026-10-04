import numpy as np
from sklearn.b3 import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from Models import LinearModel
def fonk1():
    b1 = np.array([
        1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970,
        1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
        1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990,
        1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
        2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
        2011, 2012, 2013, 2014
    ])
    b2 = np.array([
        1.4, 1.4, 1.426, 1.4257, 1.44, 1.44, 1.4144, 1.7064, 1.7177, 1.4757,
        1.34, 1.5652, 1.617, 1.617, 1.6116, 1.6598, 1.5833, 1.6183, 1.6102, 1.6711,
        1.669, 1.6658, 1.6641, 1.6612, 1.6652, 1.6875, 1.702, 1.7034, 1.6963, 1.7582,
        1.68, 1.5, 1.6786, 1.6667, 1.6563, 1.6364, 1.5, 1.65, 1.5, 1.1979,
        2, 2.98, 0.84, 1.6, 1.2069, 2.6204, 2.6277, 2.6277, 2.1429, 1.6448,
        1.64, 2.1986, 2.1972, 2.4882
    ])
    return b1[:, np.newaxis], b2[:, np.newaxis]
def fonk2(x_train, b11):
    b3 = LinearRegression()
    b4 = LinearModel(b3)
    b3.fit(x_train, b11)
    b4.compute_metrics(x_train, b11)
    return b4
def fonk3(x_train, b11, b5 = 2):
    b6 = PolynomialFeatures(b5=b5, include_bias=False)
    b7 = b6.fit_transform(x_train)
    b8 = LinearRegression()
    b9 = LinearModel(b8)
    b8.fit(b7, b11)
    b9.compute_metrics(b7, b11)
    return b9
if b10 = = "__main__":
    x_train, b11 = fonk1()
    b4 = fonk2(x_train, b11)
    print('The RMSE of the linear regression model is {:.4f}'.format(b4.rmse_))
    print('The R2 score of the linear regression model is {:.4f}'.format(b4.r2_))
    b9 = fonk3(x_train, b11, b5=2)
    print('The RMSE of the polynomial regression model is {:.4f}'.format(b9.rmse_))
    print('The R2 score of the polynomial regression model is {:.4f}'.format(b9.r2_))