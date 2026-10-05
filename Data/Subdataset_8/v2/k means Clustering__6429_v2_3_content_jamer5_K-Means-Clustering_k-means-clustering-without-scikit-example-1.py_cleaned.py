import numpy as np
import os
def compute_euclidean_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid) ** 2))
def assign_label_cluster(distance, data_point, centroids):
    index_of_minimum = min(distance, key=distance.get)
    return [index_of_minimum, data_point, centroids[index_of_minimum]]
def compute_new_centroids(cluster_label, centroids):
    return np.array(cluster_label + centroids) / 2
def iterate_k_means(data_points, centroids, total_iteration):
    cluster_label = []
    total_points = len(data_points)
    k = len(centroids)
    for iteration in range(total_iteration):
        for index_point in range(total_points):
            distance = {}
            for index_centroid in range(k):
                distance[index_centroid] = compute_euclidean_distance(data_points[index_point], centroids[index_centroid])
            label = assign_label_cluster(distance, data_points[index_point], centroids)
            centroids[label[0]] = compute_new_centroids(label[1], centroids[label[0]])
            if iteration == total_iteration - 1:
                cluster_label.append(label)
    return [cluster_label, centroids]
def print_label_data(result):
    print("Result of k-Means Clustering:\n")
    for data in result[0]:
        print("Data point:", data[1])
        print("Cluster number:", data[0], "\n")
    print("Last centroids position:\n", result[1])
def create_centroids():
    centroids = [[5.0, 0.0], [45.0, 70.0], [50.0, 90.0]]
    return np.array(centroids)
if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), "data-example-1.csv")
    data_points = np.genfromtxt(filename, delimiter=",")
    centroids = create_centroids()
    total_iteration = 100
    [cluster_label, new_centroids] = iterate_k_means(data_points, centroids, total_iteration)
    print_label_data([cluster_label, new_centroids])
    print()