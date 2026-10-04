from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import statistics
from itertools import combinations
def inter_cluster_distance(centers):
    distances = [distance.euclidean(p1, p2) for p1, p2 in combinations(centers, 2)]
    avg_distance = np.mean(distances)
    st_dev = np.std(distances)
    return st_dev / avg_distance
def euclidean_distance(point_a, point_b):
    return distance.euclidean(point_a, point_b)
def intra_cluster_distance(centers, points):
    sum_distances = []
    for i, center in enumerate(centers):
        distances = [euclidean_distance(center, point) for point in points[i]]
        sum_distances.append(sum(distances))
    avg_intra_distance = np.mean(sum_distances)
    st_dev = np.std(sum_distances)
    return st_dev / avg_intra_distance
def plot_data(points, centers):
    points = np.array(points)
    plt.scatter(points[:, 0], points[:, 1], s=50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.title('Ideal Number of Clusters')
    plt.xlabel('CPU')
    plt.ylabel('Disks (I/O)')
    plt.show()
def clusterization(X, num_clusters, plot=False):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(X)
    if plot:
        plot_data(X, kmeans.cluster_centers_)
    clusters = [[] for _ in range(num_clusters)]
    for point, label in zip(X, kmeans.labels_):
        clusters[label].append(point)
    cv_intra_cluster = intra_cluster_distance(kmeans.cluster_centers_, clusters)
    cv_inter_cluster = inter_cluster_distance(kmeans.cluster_centers_)
    beta_cv = cv_intra_cluster / cv_inter_cluster
    return beta_cv