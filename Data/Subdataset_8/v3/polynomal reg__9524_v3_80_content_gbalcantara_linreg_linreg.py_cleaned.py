import numpy as np
import matplotlib.pyplot as plt
import sys
def gradient_descent(x, y, theta, learning_rate, num_samples, num_iterations):
    x_transpose = x.transpose()
    convergence_flag = 1
    while convergence_flag != 0:
        for _ in range(num_iterations):
            hypothesis = np.dot(x, theta)
            loss = hypothesis - y
            cost = np.sum(loss ** 2) / (2 * num_samples)
            gradient = np.dot(x_transpose, loss) / num_samples
            theta -= learning_rate * gradient
            convergence_flag = round(cost, 2)
        learning_rate += 0.00001
    return theta, learning_rate
if __name__ == "__main__":
    x2 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    x1 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    x0 = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    x = np.array([[1, num, num ** 2] for num in range(-10, 10)])
    y = np.array([((x2) * num ** 2) + ((x1) * num) + x0 for num in range(-10, 10)])
    num_samples, num_features = np.shape(x)
    num_iterations = 5000
    learning_rate = 0.000001
    theta = np.ones(num_features)
    noise = np.random.uniform(-0.1, 0.1, y.shape)
    y += noise
    theta, learning_rate = gradient_descent(x, y, theta, learning_rate, num_samples, num_iterations)
    print('Learning rate =', learning_rate)
    print('x2 =', theta[2])
    print('x1 =', theta[1])
    print('x0 =', theta[0])
    xx = np.linspace(-10, 10, 20)
    yy = theta[2] * xx ** 2 + theta[1] * xx + theta[0]
    plt.plot(x[:, 1], y, 'kx', xx, yy)
    plt.show()