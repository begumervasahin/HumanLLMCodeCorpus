import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.b10 as metric
def fonk1(b14, k):
    b1 = np.shape(b14)[1]
    b2 = np.zeros((k, b1))
    for i in range(b1):
        b3 = min(b14[:, i])
        b4 = float(max(b14[:, i]) - b3)
        b2[:, i] = b3 + b4 * np.random.rand(k)
    return b2
def fonk2(b14, k):
    b5 = np.shape(b14)[0]
    b6 = np.zeros((b5, 2))
    b2 = fonk1(b14, k)
    b7 = b2.copy()
    b8 = False
    a1 = 0
    while not b8:
        b8 = True
        for i in range(b5):
            b9 = np.inf
            a2 = -1
            for j in range(k):
                b10 = metric.euclidean(b2[j, :], b14[i, :])
                if b10 < b9:
                    b9 = b10
                    a2 = j
            if b6[i, 0] != a2:
                b8 = False
            b6[i, :] = a2, b9 ** 2
        for cent in range(k):
            b11 = b14[np.nonzero(b6[:, 0] == cent)[0]]
            b2[cent, :] = np.mean(b11, b12 = 0)
        a1 += 1
    return b2, b6, a1, b7
print('k Means Clustering Algorithm in Python')
b13 = 'kmeans_data.csv'
b14 = np.genfromtxt(b13, delimiter=',')
plt.scatter(b14[:, 0], b14[:, 1])
plt.title('Input Dataset')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
b15 = int(input("Number of Centroids: "))
final_centroids, b6, a1, b7 = fonk2(b14, b15)
print('Number of iterations:', a1)
print('\nFinal b2:\n', final_centroids)
print('\nOriginal b2:\n', b7)
b16 = np.concatenate((b14, b6), b12=1)
plt.scatter(b16[:, 0], b16[:, 1], b17 = b16[:, 2])
plt.title('Clustered Dataset')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()