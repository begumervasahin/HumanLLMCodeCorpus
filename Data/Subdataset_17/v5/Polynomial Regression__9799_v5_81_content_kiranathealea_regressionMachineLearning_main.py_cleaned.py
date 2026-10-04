import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from Models import LinearModel
def generate_data_set():
    x = np.array([
        1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970,
        1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
        1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990,
        1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
        2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
        2011, 2012, 2013, 2014
    ])
    y = np.array([
        1.4, 1.4, 1.426, 1.4257, 1.44, 1.44, 1.4144, 1.7064, 1.7177, 1.4757,
        1.34, 1.5652, 1.617, 1.617, 1.6116, 1.6598, 1.5833, 1.6183, 1.6102, 1.6711,
        1.669, 1.6658, 1.6641, 1.6612, 1.6652, 1.6875, 1.702, 1.7034, 1.6963, 1.7582,
        1.68, 1.5, 1.6786, 1.6667, 1.6563, 1.6364, 1.5, 1.65, 1.5, 1.1979,
        2, 2.98, 0.84, 1.6, 1.2069, 2.6204, 2.6277, 2.6277, 2.1429, 1.6448,
        1.64, 2.1986, 2.1972, 2.4882
    ])
    return x[:, np.newaxis], y[:, np.newaxis]
def train_and_evaluate_linear_model(x_train, y_train):
    linear_model = LinearRegression()
    linear_regression = LinearModel(linear_model)
    linear_model.fit(x_train, y_train)
    linear_regression.compute_metrics(x_train, y_train)
    return linear_regression
def train_and_evaluate_polynomial_model(x_train, y_train, degree=2):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    x_poly_train = polynomial_features.fit_transform(x_train)
    polynomial_model = LinearRegression()
    polynomial_regression = LinearModel(polynomial_model)
    polynomial_model.fit(x_poly_train, y_train)
    polynomial_regression.compute_metrics(x_poly_train, y_train)
    return polynomial_regression
if __name__ == "__main__":
    x_train, y_train = generate_data_set()
    linear_regression = train_and_evaluate_linear_model(x_train, y_train)
    print('The RMSE of the linear regression model is {:.4f}'.format(linear_regression.rmse_))
    print('The R2 score of the linear regression model is {:.4f}'.format(linear_regression.r2_))
    polynomial_regression = train_and_evaluate_polynomial_model(x_train, y_train, degree=2)
    print('The RMSE of the polynomial regression model is {:.4f}'.format(polynomial_regression.rmse_))
    print('The R2 score of the polynomial regression model is {:.4f}'.format(polynomial_regression.r2_))