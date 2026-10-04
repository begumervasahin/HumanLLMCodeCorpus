from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import statistics
from itertools import combinations
def fonk1(centers):
    b1 = [distance.euclidean(p1, p2) for p1, p2 in combinations(centers, 2)]
    b2 = np.mean(b1)
    b3 = statistics.stdev(b1)
    return b3 / b2
def fonk2(point_a, point_b):
    return distance.euclidean(point_a, point_b)
def fonk3(centers, b12):
    b4 = []
    for i, center in enumerate(centers):
        b5 = sum(fonk2(center, point) for point in b12[i])
        b4.append(b5)
    b6 = np.mean(b4)
    b3 = statistics.stdev(b4)
    return b3 / b6
def fonk4(b7, centers):
    b7 = np.array(b7)
    plt.scatter(b7[:, 0], b7[:, 1], b8 = 50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], b9 = 'black', b8=200, alpha=0.5)
    plt.title('NÃºmero ideal de b12')
    plt.xlabel('CPU')
    plt.ylabel('Disks (I/O)')
    plt.show()
def fonk5(b17, a1, b18):
    b10 = KMeans(n_clusters=a1, random_state=0).fit(b17)
    b11 = b10.predict(b17)
    if b18:
        fonk4(b17, b10.cluster_centers_)
    b12 = [[] for _ in range(a1)]
    for point, label in zip(b17, b11):
        b12[label].append(point)
    b13 = fonk3(b10.cluster_centers_, b12)
    b14 = fonk1(b10.cluster_centers_)
    b15 = b13 / b14
    return b15
if b16 = = "__main__":
    b17 = np.array([
        [1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6],
        [9.0, 11.0], [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]
    ])
    a1 = 3
    b18 = True
    b15 = fonk5(b17, a1, b18)
    print("Beta CV:", b15)