import numpy as np
import matplotlib.pyplot as plt
num_points = 1000
num_samples = 10
x_samples = np.linspace(0, 1, num_samples)
noise = np.random.normal(0, 0.3, num_samples)
t_samples = np.sin(2 * np.pi * x_samples) + noise
def predict_y(x, weights, degree):
    polynomial_terms = np.array([weights[i] * (x ** i) for i in range(degree + 1)])
    return np.sum(polynomial_terms)
def calculate_weights(x, t, degree):
    A = np.zeros((degree + 1, degree + 1))
    for i in range(degree + 1):
        for j in range(degree + 1):
            A[i, j] = (x ** (i + j)).sum()
    T = np.array([((x ** i) * t).sum() for i in range(degree + 1)])
    return np.linalg.solve(A, T)
def compute_design_matrix(x, degree):
    return x[:, None] ** np.arange(degree + 1)
for degree in [0, 1, 3, 9]:
    weights = calculate_weights(x_samples, t_samples, degree)
    y_estimates = [predict_y(i, weights, degree) for i in x_samples]
    plt.plot(x_samples, y_estimates, 'r-', label=f'Degree {degree}')
    plt.plot(x_samples, t_samples, 'bo', label='Sample Points')
    plt.plot(x_samples, np.sin(2 * np.pi * x_samples), 'g-', label='True Sine Curve')
    plt.legend()
    plt.show()
degree = 9
regularization_param = 1
design_matrix = compute_design_matrix(x_samples, degree)
S_0 = design_matrix.T.dot(design_matrix) + regularization_param * np.eye(degree + 1)
y_0 = t_samples.dot(design_matrix)
coefficients = np.linalg.solve(S_0, y_0)[::-1]
fitted_polynomial = np.poly1d(coefficients)
x_smooth = np.linspace(0, 1, num_points)
plt.plot(x_samples, t_samples, 'bo', label='Sample Points')
plt.plot(x_smooth, np.sin(2 * np.pi * x_smooth), 'g-', label='True Sine Curve')
plt.plot(x_smooth, fitted_polynomial(x_smooth), 'r-', label='Fitted Polynomial')
plt.legend()
plt.show()