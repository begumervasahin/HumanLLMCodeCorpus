import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from Models import LinearModel
def fonk1():
    b1 = np.array([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014])
    b2 = np.array([1.4, 1.4, 1.426, 1.4257, 1.44, 1.44, 1.4144, 1.7064, 1.7177, 1.4757, 1.34, 1.5652, 1.617, 1.617, 1.6116, 1.6598, 1.5833, 1.6183, 1.6102, 1.6711, 1.669, 1.6658, 1.6641, 1.6612, 1.6652, 1.6875, 1.702, 1.7034, 1.6963, 1.7582, 1.68, 1.5, 1.6786, 1.6667, 1.6563, 1.6364, 1.5, 1.65, 1.5, 1.1979, 2, 2.98, 0.84, 1.6, 1.2069, 2.6204, 2.6277, 2.6277, 2.1429, 1.6448, 1.64, 2.1986, 2.1972, 2.4882])
    b1 = b1[:, np.newaxis]
    b2 = b2[:, np.newaxis]
    return b1, b2
if b3 = = "__main__":
    x_train, b4 = fonk1()
    b5 = LinearRegression()
    b6 = LinearModel(b5)
    b5.fit(x_train,b4)
    b6.compute_metrics(x_train, b4)
    print('The RMSE of the linear regression b5 is {}'.format(b6.rmse_))
    print('The R2 score of the linear regression b5 is {}'.format(b6.r2_))
    b7 = PolynomialFeatures(degree=2, include_bias=False)
    b8 = b7.fit_transform(x_train)
    b9 = LinearModel(b5)
    b9.compute_metrics(b8, b4)
    print('The RMSE of the polynomial regression b5 is {}'.format(b9.rmse_))
    print('The R2 score of the polynomial regression b5 is {}'.format(b9.r2_))