import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import linalg
data = pd.read_csv("C:/Users/pc/Desktop/kurs/HW1_DATA.csv")
x = data['x'].values
y = data['y'].values
plt.scatter(x, y, c='b', label='Data')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
x_mean = np.mean(x)
y_mean = np.mean(y)
xy_mean = np.mean(x * y)
x_squared_mean = np.mean(x**2)
den = x_squared_mean - x_mean**2
a = (xy_mean - x_mean * y_mean) / den
b = (y_mean * x_squared_mean - xy_mean * x_mean) / den
y_hat = a * x + b
plt.scatter(x, y, c='b', label='Data')
plt.plot(x, y_hat, c='r', label='Linear Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
sse = np.sum((y - y_hat)**2)
sst = np.sum((y - y_mean)**2)
r_squared = 1 - sse / sst
print(f"Linear Fit R-squared: {r_squared}")
def y_poly(p, x):
    y_hat = np.polyval(p, x)
    return y_hat
def calculate_r_squared(y_hat, y):
    sse = np.sum((y - y_hat)**2)
    sst = np.sum((y - np.mean(y))**2)
    return 1 - sse / sst
for degree in range(1, 8):
    coefficients = np.polyfit(x, y, degree)
    y_poly_hat = y_poly(coefficients, x)
    r_squared_poly = calculate_r_squared(y_poly_hat, y)
    print(f"Degree {degree} Polynomial Coefficients: {coefficients}")
    print(f"Degree {degree} Polynomial R-squared: {r_squared_poly}")
    plt.scatter(x, y, c='b', label='Data')
    plt.plot(x, y_poly_hat, label=f'Degree {degree} Polynomial Fit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()