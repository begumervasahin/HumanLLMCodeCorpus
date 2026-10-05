import numpy as np
import matplotlib.pyplot as plt
X = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
Y = np.array([4, 5, 6, 8, 11, 15, 20, 30, 50, 100])
plt.scatter(X, Y, s=50, color='red')
coefficients = {
    'b0': 0,
    'b1': -10,
    'b2': -50,
    'b3': -10,
    'b4': 50
}
N = len(Y)
learning_rate = 0.001
polynomial_features = {
    'a': X,
    'b': X ** 2,
    'c': X ** 3,
    'd': X ** 4
}
for _ in range(1000):
    Y_pred = sum(coefficients[key] * value for key, value in polynomial_features.items())
    gradients = {}
    for key in coefficients.keys():
        gradients[key] = (-2/N) * sum(polynomial_features[key] * (Y - Y_pred))
    for key in coefficients.keys():
        coefficients[key] -= gradients[key] * learning_rate
Y_predicted = sum(coefficients[key] * value for key, value in polynomial_features.items())
plt.plot(X, Y_predicted, color='blue')
plt.show()