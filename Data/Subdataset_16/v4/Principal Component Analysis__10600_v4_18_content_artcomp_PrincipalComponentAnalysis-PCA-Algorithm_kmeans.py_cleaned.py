from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import statistics
from itertools import combinations
def fonk1(centers):
    b1 = [distance.euclidean(p1, p2) for p1, p2 in combinations(centers, 2)]
    b2 = sum(b1) / len(b1)
    b3 = statistics.stdev(b1)
    return b3 / b2
def fonk2(point_a, point_b):
    return distance.euclidean(point_a, point_b)
def fonk3(centers, points):
    b4 = []
    for i in range(len(centers)):
        b5 = sum(fonk2(centers[i], point) for point in points[i])
        b4.append(b5)
    b6 = sum(b4) / len(centers)
    b3 = statistics.stdev(b4)
    return b3 / b6
def fonk4(points, centers):
    b7 = np.array(points)
    plt.scatter(b7[:, 0], b7[:, 1], b8 = 50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], b9 = 'black', b8=200, alpha=0.5)
    plt.title('Ideal Number of Clusters')
    plt.xlabel('CPU')
    plt.ylabel('Disks (I/O)')
    plt.show()
def fonk5(b7, num_clusters, plot):
    b10 = KMeans(n_clusters=num_clusters, random_state=0).fit(b7)
    if plot:
        fonk4(b7, b10.cluster_centers_)
    b11 = [[] for _ in range(num_clusters)]
    for i, label in enumerate(b10.labels_):
        b11[label].append(b7[i])
    b12 = fonk3(b10.cluster_centers_, b11)
    b13 = fonk1(b10.cluster_centers_)
    b14 = b12 / b13
    return b14