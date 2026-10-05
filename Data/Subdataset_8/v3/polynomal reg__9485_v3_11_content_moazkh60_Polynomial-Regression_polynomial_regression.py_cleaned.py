import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def load_dataset(filename):
    return pd.read_csv(filename)
def prepare_data(dataset):
    X = dataset['Level'].values.reshape(-1, 1)
    y = dataset['Salary'].values
    return X, y
def fit_linear_regression(X, y):
    regressor = LinearRegression()
    regressor.fit(X, y)
    return regressor
def fit_polynomial_regression(X, y, degree=4):
    polynomial_features = PolynomialFeatures(degree=degree)
    X_poly = polynomial_features.fit_transform(X)
    regressor = LinearRegression()
    regressor.fit(X_poly, y)
    return regressor, polynomial_features
def visualize_results(X, y, regressors, labels):
    plt.scatter(X, y, color='red')
    for regressor, label in zip(regressors, labels):
        if label == 'Linear':
            plt.plot(X, regressor.predict(X), label=label)
        else:
            plt.plot(X, regressor[0].predict(regressor[1].fit_transform(X)), label=label)
    plt.title('Regression Analysis')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()
def predict(regressor, poly_features, value):
    if poly_features:
        prediction = regressor.predict(poly_features.transform([[value]]))
    else:
        prediction = regressor.predict([[value]])
    return prediction
if __name__ == "__main__":
    dataset = load_dataset('Position_Salaries.csv')
    X, y = prepare_data(dataset)
    linear_regressor = fit_linear_regression(X, y)
    polynomial_regressor, poly_features = fit_polynomial_regression(X, y)
    visualize_results(X, y, [(linear_regressor, 'Linear'), (polynomial_regressor, poly_features, 'Polynomial')], ['Linear', 'Polynomial'])
    level = 6.5
    linear_prediction = predict(linear_regressor, None, level)
    polynomial_prediction = predict(polynomial_regressor, poly_features, level)
    print(f"Linear Regression prediction for position level {level}: ${linear_prediction[0]:,.2f}")
    print(f"Polynomial Regression prediction for position level {level}: ${polynomial_prediction[0]:,.2f}")