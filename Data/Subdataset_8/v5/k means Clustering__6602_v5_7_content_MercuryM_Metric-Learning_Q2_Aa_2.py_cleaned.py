import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from Split import split_data
from scipy.optimize import linear_sum_assignment
def euclidean_distance(a, b):
    return np.linalg.norm(a - b)
def calculate_cost_matrix(cluster_indices, true_labels):
    num_clusters = len(cluster_indices)
    cost_matrix = np.zeros((num_clusters, num_clusters))
    for i, cluster in enumerate(cluster_indices):
        for j in range(len(cluster)):
            point_index = cluster[j]
            true_label = true_labels[0, point_index]
            cost_matrix[i, :] += 1
            cost_matrix[i, true_label - 1] -= 1
    return cost_matrix
def find_cluster_statistics(k, num_iterations, random_seed, data):
    all_accuracies = []
    time_list = []
    np.random.seed(random_seed)
    for _ in range(num_iterations):
        random_state = np.random.randint(0, 1000)
        cluster_indices, elapsed_time = run_kmeans(k, random_state, data)
        cost_matrix = calculate_cost_matrix(cluster_indices, train_labels)
        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        total_cost = cost_matrix[row_ind, col_ind].sum()
        accuracy = calculate_accuracy(k, total_cost)
        time_list.append(elapsed_time)
        all_accuracies.append(accuracy)
    average_time = np.mean(time_list)
    average_accuracy = np.mean(all_accuracies)
    return average_accuracy, average_time
def calculate_accuracy(k, total_cost):
    return (10 * k - total_cost) / (10 * k)
def run_kmeans(k, random_state, data):
    X = data.T
    start_time = time.time()
    kmeans = KMeans(n_clusters=k, random_state=random_state).fit(X)
    elapsed_time = time.time() - start_time
    cluster_labels = kmeans.labels_
    cluster_indices = [[] for _ in range(k)]
    for i, label in enumerate(cluster_labels):
        cluster_indices[label].append(i)
    return cluster_indices, elapsed_time
data = split_data()
train_data, train_labels = data['train']
test_data, test_labels = data['test']
train_data_normalized = train_data / np.apply_along_axis(np.linalg.norm, 0, train_data)
test_data_normalized = test_data / np.apply_along_axis(np.linalg.norm, 0, test_data)
average_accuracy, average_time_taken = find_cluster_statistics(32, 1, 10, train_data_normalized)