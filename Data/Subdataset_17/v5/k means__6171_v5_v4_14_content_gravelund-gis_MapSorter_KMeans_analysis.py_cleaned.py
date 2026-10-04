import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
def cluster_analysis(data_array, k):
    kmeans = KMeans(n_clusters=k)
    labels = kmeans.fit_predict(data_array)
    xs, ys = data_array[:, 0], data_array[:, 1]
    centroids = kmeans.cluster_centers_
    centroids_x, centroids_y = centroids[:, 0], centroids[:, 1]
    plt.scatter(xs, ys, c=labels, alpha=0.5, label='Data Points')
    plt.scatter(centroids_x, centroids_y, marker='D', s=100, color='red', label='Centroids')
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    plt.title(f"Cluster Analysis - {current_time}")
    plt.legend()
    plt.show()
    print("\nInspect the cluster plot shown. When ready, close the plot and the images will be sorted "
          "and copied into subdirectories.")
    return labels