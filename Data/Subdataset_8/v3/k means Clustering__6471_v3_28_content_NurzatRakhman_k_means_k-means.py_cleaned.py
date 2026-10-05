import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("data_kmeans.txt")
num_observations, num_features = data.shape
def initialize_clusters(num_clusters):
    centroids = np.random.uniform(low=-10, high=10, size=(num_clusters, num_features))
    return centroids
def calculate_distances(data, centroids):
    distances = np.zeros((num_observations, num_clusters))
    for i in range(num_observations):
        for j in range(num_clusters):
            distances[i, j] = np.linalg.norm(data[i] - centroids[j])
    return distances
def assign_clusters(distances):
    return np.argmin(distances, axis=1)
def recompute_centroids(data, cluster_indices, num_clusters):
    centroids = np.zeros((num_clusters, num_features))
    for cluster_idx in range(num_clusters):
        cluster_points = data[cluster_indices == cluster_idx]
        if len(cluster_points) > 0:
            centroids[cluster_idx] = np.mean(cluster_points, axis=0)
    return centroids
def kmeans(data, num_clusters):
    centroids = initialize_clusters(num_clusters)
    while True:
        distances = calculate_distances(data, centroids)
        cluster_indices = assign_clusters(distances)
        old_centroids = centroids.copy()
        centroids = recompute_centroids(data, cluster_indices, num_clusters)
        if np.allclose(old_centroids, centroids):
            break
    return cluster_indices
def draw_plot(data, cluster_indices):
    x_positions, y_positions = data[:, 0], data[:, 1]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    for i in range(len(data)):
        ax.scatter(x_positions[i], y_positions[i], color=colors[int(cluster_indices[i])])
    plt.show()
def main():
    num_clusters = 2
    cluster_indices = kmeans(data, num_clusters)
    draw_plot(data, cluster_indices)
if __name__ == '__main__':
    main()