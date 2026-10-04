import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
import numpy as np
def cluster_analysis(data_array, k):
    data_array = np.array(data_array)
    kmeans_model = KMeans(n_clusters=k, random_state=42)
    labels = kmeans_model.fit_predict(data_array)
    x_coords = data_array[:, 0]
    y_coords = data_array[:, 1]
    cluster_centers = kmeans_model.cluster_centers_
    center_x = cluster_centers[:, 0]
    center_y = cluster_centers[:, 1]
    plt.figure(figsize=(10, 6))
    plt.scatter(x_coords, y_coords, c=labels, cmap='viridis', alpha=0.6, edgecolor='w', s=100)
    plt.scatter(center_x, center_y, c='red', marker='D', s=150, label='Centroids')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    plt.title(f"Cluster Analysis - {current_time}")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.show()
    return labels
if __name__ == "__main__":
    example_data = np.array([[1, 2], [2, 3], [3, 4], [10, 9], [8, 7], [7, 6]])
    num_clusters = 2
    cluster_labels = cluster_analysis(example_data, num_clusters)
    print("Cluster Labels:", cluster_labels)