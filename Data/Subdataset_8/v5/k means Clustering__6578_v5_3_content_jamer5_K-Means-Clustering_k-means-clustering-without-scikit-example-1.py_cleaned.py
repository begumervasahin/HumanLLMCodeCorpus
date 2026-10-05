import numpy as np
import os
def euclidean_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid) ** 2))
def assign_cluster_label(distances, data_point, centroids):
    closest_centroid_index = min(distances, key=distances.get)
    return [closest_centroid_index, data_point, centroids[closest_centroid_index]]
def compute_new_centroids(cluster_label, centroids):
    return np.array(cluster_label + centroids) / 2
def k_means(data_points, centroids, total_iterations):
    cluster_labels = []
    num_points = len(data_points)
    num_centroids = len(centroids)
    for iteration in range(total_iterations):
        for point_index in range(num_points):
            distances = {}
            for centroid_index in range(num_centroids):
                distances[centroid_index] = euclidean_distance(data_points[point_index], centroids[centroid_index])
            label = assign_cluster_label(distances, data_points[point_index], centroids)
            centroids[label[0]] = compute_new_centroids(label[1], centroids[label[0]])
            if iteration == total_iterations - 1:
                cluster_labels.append(label)
    return [cluster_labels, centroids]
def print_cluster_data(result):
    print("Result of k-Means Clustering: \n")
    for data in result[0]:
        print("Data point: {}".format(data[1]))
        print("Cluster number: {} \n".format(data[0]))
    print("Last centroids position: \n {}".format(result[1]))
def initialize_centroids():
    centroids = np.array([[5.0, 0.0], [45.0, 70.0], [50.0, 90.0]])
    return centroids
if __name__ == "__main__":
    filename = os.path.dirname(__file__) + "\data-example-1.csv"
    data_points = np.genfromtxt(filename, delimiter=",")
    centroids = initialize_centroids()
    total_iterations = 100
    [cluster_labels, new_centroids] = k_means(data_points, centroids, total_iterations)
    print_cluster_data([cluster_labels, new_centroids])
    print()