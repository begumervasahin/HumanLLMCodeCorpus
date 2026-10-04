import numpy as np
import matplotlib.pyplot as plt
import operator
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
years = np.array([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014])
values = np.array([1.4, 1.4, 1.426, 1.4257, 1.44, 1.44, 1.4144, 1.7064, 1.7177, 1.4757, 1.34, 1.5652, 1.617, 1.617, 1.6116, 1.6598, 1.5833, 1.6183, 1.6102, 1.6711, 1.669, 1.6658, 1.6641, 1.6612, 1.6652, 1.6875, 1.702, 1.7034, 1.6963, 1.7582, 1.68, 1.5, 1.6786, 1.6667, 1.6563, 1.6364, 1.5, 1.65, 1.5, 1.1979, 2, 2.98, 0.84, 1.6, 1.2069, 2.6204, 2.6277, 2.6277, 2.1429, 1.6448, 1.64, 2.1986, 2.1972, 2.4882])
x = years[:, np.newaxis]
y = values[:, np.newaxis]
polynomial_features = PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(x)
model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)
rmse = mean_squared_error(y, y_poly_pred)
r2 = r2_score(y, y_poly_pred)
print(f'The RMSE of the linear regression model is {rmse}')
print(f'The R2 score of the linear regression model is {r2}')
future_years = np.array([2015, 2016, 2017, 2018, 2019])
future_years_poly = polynomial_features.fit_transform(future_years[:, np.newaxis])
future_values_pred = model.predict(future_years_poly)
print(future_values_pred)
x_final = np.concatenate((years, future_years))
y_final = np.concatenate((y_poly_pred, future_values_pred))
plt.scatter(x, y, s=10, color='c', label='Actual Data')
plt.scatter(future_years, future_values_pred, s=10, color='r', label='Predicted Future Data')
sorted_data = sorted(zip(x_final, y_final), key=operator.itemgetter(0))
x_final, y_final = zip(*sorted_data)
plt.plot(x_final, y_final, color='m', label='Polynomial Regression')
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Polynomial Regression and Prediction')
plt.legend()
plt.show()