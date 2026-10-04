from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import statistics
from itertools import combinations
def inter_cluster_distance(centers):
    distances = [distance.euclidean(p1, p2) for p1, p2 in combinations(centers, 2)]
    avg_distance = np.mean(distances)
    st_dev = statistics.stdev(distances)
    return st_dev / avg_distance
def euclidean_distance(point_a, point_b):
    return distance.euclidean(point_a, point_b)
def intra_cluster_distance(centers, clusters):
    sum_distances = []
    for i, center in enumerate(centers):
        total_distance = sum(euclidean_distance(center, point) for point in clusters[i])
        sum_distances.append(total_distance)
    avg_intra_distance = np.mean(sum_distances)
    st_dev = statistics.stdev(sum_distances)
    return st_dev / avg_intra_distance
def plot_data(points, centers):
    points = np.array(points)
    plt.scatter(points[:, 0], points[:, 1], s=50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.title('NÃºmero ideal de clusters')
    plt.xlabel('CPU')
    plt.ylabel('Disks (I/O)')
    plt.show()
def clusterization(data, num_clusters, plot):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(data)
    labels = kmeans.predict(data)
    if plot:
        plot_data(data, kmeans.cluster_centers_)
    clusters = [[] for _ in range(num_clusters)]
    for point, label in zip(data, labels):
        clusters[label].append(point)
    cv_intra_cluster = intra_cluster_distance(kmeans.cluster_centers_, clusters)
    cv_inter_cluster = inter_cluster_distance(kmeans.cluster_centers_)
    beta_cv = cv_intra_cluster / cv_inter_cluster
    return beta_cv
if __name__ == "__main__":
    data = np.array([
        [1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6],
        [9.0, 11.0], [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]
    ])
    num_clusters = 3
    plot = True
    beta_cv = clusterization(data, num_clusters, plot)
    print("Beta CV:", beta_cv)