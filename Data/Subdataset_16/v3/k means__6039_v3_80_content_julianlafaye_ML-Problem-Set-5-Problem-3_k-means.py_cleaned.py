import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as metric
def fonk1(b16, b17):
    b1 = b16.shape[1]
    b2 = np.zeros((b17, b1))
    for i in range(b1):
        b3 = np.min(b16[:, i])
        b4 = np.max(b16[:, i]) - b3
        b2[:, i] = b3 + b4 * np.random.rand(b17)
    return b2
def fonk2(b16, b17):
    b5 = b16.shape[0]
    b6 = np.zeros((b5, 2))
    b2 = fonk1(b16, b17)
    b7 = b2.copy()
    b8 = True
    a1 = 0
    while b8:
        b8 = False
        for i in range(b5):
            b9 = [metric.euclidean(b16[i, :], centroid) for centroid in b2]
            b10 = np.argmin(b9)
            if b6[i, 0] != b10:
                b8 = True
            b6[i, :] = b10, b9[b10] ** 2
        for cent in range(b17):
            b11 = b16[b6[:, 0] == cent]
            if b11.size > 0:
                b2[cent, :] = np.mean(b11, b12 = 0)
        a1 += 1
        print(f'Iteration {a1}')
    return b2, b6, a1, b7
def fonk3(b16):
    plt.scatter(b16[:, 0], b16[:, 1])
    plt.title('Dataset')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
def fonk4(b16, b2, b6):
    plt.scatter(b16[:, 0], b16[:, 1], b13 = b6[:, 0])
    plt.scatter(b2[:, 0], b2[:, 1], b14 = 'x', color='red')
    plt.title('Clustered Data with Centroids')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
def fonk5():
    print('b17-Means Clustering Algorithm in Python')
    b15 = 'kmeans_data.csv'
    b16 = np.genfromtxt(b15, delimiter=',')
    fonk3(b16)
    b17 = int(input("Number of Centroids: "))
    b2, b6, a1, b7 = fonk2(b16, b17)
    print('Number of a1:', a1)
    print('\nFinal b2:\n', b2)
    print('\nInitial b2:\n', b7)
    fonk4(b16, b2, b6)
if b18 = = "__main__":
    fonk5()