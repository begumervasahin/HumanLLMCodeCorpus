import numpy as np
import matplotlib.pyplot as plt
N = 1000
sample_points = 10
x = np.linspace(0, 1, sample_points)
noise = np.random.normal(0, 0.3, sample_points)
t = np.sin(2 * np.pi * x) + noise
def predict_y(x, W, M):
    Y = np.array([W[i] * (x ** i) for i in range(M + 1)])
    return Y.sum()
def calculate_weights(x, t, M):
    A = np.zeros((M + 1, M + 1))
    for i in range(M + 1):
        for j in range(M + 1):
            A[i, j] = (x ** (i + j)).sum()
    T = np.array([((x ** i) * t).sum() for i in range(M + 1)])
    return np.linalg.solve(A, T)
for M in [0, 1, 3, 9]:
    W = calculate_weights(x, t, M)
    y_estimate = [predict_y(i, W, M) for i in x]
    plt.plot(x, y_estimate, 'r-')
    plt.plot(x, t, 'bo')
    plt.plot(x, np.sin(2 * np.pi * x), 'g-')
    plt.show()
def compute_design_matrix(x, M):
    return x[:, None] ** np.arange(M + 1)
M = 9
lam = 1
phi_x = compute_design_matrix(x, M)
S_0 = phi_x.T.dot(phi_x) + lam * np.eye(M + 1)
y_0 = t.dot(phi_x)
coeff = np.linalg.solve(S_0, y_0)[::-1]
f = np.poly1d(coeff)
xx = np.linspace(0, 1, N)
fig, ax = plt.subplots()
ax.plot(x, t, 'bo')
ax.plot(xx, np.sin(2 * np.pi * xx), 'g-')
ax.plot(xx, f(xx), 'r-')
plt.show()