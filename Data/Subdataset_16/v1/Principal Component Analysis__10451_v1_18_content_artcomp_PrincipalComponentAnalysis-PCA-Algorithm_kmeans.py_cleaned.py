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
def fonk3(center, points):
    b4 = []
    for i in range(len(center)):
        a1 = 0
        for j in points[i]:
            a1 += fonk2(center[i], j)
        b4.append(a1)
    b5 = sum(b4) / len(center)
    b3 = statistics.stdev(b4)
    return b3 / b5
def fonk4(Y, centers):
    b6 = np.array(Y)
    plt.scatter(b6[:,0], b6[:,1], b7 = 50, cmap='viridis')
    plt.scatter(centers[:,0], centers[:,1], b8 = 'black', b7=200, alpha=0.5)
    plt.title('NÃºmero ideal de clusters')
    plt.xlabel('CPU')
    plt.ylabel('Disks (I/O)')
    plt.show()
def fonk5(b6, a2, a3):
    b9 = KMeans(n_clusters=a2, random_state=0).fit(b6)
    b9.predict(b6)
    if a3 != 0:
        fonk4(b6, b9.cluster_centers_)
    b10 = [ [] for _ in range(a2) ]
    for i in range(len(b6)):
        b10[b9.labels_[i]].append(b6[i])
    b11 = fonk3(b9.cluster_centers_, b10)
    b12 = fonk1(b9.cluster_centers_)
    b13 = b11 / b12
    return b13
if b14 = = "__main__":
    b6 = np.array([[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6], [9.0, 11.0], [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]])
    a2 = 3
    a3 = 1
    b13 = fonk5(b6, a2, a3)
    print("Beta CV:", b13)