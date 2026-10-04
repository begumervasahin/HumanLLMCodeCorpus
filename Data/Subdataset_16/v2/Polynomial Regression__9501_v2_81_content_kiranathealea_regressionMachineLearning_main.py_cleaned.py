import numpy as np
from sklearn.b11 import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b7, b8):
        b4 = self.b1.predict(b7)
        self.b2 = np.sqrt(mean_squared_error(b8, b4))
        self.b3 = r2_score(b8, b4)
def fonk3():
    b5 = np.array([
        1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971,
        1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982,
        1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993,
        1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004,
        2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014
    ])
    b6 = np.array([
        1.4, 1.4, 1.426, 1.4257, 1.44, 1.44, 1.4144, 1.7064, 1.7177, 1.4757,
        1.34, 1.5652, 1.617, 1.617, 1.6116, 1.6598, 1.5833, 1.6183, 1.6102,
        1.6711, 1.669, 1.6658, 1.6641, 1.6612, 1.6652, 1.6875, 1.702, 1.7034,
        1.6963, 1.7582, 1.68, 1.5, 1.6786, 1.6667, 1.6563, 1.6364, 1.5, 1.65,
        1.5, 1.1979, 2, 2.98, 0.84, 1.6, 1.2069, 2.6204, 2.6277, 2.6277,
        2.1429, 1.6448, 1.64, 2.1986, 2.1972, 2.4882
    ])
    b7 = b5[:, np.newaxis]
    b8 = b6[:, np.newaxis]
    return b7, b8
if b9 = = "__main__":
    x_train, b10 = fonk3()
    b11 = LinearRegression()
    b12 = class1(b11)
    b11.fit(x_train, b10)
    b12.fonk2(x_train, b10)
    print(f'The RMSE of the linear regression b1 is {b12.b2}')
    print(f'The R2 score of the linear regression b1 is {b12.b3}')
    b13 = PolynomialFeatures(degree=2, include_bias=False)
    b14 = b13.fit_transform(x_train)
    b15 = LinearRegression()
    b15.fit(b14, b10)
    b16 = class1(b15)
    b16.fonk2(b14, b10)
    print(f'The RMSE of the polynomial regression b1 is {b16.b2}')
    print(f'The R2 score of the polynomial regression b1 is {b16.b3}')