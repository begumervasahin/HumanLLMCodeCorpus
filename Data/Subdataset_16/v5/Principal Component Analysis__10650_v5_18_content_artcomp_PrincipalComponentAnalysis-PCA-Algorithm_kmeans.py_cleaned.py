from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import statistics
from itertools import combinations
def fonk1(centers):
    b1 = [distance.euclidean(p1, p2) for p1, p2 in combinations(centers, 2)]
    b2 = np.mean(b1)
    b3 = np.std(b1)
    return b3 / b2
def fonk2(point_a, point_b):
    return distance.euclidean(point_a, point_b)
def fonk3(centers, b6):
    b4 = []
    for i, center in enumerate(centers):
        b1 = [fonk2(center, point) for point in b6[i]]
        b4.append(sum(b1))
    b5 = np.mean(b4)
    b3 = np.std(b4)
    return b3 / b5
def fonk4(b6, centers):
    b6 = np.array(b6)
    plt.scatter(b6[:, 0], b6[:, 1], b7 = 50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], b8 = 'black', b7=200, alpha=0.5)
    plt.title('Ideal Number of Clusters')
    plt.xlabel('CPU')
    plt.ylabel('Disks (I/O)')
    plt.show()
def fonk5(X, num_clusters, b9 = False):
    b10 = KMeans(n_clusters=num_clusters, random_state=0).fit(X)
    if b9:
        fonk4(X, b10.cluster_centers_)
    b11 = [[] for _ in range(num_clusters)]
    for point, label in zip(X, b10.labels_):
        b11[label].append(point)
    b12 = fonk3(b10.cluster_centers_, b11)
    b13 = fonk1(b10.cluster_centers_)
    b14 = b12 / b13
    return b14