import numpy as np
import time
from sklearn.cluster import KMeans
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
def euclidean_distance(a, b):
    return np.linalg.norm(a - b)
def calculate_cost_matrix(clusters, train_labels):
    num_clusters = len(clusters)
    cost_matrix = np.zeros((num_clusters, num_clusters))
    for i, cluster_indices in enumerate(clusters):
        for index in cluster_indices:
            true_label = train_labels[0, index]
            cost_matrix[i, :] += 1
            cost_matrix[i, true_label - 1] -= 1
    return cost_matrix
def find_cluster_mean(num_clusters, num_runs, random_seed, test_data, train_labels):
    all_accuracies = []
    all_times = []
    np.random.seed(random_seed)
    for _ in range(num_runs):
        random_state = np.random.randint(0, 1000)
        clusters, time_taken = run_kmeans(num_clusters, random_state, test_data)
        cost_matrix = calculate_cost_matrix(clusters, train_labels)
        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        total_cost = cost_matrix[row_ind, col_ind].sum()
        accuracy = calculate_accuracy(num_clusters, total_cost)
        all_times.append(time_taken)
        all_accuracies.append(accuracy)
    average_time = np.mean(all_times)
    average_accuracy = np.mean(all_accuracies)
    return average_accuracy, average_time
def calculate_accuracy(num_clusters, total_cost):
    return (10 * num_clusters - total_cost) / (10 * num_clusters)
def run_kmeans(num_clusters, random_state, test_data):
    X = test_data.T
    start_time = time.time()
    kmeans = KMeans(n_clusters=num_clusters, random_state=random_state).fit(X)
    end_time = time.time()
    cluster_labels = kmeans.labels_
    clusters = [[] for _ in range(num_clusters)]
    for index, label in enumerate(cluster_labels):
        clusters[label].append(index)
    return clusters, end_time - start_time
def split_data():
    pass
data = split_data()
train_features, train_labels = data['train']
num_train_samples, num_train_features = train_features.shape
test_features, test_labels = data['test']
num_test_samples, num_test_features = test_features.shape
train_features = train_features / np.apply_along_axis(np.linalg.norm, 0, train_features)
test_features = test_features / np.apply_along_axis(np.linalg.norm, 0, test_features)
num_clusters = 32
num_runs = 1
random_seed = 10
accuracy, average_time = find_cluster_mean(num_clusters, num_runs, random_seed, train_features, train_labels)
print("Average Accuracy:", accuracy)
print("Average Time:", average_time)