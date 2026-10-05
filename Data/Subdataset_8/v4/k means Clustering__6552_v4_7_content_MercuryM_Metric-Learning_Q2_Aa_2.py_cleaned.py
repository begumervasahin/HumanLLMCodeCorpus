import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from Split import split_data
from scipy.optimize import linear_sum_assignment
def euclidean_distance(a, b):
    return np.linalg.norm(a - b)
def cost_matrix(record):
    k = len(record)
    cost = np.full((k, k), 0)
    for i in range(k):
        cluster = record[i]
        for j in range(len(cluster)):
            m = cluster[j]
            n = train_labels[0, m]
            cost[i, :] += 1
            cost[i, n - 1] -= 1
    return cost
def find_cluster_mean(k, times, random_num, test_data):
    all_accuracy = []
    time_list = []
    np.random.seed(random_num)
    for i in range(times):
        r = np.random.randint(0, 1000)
        labels, time_taken = k_means(k, r, test_data)
        cost = cost_matrix(labels)
        row_ind, col_ind = linear_sum_assignment(cost)
        cost_sum = cost[row_ind, col_ind].sum()
        accuracy = calculate_accuracy(k, cost_sum)
        time_list.append(time_taken)
        all_accuracy.append(accuracy)
    average_time = np.mean(time_list)
    average_accuracy = np.mean(all_accuracy)
    return average_accuracy, average_time
def calculate_accuracy(k, cost_sum):
    return (10 * k - cost_sum) / (10 * k)
def k_means(k, state, test_data):
    X = test_data.T
    start_time = time.time()
    kmeans = KMeans(n_clusters=k, random_state=state).fit(X)
    time_taken = time.time() - start_time
    cluster_labels = kmeans.labels_
    labels = []
    for i in range(k):
        temp = []
        for j in range(len(cluster_labels)):
            if i == cluster_labels[j]:
                temp.append(j)
        labels.append(temp)
    return labels, time_taken
data = split_data()
train_data, train_labels = data['train']
test_data, test_labels = data['test']
train_data = train_data / np.apply_along_axis(np.linalg.norm, 0, train_data)
test_data = test_data / np.apply_along_axis(np.linalg.norm, 0, test_data)
accuracy, time_taken = find_cluster_mean(32, 1, 10, train_data)