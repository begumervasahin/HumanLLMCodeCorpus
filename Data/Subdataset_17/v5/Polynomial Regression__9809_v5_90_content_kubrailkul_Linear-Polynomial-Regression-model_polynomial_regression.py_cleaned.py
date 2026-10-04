import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/pc/Desktop/kurs/HW1_DATA.csv")
x = data['x'].values
y = data['y'].values
def plot_data(x, y):
    plt.scatter(x, y, c='b', label='Data')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
plot_data(x, y)
def calculate_linear_coefficients(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    xy_mean = np.mean(x * y)
    x_squared_mean = np.mean(x**2)
    den = x_squared_mean - x_mean**2
    a = (xy_mean - x_mean * y_mean) / den
    b = (y_mean * x_squared_mean - xy_mean * x_mean) / den
    return a, b
a, b = calculate_linear_coefficients(x, y)
def plot_linear_fit(x, y, a, b):
    y_hat = a * x + b
    plt.scatter(x, y, c='b', label='Data')
    plt.plot(x, y_hat, c='r', label='Linear Fit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    return y_hat
y_hat = plot_linear_fit(x, y, a, b)
def calculate_r_squared(y, y_hat):
    sse = np.sum((y - y_hat)**2)
    sst = np.sum((y - np.mean(y))**2)
    return 1 - sse / sst
r_squared = calculate_r_squared(y, y_hat)
print(f"Linear Fit R-squared: {r_squared}")
def fit_and_evaluate_polynomial(x, y, degree):
    coefficients = np.polyfit(x, y, degree)
    y_poly_hat = np.polyval(coefficients, x)
    r_squared_poly = calculate_r_squared(y, y_poly_hat)
    return coefficients, y_poly_hat, r_squared_poly
for degree in range(1, 8):
    coefficients, y_poly_hat, r_squared_poly = fit_and_evaluate_polynomial(x, y, degree)
    print(f"Degree {degree} Polynomial Coefficients: {coefficients}")
    print(f"Degree {degree} Polynomial R-squared: {r_squared_poly}")
    plt.scatter(x, y, c='b', label='Data')
    plt.plot(x, y_poly_hat, label=f'Degree {degree} Polynomial Fit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()