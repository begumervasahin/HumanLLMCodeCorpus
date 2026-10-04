import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linear_regressor = LinearRegression()
linear_regressor.fit(x, y)
polynomial_features = PolynomialFeatures(degree=4)
x_poly = polynomial_features.fit_transform(x)
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(x_poly, y)
def visualize_results(x, y, model, title, xlabel, ylabel, transform=None):
    plt.scatter(x, y, color='red')
    if transform:
        x_grid = np.arange(min(x), max(x), 0.1).reshape(-1, 1)
        plt.plot(x_grid, model.predict(transform(x_grid)), color='blue')
    else:
        plt.plot(x, model.predict(x), color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
visualize_results(x, y, linear_regressor, 'Truth or Bluff (Linear Regression)', 'Position Level', 'Salary')
visualize_results(x, y, polynomial_regressor, 'Truth or Bluff (Polynomial Regression)', 'Position Level', 'Salary', transform=polynomial_features.fit_transform)
linear_prediction = linear_regressor.predict([[6.5]])
print(f"Linear Regression Prediction for position level 6.5: {linear_prediction[0]}")
poly_prediction = polynomial_regressor.predict(polynomial_features.fit_transform([[6.5]]))
print(f"Polynomial Regression Prediction for position level 6.5: {poly_prediction[0]}")