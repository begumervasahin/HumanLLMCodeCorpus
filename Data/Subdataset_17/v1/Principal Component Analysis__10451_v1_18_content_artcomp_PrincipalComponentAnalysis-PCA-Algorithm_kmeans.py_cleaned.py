from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import statistics
from itertools import combinations
def interClusterDistance(centers):
    distances = [distance.euclidean(p1, p2) for p1, p2 in combinations(centers, 2)]
    avg_distance = sum(distances) / len(distances)
    st_dev = statistics.stdev(distances)
    return st_dev / avg_distance
def euclideanDistance(point_a, point_b):
    return distance.euclidean(point_a, point_b)
def intraClusterDistance(center, points):
    sum_distance_of_point_and_its_centroid = []
    for i in range(len(center)):
        result = 0
        for j in points[i]:
            result += euclideanDistance(center[i], j)
        sum_distance_of_point_and_its_centroid.append(result)
    average_intra_distance = sum(sum_distance_of_point_and_its_centroid) / len(center)
    st_dev = statistics.stdev(sum_distance_of_point_and_its_centroid)
    return st_dev / average_intra_distance
def plotData(Y, centers):
    X = np.array(Y)
    plt.scatter(X[:,0], X[:,1], s=50, cmap='viridis')
    plt.scatter(centers[:,0], centers[:,1], c='black', s=200, alpha=0.5)
    plt.title('NÃºmero ideal de clusters')
    plt.xlabel('CPU')
    plt.ylabel('Disks (I/O)')
    plt.show()
def clusterization(X, num_clusters, plot):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(X)
    kmeans.predict(X)
    if plot != 0:
        plotData(X, kmeans.cluster_centers_)
    l = [ [] for _ in range(num_clusters) ]
    for i in range(len(X)):
        l[kmeans.labels_[i]].append(X[i])
    cv_intra_cluster = intraClusterDistance(kmeans.cluster_centers_, l)
    cv_inter_cluster = interClusterDistance(kmeans.cluster_centers_)
    beta_cv = cv_intra_cluster / cv_inter_cluster
    return beta_cv
if __name__ == "__main__":
    X = np.array([[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6], [9.0, 11.0], [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]])
    num_clusters = 3
    plot = 1
    beta_cv = clusterization(X, num_clusters, plot)
    print("Beta CV:", beta_cv)