import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
import numpy as np
def cluster_analysis(data_array, k):
    data_array = np.array(data_array)
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(data_array)
    xs = data_array[:, 0]
    ys = data_array[:, 1]
    centroids = model.cluster_centers_
    centroids_x = centroids[:, 0]
    centroids_y = centroids[:, 1]
    plt.scatter(xs, ys, c=labels, alpha=0.5, cmap='viridis')
    plt.scatter(centroids_x, centroids_y, marker='D', s=100, c='red', label='Centroids')
    plt.title("Cluster Analysis - " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.show()
    return labels
if __name__ == "__main__":
    data_array = np.array([[1, 2], [2, 3], [3, 4], [10, 9], [8, 7], [7, 6]])
    k = 2
    cluster_labels = cluster_analysis(data_array, k)
    print("Cluster Labels:", cluster_labels)