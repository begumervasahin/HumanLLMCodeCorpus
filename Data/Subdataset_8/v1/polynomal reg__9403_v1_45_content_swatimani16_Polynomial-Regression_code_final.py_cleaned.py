import numpy as np
import matplotlib.pyplot as plt
def generate_data(sample_points=10, noise_std=0.3):
    x = np.linspace(0, 1, sample_points)
    noise = np.random.normal(0, noise_std, sample_points)
    t = np.sin(2 * np.pi * x) + noise
    return x, t
def polynomial_regression(x, t, M):
    phi_x = np.array([x ** i for i in range(M + 1)]).T
    A = np.dot(phi_x.T, phi_x)
    T = np.dot(phi_x.T, t)
    W = np.linalg.solve(A, T)
    return W
def predict(x, W):
    return np.dot(np.array([x ** i for i in range(len(W))]), W)
def plot_polynomial_fit(x, t, xsin, ysin, M):
    W = polynomial_regression(x, t, M)
    y_estimate = predict(x, W)
    plt.plot(x, y_estimate, 'r-', label='Polynomial Fit')
    plt.plot(xsin, ysin, 'g-', label='True Function')
    plt.plot(x, t, 'bo', label='Noisy Samples')
    plt.legend()
    plt.title(f'Polynomial Regression (M={M})')
    plt.show()
def regularized_regression(x, t, M, lam):
    phi_x = np.array([x ** i for i in range(M + 1)]).T
    S_0 = np.dot(phi_x.T, phi_x) + lam * np.eye(M + 1)
    y_0 = np.dot(t, phi_x)
    coeff = np.linalg.solve(S_0, y_0)[::-1]
    return np.poly1d(coeff)
def plot_regularized_fit(x, t, xsin, ysin, M, lam):
    f = regularized_regression(x, t, M, lam)
    xx = np.linspace(0, 1, len(xsin))
    plt.plot(x, t, 'bo', label='Noisy Samples')
    plt.plot(xsin, ysin, 'g-', label='True Function')
    plt.plot(xx, f(xx), 'r-', label='Regularized Fit')
    plt.legend()
    plt.title(f'Regularized Regression (M={M}, lambda={lam})')
    plt.show()
N = 1000
sample_points = 10
x, t = generate_data(sample_points)
xsin = np.linspace(0, 1, N)
ysin = np.sin(2 * np.pi * xsin)
for M in [0, 1, 3, 9]:
    plot_polynomial_fit(x, t, xsin, ysin, M)
M = 9
lam = 1
plot_regularized_fit(x, t, xsin, ysin, M, lam)