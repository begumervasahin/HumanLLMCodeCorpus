import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
lin_reg = LinearRegression()
lin_reg.fit(x, y)
poly_reg2 = PolynomialFeatures(degree=2)
X_poly2 = poly_reg2.fit_transform(x)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly2, y)
poly_reg3 = PolynomialFeatures(degree=3)
X_poly3 = poly_reg3.fit_transform(x)
lin_reg3 = LinearRegression()
lin_reg3.fit(X_poly3, y)
poly_reg4 = PolynomialFeatures(degree=4)
X_poly4 = poly_reg4.fit_transform(x)
lin_reg4 = LinearRegression()
lin_reg4.fit(X_poly4, y)
def plot_regression(x, y, model, poly_reg=None, title='Truth or Bluff', degree=None):
    plt.scatter(x, y, color='red')
    if poly_reg:
        X_grid = np.arange(min(x), max(x), 0.1).reshape(-1, 1)
        plt.plot(X_grid, model.predict(poly_reg.fit_transform(X_grid)), color='blue')
    else:
        plt.plot(x, model.predict(x), color='blue')
    plt.title(title + (f" (degree {degree})" if degree else ""))
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
plot_regression(x, y, lin_reg, title='Linear Regression')
plot_regression(x, y, lin_reg2, poly_reg2, title='Polynomial Regression', degree=2)
plot_regression(x, y, lin_reg3, poly_reg3, title='Polynomial Regression', degree=3)
plot_regression(x, y, lin_reg4, poly_reg4, title='Polynomial Regression', degree=4)
linear_pred = lin_reg.predict([[6.2]])
poly_pred = lin_reg4.predict(poly_reg4.fit_transform([[6.2]]))
print("Linear Regression Prediction for 6.2:", linear_pred)
print("Polynomial Regression Prediction for 6.2:", poly_pred)
print("Linear Regression Coefficients:", lin_reg.coef_, "Intercept:", lin_reg.intercept_)
print("Polynomial Regression Coefficients (degree 4):", lin_reg4.coef_, "Intercept:", lin_reg4.intercept_)