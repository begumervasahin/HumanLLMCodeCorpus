import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
import numpy as np
def cluster_analysis(data_array, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans.fit(data_array)
    labels = kmeans.predict(data_array)
    x_coords, y_coords = data_array[:, 0], data_array[:, 1]
    centroids = kmeans.cluster_centers_
    centroids_x, centroids_y = centroids[:, 0], centroids[:, 1]
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, c=labels, alpha=0.6, edgecolor='w', cmap='viridis')
    plt.scatter(centroids_x, centroids_y, marker='D', s=100, color='red', label='Centroids')
    plt.title('K-Means Clustering\n' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Cluster analysis complete. Close the plot to proceed.")
    return labels
if __name__ == "__main__":
    sample_data = np.random.rand(100, 2)
    num_clusters = 3
    cluster_labels = cluster_analysis(sample_data, num_clusters)
    print("Cluster labels:", cluster_labels)