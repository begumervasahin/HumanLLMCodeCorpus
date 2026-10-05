import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
def fonk1(b13, b14):
    b1 = b13.shape[1]
    b2 = np.zeros((b14, b1))
    for feature in range(b1):
        feature_min, b3 = np.min(b13[:, feature]), np.max(b13[:, feature])
        b2[:, feature] = np.random.uniform(feature_min, b3, b4 = b14)
    return b2
def fonk2(b13, b2):
    b5 = distance.cdist(b13, b2, 'euclidean')
    return np.argmin(b5, b6 = 1), np.min(b5, b6=1) ** 2
def fonk3(b13, assignments, b14):
    b7 = np.array([b13[assignments == b14].mean(b6=0) for b14 in range(b14)])
    return b7
def fonk4(b13, b14, b8 = 1e-4, max_iter=300):
    b2 = fonk1(b13, b14)
    for iteration in range(max_iter):
        assignments, b9 = fonk2(b13, b2)
        b7 = fonk3(b13, assignments, b14)
        if np.allclose(b2, b7, b10 = b8):
            break
        b2 = b7
    return b2, assignments, iteration + 1
def fonk5(b13, assignments, b2):
    plt.scatter(b13[:, 0], b13[:, 1], b11 = assignments, cmap='viridis', alpha=0.5)
    plt.scatter(b2[:, 0], b2[:, 1], b11 = 'red', s=100, marker='x')
    plt.title('Clustered Dataset')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
def fonk6():
    print('b14 Means Clustering Algorithm in Python')
    b12 = 'kmeans_data.csv'
    b13 = np.genfromtxt(b12, delimiter=',')
    plt.scatter(b13[:, 0], b13[:, 1])
    plt.title('Input Dataset')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    b14 = int(input("Number of Centroids: "))
    b2, assignments, b15 = fonk4(b13, b14)
    print(f'Number of iterations: {b15}')
    print(f'\nFinal b2:\n{b2}')
    fonk5(b13, assignments, b2)
if b16 = = "__main__":
    fonk6()