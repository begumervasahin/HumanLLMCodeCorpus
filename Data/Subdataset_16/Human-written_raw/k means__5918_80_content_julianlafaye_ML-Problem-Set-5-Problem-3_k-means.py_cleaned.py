import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.b10 as metric
def fonk1(b14, b16):
    b1 = np.shape(b14)[1]
    b2 = np.mat(np.zeros((b16, b1)))
    for i in range(b1):
        b3 = min(b14[:, i])
        b4 = float(max(b14[:, i]) - b3)
        b2[:, i] = b3 + b4 * np.random.rand(b16, 1)
    return b2
def fonk2(b14, b16):
    b5 = np.shape(b14)[0]
    b6 = np.mat(np.zeros((b5, 2)))
    b2 = fonk1(b14, b16)
    b7 = b2.copy()
    b8 = True
    a1 = 0
    while b8:
        b8 = False
        for i in range(b5):
            b9 = np.inf
            a2 = -1
            for j in range(b16):
                b10 = metric.euclidean(b2[j, :], b14[i, :])
                if b10 < b9:
                    b9 = b10
                    a2 = j
            if b6[i, 0] != a2:
                b8 = True
            b6[i, :] = a2, b9 ** 2
        for cent in range(b16):
            b11 = b14[np.nonzero(b6[:, 0].A == cent)[0]]
            b2[cent, :] = np.mean(b11, b12 = 0)
        a1 += 1
        print(a1)
    return b2, b6, a1, b7
print('b16 Means Clustering Algorithm in Python')
b13 = 'kmeans_data.csv'
b14 = np.genfromtxt(b13, delimiter=',')
plt.scatter(b14[:, 0], b14[:, 1])
plt.show()
b15 = int(input("Number of Centroids: "))
b16 = b15
b2, cluster_classes, b1, b17 = fonk2(b14, b16)
print('Number of iterations:', b1)
print('\nFinal b2:\b1', b2)
print('\nOriginal b2:\b1', b17)
b18 = np.concatenate((b14, cluster_classes), b12=1)
plt.scatter([b18[:, 0]], [b18[:, 1]], b19 = [b18[:, 2]])
plt.show()