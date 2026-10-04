import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.b10 as metric
def fonk1(b14, b15):
    b1 = b14.shape[1]
    b2 = np.zeros((b15, b1))
    for i in range(b1):
        b3 = b14[:, i].min()
        b4 = float(b14[:, i].max() - b3)
        b2[:, i] = b3 + b4 * np.random.rand(b15)
    return b2
def fonk2(b14, b15):
    b5 = b14.shape[0]
    b6 = np.zeros((b5, 2))
    b2 = fonk1(b14, b15)
    b7 = b2.copy()
    b8 = True
    a1 = 0
    while b8:
        b8 = False
        for i in range(b5):
            b9 = float('inf')
            a2 = -1
            for j in range(b15):
                b10 = metric.euclidean(b2[j, :], b14[i, :])
                if b10 < b9:
                    b9 = b10
                    a2 = j
            if b6[i, 0] != a2:
                b8 = True
            b6[i, :] = a2, b9 ** 2
        for cent in range(b15):
            b11 = b14[np.where(b6[:, 0] == cent)[0]]
            if len(b11) > 0:
                b2[cent, :] = np.mean(b11, b12 = 0)
        a1 += 1
        print(f'Iteration {a1}')
    return b2, b6, a1, b7
def fonk3():
    print('b15-Means Clustering Algorithm in Python')
    b13 = 'kmeans_data.csv'
    b14 = np.genfromtxt(b13, delimiter=',')
    plt.scatter(b14[:, 0], b14[:, 1])
    plt.title('Dataset')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
    b15 = int(input("Number of Centroids: "))
    b2, b6, a1, b7 = fonk2(b14, b15)
    print('Number of a1:', a1)
    print('\nFinal b2:\n', b2)
    print('\nInitial b2:\n', b7)
    plt.scatter(b14[:, 0], b14[:, 1], b16 = b6[:, 0])
    plt.scatter(b2[:, 0], b2[:, 1], b17 = 'x', color='red')
    plt.title('Clustered Data with Centroids')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
if b18 = = "__main__":
    fonk3()