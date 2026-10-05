import numpy as np
import matplotlib.pyplot as plt
import sys
def gradient_descent(x, y, theta, epsilon, m, max_iterations):
    x_transpose = x.transpose()
    previous_cost = None
    while True:
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        cost = np.sum(loss ** 2) / (2 * m)
        if previous_cost is not None and round(cost, 2) == previous_cost:
            break
        previous_cost = round(cost, 2)
        gradient = np.dot(x_transpose, loss) / m
        theta = theta - epsilon * gradient
        epsilon += 0.00001
    return theta, epsilon
var1 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
var2 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
var3 = int(sys.argv[3]) if len(sys.argv) > 3 else 0
x = np.array([[1, num, num ** 2] for num in range(-10, 10)])
y = np.array([(var1 * num ** 2) + (var2 * num) + var3 for num in range(-10, 10)])
noise = np.random.uniform(-0.1, 0.1, y.shape)
y = y + noise
m, n = x.shape
max_iterations = 5000
epsilon = 0.000001
theta = np.ones(n)
theta, epsilon = gradient_descent(x, y, theta, epsilon, m, max_iterations)
print('Learning rate =', epsilon)
print('x2 =', theta[2])
print('x1 =', theta[1])
print('x0 =', theta[0])
xx = np.linspace(-10, 10, 20)
yy = (theta[2] * xx ** 2) + (theta[1] * xx) + theta[0]
plt.plot(x[:, 1], y, 'kx', xx, yy)
plt.show()