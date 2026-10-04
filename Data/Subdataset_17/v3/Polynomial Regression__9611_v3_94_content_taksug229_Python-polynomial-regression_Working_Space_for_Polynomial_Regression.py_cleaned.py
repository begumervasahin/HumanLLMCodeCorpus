import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def load_data(file_path):
    dataset = pd.read_csv(file_path)
    X = dataset.iloc[:, 1:2].values
    y = dataset.iloc[:, 2].values
    return X, y
def fit_linear_regression(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model
def fit_polynomial_regression(X, y, degree):
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)
    return poly_features, model
def plot_results(X, y, linear_regressor, polynomial_regressor, poly_features):
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plt.scatter(X, y, color='red', label='Actual Data')
    plt.plot(X, linear_regressor.predict(X), color='blue', label='Linear Prediction')
    plt.title('Linear Regression')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.scatter(X, y, color='red', label='Actual Data')
    plt.plot(X, polynomial_regressor.predict(poly_features.transform(X)), color='blue', label='Polynomial Prediction')
    plt.title('Polynomial Regression')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.legend()
    plt.tight_layout()
    plt.show()
    X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
    plt.scatter(X, y, color='red', label='Actual Data')
    plt.plot(X_grid, polynomial_regressor.predict(poly_features.transform(X_grid)), color='blue', label='Polynomial Prediction')
    plt.title('Polynomial Regression (Smoother Curve)')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()
def predict_salaries(linear_regressor, polynomial_regressor, poly_features, level):
    linear_prediction = linear_regressor.predict([[level]])
    polynomial_prediction = polynomial_regressor.predict(poly_features.transform([[level]]))
    return linear_prediction[0], polynomial_prediction[0]
if __name__ == "__main__":
    X, y = load_data('Position_Salaries.csv')
    linear_regressor = fit_linear_regression(X, y)
    poly_features, polynomial_regressor = fit_polynomial_regression(X, y, degree=4)
    plot_results(X, y, linear_regressor, polynomial_regressor, poly_features)
    level = 6.5
    linear_prediction, polynomial_prediction = predict_salaries(linear_regressor, polynomial_regressor, poly_features, level)
    print(f"Linear Regression Prediction for position level {level}: {linear_prediction}")
    print(f"Polynomial Regression Prediction for position level {level}: {polynomial_prediction}")