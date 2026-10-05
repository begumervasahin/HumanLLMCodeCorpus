import math
import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("data_kmeans.txt")
num_observations, num_features = data.shape
def k_means_clustering(k):
    convergence_threshold = 1000000000
    cluster_assignments = np.zeros((num_observations, k))
    centroids = np.random.uniform(low=-10, high=10, size=(k, num_features))
    while True:
        for obs_idx in range(num_observations):
            for cluster_idx in range(k):
                squared_distance = 0
                for feature_idx in range(num_features):
                    squared_distance += (data[obs_idx][feature_idx] - centroids[cluster_idx][feature_idx])**2
                cluster_assignments[obs_idx][cluster_idx] = squared_distance
        cluster_labels = cluster_assignments.argmin(axis=1)
        total_loss = calculate_total_loss(cluster_assignments, cluster_labels)
        if total_loss <= convergence_threshold:
            break
        else:
            convergence_threshold = total_loss
            centroids = update_centroids(k, cluster_labels)
    return cluster_assignments, cluster_labels
def update_centroids(k, cluster_labels):
    new_centroids = np.zeros((k, num_features))
    for cluster_idx in range(k):
        cluster_sum = np.zeros(num_features)
        cluster_count = 0
        for obs_idx in range(num_observations):
            if cluster_labels[obs_idx] == cluster_idx:
                cluster_sum += data[obs_idx]
                cluster_count += 1
        if cluster_count > 0:
            new_centroids[cluster_idx] = cluster_sum / cluster_count
    return new_centroids
def calculate_total_loss(cluster_assignments, cluster_labels):
    total_loss = 0
    for obs_idx in range(num_observations):
        total_loss += cluster_assignments[obs_idx][cluster_labels[obs_idx]]
    return total_loss
def plot_clusters(cluster_labels):
    x_values = data[:, 0]
    y_values = data[:, 1]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    for i in range(len(data)):
        ax.scatter(x_values[i], y_values[i], color=colors[int(cluster_labels[i])])
    plt.show()
def main():
    cluster_assignments, cluster_labels = k_means_clustering(2)
    plot_clusters(cluster_labels)
if __name__ == '__main__':
    main()