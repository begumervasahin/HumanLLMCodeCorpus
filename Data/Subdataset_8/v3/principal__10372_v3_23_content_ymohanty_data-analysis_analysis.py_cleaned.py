import numpy as np
import scipy.spatial.distance as norms
import scipy.cluster.vq as vq
import sys
import random
import data
__author__ = "Yashaswi Mohanty"
__email__ = "ymohanty@colby.edu"
__version__ = "2/21/2016"
def initialize_centers(data_matrix, num_clusters, categories=None):
    cluster_centers = []
    num_samples = data_matrix.shape[0]
    if categories is None:
        for _ in range(num_clusters):
            cluster_centers.append(data_matrix[np.random.randint(0, num_samples)].tolist()[0])
    else:
        if num_clusters != max(categories) + 1:
            print("The highest category label and specified clusters should be the same")
            return
        for i in range(num_clusters):
            cluster_sum = np.zeros(data_matrix.shape[1])
            num_elements = 0
            for j in range(len(categories)):
                if categories[j] == i:
                    cluster_sum = np.add(cluster_sum, data_matrix[j].tolist()[0])
                    num_elements += 1
            cluster_mean = 1 / float(num_elements) * cluster_sum
            cluster_centers.append(cluster_mean)
    return np.matrix(cluster_centers)
def classify_data(data_matrix, cluster_centers, distance_metric):
    classified_data = []
    distances = []
    max_distance = sys.maxsize
    for data_point in data_matrix:
        closest_center_index = 0
        for i, center in enumerate(cluster_centers.tolist()):
            norm_matrix = np.vstack((data_point, center))
            distance = norms.pdist(norm_matrix, distance_metric)[0]
            if distance < max_distance:
                max_distance = distance
                closest_center_index = i
        classified_data.append([closest_center_index])
        distances.append([max_distance])
        max_distance = sys.maxsize
    return np.matrix(classified_data), np.matrix(distances)
def kmeans_algorithm(data_matrix, initial_centers, distance_metric):
    MIN_CHANGE = 1e-7
    MAX_ITERATIONS = 100
    num_clusters = initial_centers.shape[0]
    num_samples = data_matrix.shape[0]
    for _ in range(MAX_ITERATIONS):
        classified_data, _ = classify_data(data_matrix, initial_centers, distance_metric)
        new_centers = np.zeros_like(initial_centers)
        cluster_counts = np.zeros((num_clusters, 1))
        for j in range(num_samples):
            cluster_index = classified_data[j, 0]
            new_centers[cluster_index, :] += data_matrix[j, :]
            cluster_counts[cluster_index, 0] += 1.0
        for j in range(num_clusters):
            if cluster_counts[j, 0] > 0.0:
                new_centers[j, :] /= cluster_counts[j, 0]
            else:
                new_centers[j, :] = data_matrix[random.randint(0, num_samples), :]
        difference = np.sum(np.square(initial_centers - new_centers))
        initial_centers = new_centers
        if difference < MIN_CHANGE:
            break
    classified_data, errors = classify_data(data_matrix, initial_centers, distance_metric)
    return initial_centers, classified_data, errors
def kmeans(data_obj, headers, num_clusters, distance_metric, whiten=True, categories=None):
    try:
        data_matrix = data_obj.get_data(headers)
    except AttributeError:
        data_matrix = data_obj
    if whiten:
        data_matrix = vq.whiten(data_matrix)
    initial_centers = initialize_centers(data_matrix, num_clusters, categories)
    cluster_centers, classified_data, errors = kmeans_algorithm(data_matrix, initial_centers, distance_metric)
    return cluster_centers, classified_data, errors
if __name__ == '__main__':
    data_obj = data.Data("clusterdata.csv")
    initial_centers = initialize_centers(data_obj, 3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2])
    print(classify_data(data_obj, initial_centers))