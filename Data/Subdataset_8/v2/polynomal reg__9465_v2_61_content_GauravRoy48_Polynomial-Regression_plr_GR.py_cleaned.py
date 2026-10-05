
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values
linear_model = LinearRegression()
linear_model.fit(X, Y)
poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)
poly_model = LinearRegression()
poly_model.fit(X_poly, Y)
plt.scatter(X, Y, color='red')
plt.plot(X, linear_model.predict(X), color='blue')
plt.title('Linear Regression Results')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.grid()
plt.show()
plt.scatter(X, Y, color='red')
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.plot(X_grid, poly_model.predict(poly_features.transform(X_grid)), color='green')
plt.title('Polynomial Regression Results')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.grid()
plt.show()
position_level = 6.5
linear_prediction = linear_model.predict([[position_level]])[0]
polynomial_prediction = poly_model.predict(poly_features.transform([[position_level]]))[0]
print(f"Linear Regression Prediction for Position Level {position_level}: {linear_prediction}")
print(f"Polynomial Regression Prediction for Position Level {position_level}: {polynomial_prediction}")