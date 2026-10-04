import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as metric
def fonk1(b15, b16):
    b1 = b15.shape[1]
    b2 = np.zeros((b16, b1))
    for i in range(b1):
        b3 = np.min(b15[:, i])
        b4 = np.ptp(b15[:, i])
        b2[:, i] = b3 + b4 * np.random.rand(b16)
    return np.matrix(b2)
def fonk2(b15, b2):
    b5 = b15.shape[0]
    b6 = np.zeros((b5, 2))
    for i in range(b5):
        b7 = np.inf
        for j in range(b2.shape[0]):
            b8 = metric.euclidean(b2[j, :], b15[i, :])
            if b8 < b7:
                b7 = b8
                b6[i, :] = j, b7 ** 2
    return np.matrix(b6)
def fonk3(b15, b6, b16):
    b2 = np.zeros((b16, b15.shape[1]))
    for cent in range(b16):
        b9 = b15[np.where(b6[:, 0].A == cent)[0]]
        b2[cent, :] = np.mean(b9, b10 = 0) if b9.size else b2[cent, :]
    return np.matrix(b2)
def fonk4(b15, b16):
    b2 = fonk1(b15, b16)
    b11 = b2.copy()
    b6 = np.matrix(np.zeros((b15.shape[0], 2)))
    b12 = True
    a1 = 0
    while b12:
        a1 += 1
        b6 = fonk2(b15, b2)
        b13 = fonk3(b15, b6, b16)
        if np.allclose(b2, b13):
            b12 = False
        b2 = b13
        print(f"Iteration {a1}")
    return b2, b6, a1, b11
def fonk5(b15, title, xlabel, ylabel):
    plt.scatter(b15[:, 0], b15[:, 1])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
def fonk6():
    print('b16-Means Clustering Algorithm in Python')
    b14 = 'kmeans_data.csv'
    b15 = np.genfromtxt(b14, delimiter=',')
    fonk5(b15, 'Dataset', 'Feature 1', 'Feature 2')
    b16 = int(input("Number of Centroids: "))
    b2, b6, a1, b11 = fonk4(b15, b16)
    print('Number of a1:', a1)
    print('\nFinal b2:\n', b2)
    print('\nInitial b2:\n', b11)
    b17 = np.hstack((b15, b6))
    plt.scatter(b17[:, 0], b17[:, 1], b18 = b17[:, 2])
    plt.title('Clustered Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
if b19 = = "__main__":
    fonk6()