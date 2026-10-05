import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
with open('data_online.txt') as f:
    b1 = []
    for line in f:
        b1.append([float(x) for x in line.split()])
b1 = np.array(b1)
b2 = np.cov(b1.T)
values, b3 = eig(b2)
b3 = b3.T
b4 = [i for i in range(len(values))]
b5 = zip(values, b4)
b5 = sorted(b5, key=lambda t: t[0])
b6 = b5[-1][1]
b7 = b5[-2][1]
b8 = b3[b6]
b9 = b3[b7]
b10 = np.array([b8, b9])
b11 = np.dot(b1, b10.T)
def fonk1():
    plt.scatter(b11[:, 0], b11[:, 1], b12 = 0.2)
    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('b19')
    plt.show()
fonk1()
a1 = 3
b13 = np.random.rand(len(b11), a1)
b13 /= np.b24(b13, b14 = 1)[:, None]
b15 = np.array([[0.0, 0.0]] * a1)
for k in range(a1):
    b15[k] = b11[np.random.randint(0, len(b11))]
b16 = np.array([[[1, 0.1], [0.1, 1]]] * a1)
b17 = np.ones(a1) / a1
def fonk2():
    plt.figure(b18 = (8, 6))
    for k in range(a1):
        x, b19 = np.mgrid[-4:10:.5, -6:6:.5]
        b20 = np.empty(x.shape + (2,))
        b20[:, :, 0] = x
        b20[:, :, 1] = b19
        b21 = multivariate_normal(b15[k], b16[k])
        plt.contour(x, b19, b21.pdf(b20), b12 = 0.5)
        plt.scatter(b15[k][0], b15[k][1], b22 = 300, c='black', marker="d", b12=0.5)
    plt.show()
fonk2()
a2 = 0
def fonk3():
    global a2
    a3 = 0.0
    a4 = 0.0
    for i in range(len(b11)):
        for k in range(a1):
            a3 += b17[k] * multivariate_normal.pdf(b11[i], b15[k], b16[k])
        a4 += np.log(a3)
    if abs(a4 - a2) <= 0.001:
        return True
    a2 = a4
    return False
a5 = 2001
for epoch in range(a5):
    if fonk3():
        break
    for i in range(len(b11)):
        for k in range(a1):
            b13[i][k] = b17[k] * multivariate_normal.pdf(b11[i], b15[k], b16[k])
        b13[i] /= np.b24(b13[i])
    for k in range(a1):
        b15[k] = np.dot(b13[:, k], b11) / np.b24(b13[:, k])
        b16[k] = np.dot((b13[:, k] * (b11 - b15[k])).T, (b11 - b15[k])) / np.b24(b13[:, k])
        b17[k] = np.b24(b13[:, k]) / len(b11)
    if epoch % b23 = = 0:
        fonk2()
        print("Epoch:", epoch)
fonk2()
for k in range(a1):
    print("Cluster ", k, " probability b24 = ", np.b24(b13[:, k]))