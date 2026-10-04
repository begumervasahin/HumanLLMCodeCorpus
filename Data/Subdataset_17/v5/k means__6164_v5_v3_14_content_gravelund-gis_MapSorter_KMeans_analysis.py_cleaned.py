import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
import numpy as np
def cluster_analysis(data_array, k):
    data_array = np.array(data_array)
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(data_array)
    xs, ys = data_array[:, 0], data_array[:, 1]
    centroids = kmeans.cluster_centers_
    centroids_x, centroids_y = centroids[:, 0], centroids[:, 1]
    plt.scatter(xs, ys, c=labels, alpha=0.5, cmap='viridis', label='Data Points')
    plt.scatter(centroids_x, centroids_y, marker='D', s=100, c='red', label='Cluster Centers')
    plt.title(f"Cluster Analysis ({datetime.datetime.now():%Y-%m-%d %H:%M:%S})")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    print("\nInspect the cluster plot shown.\nWhen ready, close the plot to proceed.")
    plt.show()
    return labels
if __name__ == "__main__":
    example_data = [
        [1, 2], [2, 3], [3, 4],
        [10, 9], [8, 7], [7, 6]
    ]
    num_clusters = 2
    cluster_analysis(example_data, num_clusters)