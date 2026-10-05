import numpy as np
import matplotlib.pyplot as plt
X = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
Y = np.array([4, 5, 6, 8, 11, 15, 20, 30, 50, 100])
plt.scatter(X, Y, s=50, color='red')
b0, b1, b2, b3, b4 = 0, -10, -50, -10, 50
N = len(Y)
learning_rate = 0.001
a = X
b = np.array([0.01, 0.04, 0.09, 0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1])
c = np.array([0.001, 0.008, 0.027, 0.064, 0.125, 0.216, 0.343, 0.512, 0.729, 1])
d = np.array([0.00001, 0.0016, 0.0081, 0.0256, 0.0625, 0.1296, 0.2401, 0.4096, 0.6561, 1])
for _ in range(1000):
    Yguess = b0 + b1 * a + b2 * b + b3 * c + b4 * d
    b0_gradient = (-2 / N) * np.sum(Y - Yguess)
    b1_gradient = (-2 / N) * np.sum(a * (Y - Yguess))
    b2_gradient = (-2 / N) * np.sum(b * (Y - Yguess))
    b3_gradient = (-2 / N) * np.sum(c * (Y - Yguess))
    b4_gradient = (-2 / N) * np.sum(d * (Y - Yguess))
    b0 -= learning_rate * b0_gradient
    b1 -= learning_rate * b1_gradient
    b2 -= learning_rate * b2_gradient
    b3 -= learning_rate * b3_gradient
    b4 -= learning_rate * b4_gradient
Y_predicted = b0 + b1 * a + b2 * b + b3 * c + b4 * d
plt.plot(X, Y_predicted, color='blue')
plt.show()