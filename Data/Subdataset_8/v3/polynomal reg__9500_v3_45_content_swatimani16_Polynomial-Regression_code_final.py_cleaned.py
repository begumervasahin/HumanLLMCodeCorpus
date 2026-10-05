import numpy as np
import matplotlib.pyplot as plt
def generate_noisy_data(sample_points=10, noise_std=0.3):
    x = np.linspace(0, 1, sample_points)
    noise = np.random.normal(0, noise_std, sample_points)
    t = np.sin(2 * np.pi * x) + noise
    return x, t
def polynomial_regression(x, t, degree):
    phi_x = np.array([x ** i for i in range(degree + 1)]).T
    A = np.dot(phi_x.T, phi_x)
    T = np.dot(phi_x.T, t)
    coefficients = np.linalg.solve(A, T)
    return coefficients
def predict_polynomial(x, coefficients):
    powers_of_x = np.array([x ** i for i in range(len(coefficients))])
    return np.dot(powers_of_x.T, coefficients)
def plot_polynomial_regression(x, t, xsin, ysin, degree):
    coefficients = polynomial_regression(x, t, degree)
    y_estimate = predict_polynomial(x, coefficients)
    plt.plot(x, y_estimate, 'r-', label='Polynomial Fit')
    plt.plot(xsin, ysin, 'g-', label='True Function')
    plt.plot(x, t, 'bo', label='Noisy Samples')
    plt.legend()
    plt.title(f'Polynomial Regression (Degree={degree})')
    plt.show()
def regularized_regression(x, t, degree, lambda_val):
    phi_x = np.array([x ** i for i in range(degree + 1)]).T
    S_0 = np.dot(phi_x.T, phi_x) + lambda_val * np.eye(degree + 1)
    y_0 = np.dot(t, phi_x)
    coefficients = np.linalg.solve(S_0, y_0)[::-1]
    return np.poly1d(coefficients)
def plot_regularized_regression(x, t, xsin, ysin, degree, lambda_val):
    f = regularized_regression(x, t, degree, lambda_val)
    xx = np.linspace(0, 1, len(xsin))
    plt.plot(x, t, 'bo', label='Noisy Samples')
    plt.plot(xsin, ysin, 'g-', label='True Function')
    plt.plot(xx, f(xx), 'r-', label='Regularized Fit')
    plt.legend()
    plt.title(f'Regularized Regression (Degree={degree}, Lambda={lambda_val})')
    plt.show()
N = 1000
sample_points = 10
x, t = generate_noisy_data(sample_points)
xsin = np.linspace(0, 1, N)
ysin = np.sin(2 * np.pi * xsin)
for degree in [0, 1, 3, 9]:
    plot_polynomial_regression(x, t, xsin, ysin, degree)
degree = 9
lambda_val = 1
plot_regularized_regression(x, t, xsin, ysin, degree, lambda_val)