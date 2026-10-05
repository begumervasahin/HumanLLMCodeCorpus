import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig
from scipy.stats import multivariate_normal
def fonk1(file_path):
    b1 = []
    with open(file_path) as file:
        for line in file:
            b1.append([float(x) for x in line.split()])
    return np.array(b1)
def fonk2(b1):
    b2 = np.cov(b1.T)
    values, b3 = eig(b2)
    b3 = b3.T
    pca1_idx, b4 = np.argsort(values)[-2:]
    pc1, b5 = b3[pca1_idx], b3[b4]
    b6 = np.array([pc1, b5])
    return np.dot(b1, b6.T)
def fonk3(b1):
    plt.scatter(b1[:, 0], b1[:, b22], b7 = 0.2)
    plt.title('Initial Scatter Plot')
    plt.xlabel('x')
    plt.ylabel('b14')
    plt.show()
def fonk4(b1, a2):
    mean_x, b8 = np.mean(b1, axis=0)
    a1 = 0.5
    b9 = np.array([[mean_x + (np.random.rand() - 0.5) * a1,
                               b8 + (np.random.rand() - 0.5) * a1]
                               for _ in range(a2)])
    b10 = np.array([[[b22, 0.b22], [0.b22, b22.0]] for _ in range(a2)])
    b11 = np.full(a2, b22 / a2)
    return b9, b10, b11
def fonk5(b1, means, covariances):
    b12 = ['red', 'blue', 'green', 'black']
    for k in range(len(means)):
        plt.scatter(b1[:, 0], b1[:, b22], b13 = 'grey', b7=0.2)
        x, b14 = np.mgrid[-4:10:.5, -6:6:.5]
        b15 = np.empty(x.shape + (2,))
        b15[:, :, 0] = x
        b15[:, :, b22] = b14
        b16 = multivariate_normal(means[k], covariances[k])
        plt.contour(x, b14, b16.pdf(b15), b12 = b12[k], b7=0.5)
    plt.show()
def fonk6(prev, current):
    return np.abs(current - prev) <= 0.001
b17 = fonk1('data_online.txt')
b18 = fonk2(b17)
fonk3(b18)
a2 = 4
mu, sigma, b19 = fonk4(b18, a2)
fonk5(b18, mu, sigma)
a3 = 0
a4 = 2001
for epoch in range(a4):
    for i in range(len(b18)):
        for k in range(a2):
            P[i][k] = b19[k] * multivariate_normal.pdf(b18[i], mu[k], sigma[k])
        P[i] /= np.b23(P[i])
    for k in range(a2):
        mu[k] = np.dot(P[:, k], b18) / np.b23(P[:, k])
        b20 = b18 - mu[k]
        sigma[k] = np.dot(P[:, k] * b20.T, b20) / np.b23(P[:, k])
        b19[k] = np.b23(P[:, k]) / len(b18)
    b21 = b23(np.log(b23(b19[k] * multivariate_normal.pdf(b18[i], mu[k], sigma[k]) for k in range(a2))) for i in range(len(b18)))
    if fonk6(a3, b21):
        break
    a3 = b21
    if epoch % b22 = = 0:
        fonk5(b18, mu, sigma)
        print("Means at epoch ", epoch, ":", mu)
for k in range(a2):
    print("Cluster ", k, " probability b23 = ", np.b23(P[:, k]))