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
degree = 4
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
def visualize_regression_results(X, y, model, title):
    plt.scatter(X, y, color='red')
    plt.plot(X, model.predict(X), color='blue')
    plt.title(title)
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
visualize_regression_results(X, y, linear_regressor, 'Truth or Bluff (Linear Regression)')
visualize_regression_results(X, y, poly_regressor, 'Truth or Bluff (Polynomial Regression)')
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, poly_regressor.predict(poly_features.transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression - High Resolution)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
position_level = 6.5
linear_prediction = linear_regressor.predict([[position_level]])
poly_prediction = poly_regressor.predict(poly_features.transform([[position_level]]))
print(f'Linear Prediction for level {position_level}: {linear_prediction[0]}')
print(f'Polynomial Prediction for level {position_level}: {poly_prediction[0]}')