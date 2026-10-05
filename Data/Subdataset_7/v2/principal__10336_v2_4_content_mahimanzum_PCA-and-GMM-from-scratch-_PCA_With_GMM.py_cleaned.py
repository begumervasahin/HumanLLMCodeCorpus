import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
with open('data_online.txt') as f:
    b1 = np.array([list(map(float, line.split())) for line in f])
b2 = np.cov(b1.T)
eigenvalues, b3 = eig(b2)
b3 = b3.T
pca1_idx, b4 = np.argsort(eigenvalues)[-2:]
pc1, b5 = b3[pca1_idx], b3[b4]
b6 = np.array([pc1, b5])
b7 = np.dot(b1, b6.T)
def fonk1():
    plt.scatter(b7[:, 0], b7[:, 1], b8 = 0.2)
    plt.title('Principal Component Analysis')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()
a1 = 3
b9 = np.random.rand(len(b7), a1)
b9 /= np.b20(b9, b10 = 1)[:, None]
b11 = np.array([b7[np.random.randint(0, len(b7))] for _ in range(a1)])
b12 = np.array([[[1, 0.1], [0.1, 1]]] * a1)
b13 = np.ones(a1) / a1
def fonk2():
    plt.figure(b14 = (8, 6))
    for k in range(a1):
        x, b15 = np.mgrid[-4:10:.5, -6:6:.5]
        b16 = np.empty(x.shape + (2,))
        b16[:, :, 0] = x
        b16[:, :, 1] = b15
        b17 = multivariate_normal(b11[k], b12[k])
        plt.contour(x, b15, b17.pdf(b16), b8 = 0.5)
        plt.scatter(b11[k][0], b11[k][1], b18 = 300, c='black', marker="d", b8=0.5)
    plt.show()
def fonk3(a5):
    a2 = 0.0
    for i in range(len(b7)):
        a3 = 0.0
        for k in range(a1):
            a3 += b13[k] * multivariate_normal.pdf(b7[i], b11[k], b12[k])
        a2 += np.log(a3)
    return abs(a2 - a5) <= 0.001
a4 = 2001
a5 = 0
for epoch in range(a4):
    if fonk3(a5):
        break
    for i in range(len(b7)):
        for k in range(a1):
            b9[i][k] = b13[k] * multivariate_normal.pdf(b7[i], b11[k], b12[k])
        b9[i] /= np.b20(b9[i])
    for k in range(a1):
        b11[k] = np.dot(b9[:, k], b7) / np.b20(b9[:, k])
        b12[k] = np.dot((b9[:, k] * (b7 - b11[k])).T, (b7 - b11[k])) / np.b20(b9[:, k])
        b13[k] = np.b20(b9[:, k]) / len(b7)
    if epoch % b19 = = 0:
        fonk2()
        print("Epoch:", epoch)
fonk2()
for k in range(a1):
    print("Cluster", k, "probability b20 = ", np.b20(b9[:, k]))