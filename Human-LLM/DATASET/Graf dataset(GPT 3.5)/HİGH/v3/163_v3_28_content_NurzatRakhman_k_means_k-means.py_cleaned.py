import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt("data_kmeans.txt")
num_observations, b2 = b1.shape
def fonk1(a1):
    b3 = np.random.uniform(low=-10, high=10, size=(a1, b2))
    return b3
def fonk2(b1, b3):
    b4 = np.zeros((num_observations, a1))
    for i in range(num_observations):
        for j in range(a1):
            b4[i, j] = np.linalg.norm(b1[i] - b3[j])
    return b4
def fonk3(b4):
    return np.argmin(b4, b5 = 1)
def fonk4(b1, b7, a1):
    b3 = np.zeros((a1, b2))
    for cluster_idx in range(a1):
        b6 = b1[b7 == cluster_idx]
        if len(b6) > 0:
            b3[cluster_idx] = np.mean(b6, b5 = 0)
    return b3
def fonk5(b1, a1):
    b3 = fonk1(a1)
    while True:
        b4 = fonk2(b1, b3)
        b7 = fonk3(b4)
        b8 = b3.copy()
        b3 = fonk4(b1, b7, a1)
        if np.allclose(b8, b3):
            break
    return b7
def fonk6(b1, b7):
    x_positions, b9 = b1[:, 0], b1[:, 1]
    b10 = plt.figure()
    b11 = b10.add_subplot(1, 1, 1)
    b12 = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    for i in range(len(b1)):
        b11.scatter(x_positions[i], b9[i], b13 = b12[int(b7[i])])
    plt.show()
def fonk7():
    a1 = 2
    b7 = fonk5(b1, a1)
    fonk6(b1, b7)
if b14 = = '__main__':
    fonk7()