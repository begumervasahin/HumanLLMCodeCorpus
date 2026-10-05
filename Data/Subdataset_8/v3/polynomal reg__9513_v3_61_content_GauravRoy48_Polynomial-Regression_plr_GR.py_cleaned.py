import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def load_dataset(file_path):
    return pd.read_csv(file_path)
def prepare_data(dataset):
    X = dataset.iloc[:, 1:2].values
    Y = dataset.iloc[:, 2].values
    return X, Y
def train_linear_regression(X, Y):
    model = LinearRegression()
    model.fit(X, Y)
    return model
def train_polynomial_regression(X, Y, degree=4):
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, Y)
    return model, poly_features
def visualize_linear_regression(X, Y, model):
    plt.scatter(X, Y, color='red')
    plt.plot(X, model.predict(X), color='blue')
    plt.title('Linear Regression Results')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.grid()
    plt.show()
def visualize_polynomial_regression(X, Y, model, poly_features):
    plt.scatter(X, Y, color='red')
    X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
    plt.plot(X_grid, model.predict(poly_features.transform(X_grid)), color='green')
    plt.title('Polynomial Regression Results')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.grid()
    plt.show()
def make_predictions(position_level, linear_model, poly_model, poly_features):
    linear_prediction = linear_model.predict([[position_level]])[0]
    polynomial_prediction = poly_model.predict(poly_features.transform([[position_level]]))[0]
    return linear_prediction, polynomial_prediction
dataset = load_dataset('Position_Salaries.csv')
X, Y = prepare_data(dataset)
linear_model = train_linear_regression(X, Y)
poly_model, poly_features = train_polynomial_regression(X, Y, degree=4)
visualize_linear_regression(X, Y, linear_model)
visualize_polynomial_regression(X, Y, poly_model, poly_features)
position_level = 6.5
linear_prediction, polynomial_prediction = make_predictions(position_level, linear_model, poly_model, poly_features)
print(f"Linear Regression Prediction for Position Level {position_level}: {linear_prediction}")
print(f"Polynomial Regression Prediction for Position Level {position_level}: {polynomial_prediction}")