import numpy as np
import os
def compute_euclidean_distance(point, centroid):
    return np.linalg.norm(point - centroid)
def assign_label_cluster(distances):
    return min(distances, key=distances.get)
def compute_new_centroid(cluster_points):
    return np.mean(cluster_points, axis=0)
def k_means_clustering(data_points, centroids, total_iterations):
    k = len(centroids)
    for _ in range(total_iterations):
        clusters = {i: [] for i in range(k)}
        for data_point in data_points:
            distances = {i: compute_euclidean_distance(data_point, centroids[i]) for i in range(k)}
            nearest_centroid_index = assign_label_cluster(distances)
            clusters[nearest_centroid_index].append(data_point)
        for i in range(k):
            if clusters[i]:
                centroids[i] = compute_new_centroid(clusters[i])
    cluster_labels = []
    for data_point in data_points:
        distances = {i: compute_euclidean_distance(data_point, centroids[i]) for i in range(k)}
        nearest_centroid_index = assign_label_cluster(distances)
        cluster_labels.append((nearest_centroid_index, data_point, centroids[nearest_centroid_index]))
    return cluster_labels, centroids
def print_cluster_results(cluster_labels, centroids):
    print("Result of k-Means Clustering:\n")
    for label in cluster_labels:
        print("Data point:", label[1])
        print("Cluster number:", label[0], "\n")
    print("Last centroids position:\n", centroids)
def create_initial_centroids():
    return np.array([[5.0, 0.0], [45.0, 70.0], [50.0, 90.0]])
if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), "data-example-1.csv")
    data_points = np.genfromtxt(filename, delimiter=",")
    centroids = create_initial_centroids()
    total_iterations = 100
    cluster_labels, new_centroids = k_means_clustering(data_points, centroids, total_iterations)
    print_cluster_results(cluster_labels, new_centroids)