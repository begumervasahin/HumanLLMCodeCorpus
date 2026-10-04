import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_poly, y)
def visualize_regression(X, y, regressor, title, xlabel, ylabel):
    plt.scatter(X, y, color='red')
    plt.plot(X, regressor.predict(X), color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
visualize_regression(X, y, linear_regressor, 'Truth or Bluff (Linear Regression)', 'Position level', 'Salary')
visualize_regression(X, y, polynomial_regressor, 'Truth or Bluff (Polynomial Regression)', 'Position level', 'Salary')
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, polynomial_regressor.predict(poly_features.transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression - High Resolution)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
linear_prediction = linear_regressor.predict([[6.5]])
polynomial_prediction = polynomial_regressor.predict(poly_features.transform([[6.5]]))
print(f"Linear Regression Prediction for 6.5: {linear_prediction[0]}")
print(f"Polynomial Regression Prediction for 6.5: {polynomial_prediction[0]}")