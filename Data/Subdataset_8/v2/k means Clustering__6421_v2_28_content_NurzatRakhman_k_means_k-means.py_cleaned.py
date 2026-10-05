import math
import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("data_kmeans.txt")
num_observations, num_features = data.shape
def form_clusters(num_clusters):
    threshold = 1000000000
    distances = np.zeros((num_observations, num_clusters))
    centroids = np.random.uniform(low=-10, high=10, size=(num_clusters, num_features))
    cluster_indices = np.zeros(num_observations)
    while True:
        for observation_idx in range(num_observations):
            for cluster_idx in range(num_clusters):
                distance_sum = 0
                for feature_idx in range(num_features):
                    distance_sum += math.pow((data[observation_idx][feature_idx] - centroids[cluster_idx][feature_idx]), 2)
                distances[observation_idx][cluster_idx] = distance_sum
            cluster_indices[observation_idx] = distances[observation_idx].argmin(axis=0)
        loss = calculate_loss(distances, cluster_indices)
        if loss <= threshold:
            break
        else:
            threshold = loss
            centroids = recompute_centroids(num_clusters, cluster_indices)
    return distances, cluster_indices
def recompute_centroids(num_clusters, cluster_indices):
    centroids = np.zeros((num_clusters, num_features))
    for cluster_idx in range(num_clusters):
        count = 0
        cluster_sum = np.zeros(num_features)
        for observation_idx in range(num_observations):
            if cluster_indices[observation_idx] == cluster_idx:
                for feature_idx in range(num_features):
                    cluster_sum[feature_idx] += data[observation_idx][feature_idx]
                count += 1
        for feature_idx in range(num_features):
            centroids[cluster_idx][feature_idx] = cluster_sum[feature_idx] / count
    return centroids
def calculate_loss(distances, cluster_indices):
    total_loss = 0
    for observation_idx in range(num_observations):
        total_loss += distances[observation_idx][int(cluster_indices[observation_idx])]
    return total_loss
def draw_plot(distances, cluster_indices):
    x_positions = data[:, 0]
    y_positions = data[:, 1]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    for i in range(len(data)):
        ax.scatter(x_positions[i], y_positions[i], color=colors[int(cluster_indices[i])])
    plt.show()
def main():
    distances, cluster_indices = form_clusters(2)
    draw_plot(distances, cluster_indices)
if __name__ == '__main__':
    main()