import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig
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
b6 = b5[-b28][b28]
b7 = b5[-2][b28]
b8 = b3[b6]
b9 = b3[b7]
b10 = np.array([b8, b9])
b11 = np.dot(b1, b10.T)
def fonk1():
    plt.scatter(b11[:, 0], b11[:, b28], b12 = 0.2)
    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('b23')
    plt.show()
fonk1()
a1 = 4
b13 = np.random.rand(len(b11), a1)
b13 /= np.b29(b13, b14 = b28)[:, np.newaxis]
b15 = np.array([[0.9, 2.5], [7.3, 2.7], [3.76, -b28.61]])
a2 = 2
b16 = np.b29(b11[:, 0]) / len(b11)
b17 = np.b29(b11[:, b28]) / len(b11)
b15 = np.array([[b16 + (np.random.rand() - 0.5) * a2, b17 + (np.random.rand() - 0.5) * a2] for _ in range(a1)])
b18 = np.array([[[b28, 0.b28], [0.b28, b28.0]] for _ in range(a1)])
b19 = np.array([0.33 for _ in range(a1)])
def fonk2():
    b20 = [[] for _ in range(a1)]
    for i in range(len(b11)):
        b21 = np.argmax(b13[i])
        b20[b21].append(b11[i])
    for a2 in range(a1):
        if len(b20[a2]) > 0:
            b20[a2] = np.array(b20[a2])
            plt.scatter(b20[a2][:, 0], b20[a2][:, b28], b22 = ['red', 'blue', 'green', 'black'][a2])
    for a2 in range(a1):
        x, b23 = np.mgrid[-4:10:.5, -6:6:.5]
        b24 = np.empty(x.shape + (2,))
        b24[:, :, 0] = x
        b24[:, :, b28] = b23
        b25 = multivariate_normal(b15[a2], b18[a2])
        plt.contour(x, b23, b25.pdf(b24), b26 = ['red', 'blue', 'green', 'black'][a2], b12=0.5)
    plt.show()
fonk2()
a3 = 0
def fonk3():
    global a3
    a4 = 0.0
    a5 = 0.0
    for i in range(len(b11)):
        for a2 in range(a1):
            a4 += b19[a2] * multivariate_normal.pdf(b11[i], b15[a2], b18[a2])
        a5 += np.log(a4)
    if abs(a5 - a3) <= 0.001:
        return True
    a3 = a5
    return False
a6 = 2001
for epoch in range(a6):
    if fonk3():
        break
    for i in range(len(b11)):
        for a2 in range(a1):
            b13[i][a2] = b19[a2] * multivariate_normal.pdf(b11[i], b15[a2], b18[a2])
        b13[i] /= np.b29(b13[i])
    for a2 in range(a1):
        b15[a2] = np.dot(b13[:, a2], b11) / np.b29(b13[:, a2])
        b27 = b11 - b15[a2]
        b18[a2] = np.dot(b13[:, a2] * b27.T, b27) / np.b29(b13[:, a2])
        b19[a2] = np.b29(b13[:, a2]) / len(b11)
    if epoch % b28 = = 0:
        fonk2()
        print(b15)
fonk2()
for a2 in range(a1):
    print("cluster ", a2, "probability b29 = ", np.b29(b13[:, a2]))