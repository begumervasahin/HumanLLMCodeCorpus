import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import datetime
def cluster_analysis(data_array, k):
    data_array = np.array(data_array)
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data_array)
    labels = kmeans.predict(data_array)
    x_coords = data_array[:, 0]
    y_coords = data_array[:, 1]
    centroids = kmeans.cluster_centers_
    centroids_x = centroids[:, 0]
    centroids_y = centroids[:, 1]
    plt.scatter(x_coords, y_coords, c=labels, alpha=0.5)
    plt.scatter(centroids_x, centroids_y, marker='D', s=100, c='red')
    plt.title(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("\nInspect the cluster plot shown.\nWhen ready, close the plot.")
    plt.show()
    return labels
if __name__ == "__main__":
    example_data = [[1, 2], [2, 3], [3, 4], [10, 9], [8, 7], [7, 6]]
    num_clusters = 2
    cluster_labels = cluster_analysis(example_data, num_clusters)
    print("Cluster labels:", cluster_labels)