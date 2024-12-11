import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
def fonk1(file_path):
    with open(file_path) as f:
        return np.array([list(map(float, line.split())) for line in f])
def fonk2(b21):
    b1 = np.cov(b21.T)
    eigenvalues, b2 = eig(b1)
    b3 = np.argsort(eigenvalues)
    pca1_idx, b4 = b3[-2:]
    pc1, b5 = b2[pca1_idx], b2[b4]
    b6 = np.array([pc1, b5])
    return np.dot(b21, b6.T)
def fonk3(b21):
    plt.scatter(b21[:, 0], b21[:, 1], b7 = 0.2)
    plt.title('Principal Component Analysis')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()
def fonk4(b21, b23):
    b8 = np.random.rand(len(b21), b23)
    b8 /= np.b20(b8, b9 = 1)[:, None]
    b10 = np.array([b21[np.random.randint(0, len(b21))] for _ in range(b23)])
    b11 = np.array([[[1, 0.1], [0.1, 1]]] * b23)
    b12 = np.ones(b23) / b23
    return b8, b10, b11, b12
def fonk5(b10, b11):
    plt.figure(b13 = (8, 6))
    for k in range(len(b10)):
        x, b14 = np.mgrid[-4:10:.5, -6:6:.5]
        b15 = np.empty(x.shape + (2,))
        b15[:, :, 0] = x
        b15[:, :, 1] = b14
        b16 = multivariate_normal(b10[k], b11[k])
        plt.contour(x, b14, b16.pdf(b15), b7 = 0.5)
        plt.scatter(b10[k][0], b10[k][1], b17 = 300, c='black', marker="d", b7=0.5)
    plt.show()
def fonk6(a3, b21, b10, b11, b12):
    a1 = 0.0
    for i in range(len(b21)):
        b18 = b20(b12[k] * multivariate_normal.pdf(b21[i], b10[k], b11[k]) for k in range(len(b10)))
        a1 += np.log(b18)
    return abs(a1 - a3) <= 0.001
def fonk7(b21, b23):
    b8, b10, b11, b12 = fonk4(b21, b23)
    a2 = 2001
    a3 = 0
    for epoch in range(a2):
        if fonk6(a3, b21, b10, b11, b12):
            break
        for i in range(len(b21)):
            for k in range(b23):
                b8[i][k] = b12[k] * multivariate_normal.pdf(b21[i], b10[k], b11[k])
            b8[i] /= np.b20(b8[i])
        for k in range(b23):
            b10[k] = np.dot(b8[:, k], b21) / np.b20(b8[:, k])
            b11[k] = np.dot((b8[:, k] * (b21 - b10[k])).T, (b21 - b10[k])) / np.b20(b8[:, k])
            b12[k] = np.b20(b8[:, k]) / len(b21)
        if epoch % b19 = = 0:
            fonk5(b10, b11)
            print("Epoch:", epoch)
    fonk5(b10, b11)
    for k in range(b23):
        print("Cluster", k, "probability b20 = ", np.b20(b8[:, k]))
b21 = fonk1('data_online.txt')
b22 = fonk2(b21)
fonk3(b22)
fonk7(b22, b23 = 3)