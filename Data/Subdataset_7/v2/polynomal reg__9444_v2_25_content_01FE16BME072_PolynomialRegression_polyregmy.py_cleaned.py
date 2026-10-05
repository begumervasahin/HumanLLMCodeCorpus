import numpy as np
import matplotlib.pyplot as plt
b1 = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
b2 = np.array([4, 5, 6, 8, 11, 15, 20, 30, 50, 100])
plt.scatter(b1, b2, b3 = 50, b17='red')
b0, b1, b2, b3, b4 = 0, -10, -50, -10, 50
b5 = len(b2)
a1 = 0.001
b6 = b1
b7 = np.array([0.01, 0.04, 0.09, 0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1])
b8 = np.array([0.001, 0.008, 0.027, 0.064, 0.125, 0.216, 0.343, 0.512, 0.729, 1])
b9 = np.array([0.00001, 0.0016, 0.0081, 0.0256, 0.0625, 0.1296, 0.2401, 0.4096, 0.6561, 1])
for _ in range(1000):
    b10 = b0 + b1 * b6 + b2 * b7 + b3 * b8 + b4 * b9
    b11 = (-2 / b5) * np.sum(b2 - b10)
    b12 = (-2 / b5) * np.sum(b6 * (b2 - b10))
    b13 = (-2 / b5) * np.sum(b7 * (b2 - b10))
    b14 = (-2 / b5) * np.sum(b8 * (b2 - b10))
    b15 = (-2 / b5) * np.sum(b9 * (b2 - b10))
    b0 -= a1 * b11
    b1 -= a1 * b12
    b2 -= a1 * b13
    b3 -= a1 * b14
    b4 -= a1 * b15
b16 = b0 + b1 * b6 + b2 * b7 + b3 * b8 + b4 * b9
plt.plot(b1, b16, b17 = 'blue')
plt.show()