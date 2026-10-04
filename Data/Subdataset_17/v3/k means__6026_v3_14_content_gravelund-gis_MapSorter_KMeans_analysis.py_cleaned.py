import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
def cluster_analysis(data_array, k):
    model = KMeans(n_clusters=int(k))
    model.fit(data_array)
    labels = model.predict(data_array)
    xs = data_array[:, 0]
    ys = data_array[:, 1]
    centroids = model.cluster_centers_
    centroids_x = centroids[:, 0]
    centroids_y = centroids[:, 1]
    plt.scatter(xs, ys, c=labels, alpha=0.5, label='Data Points')
    plt.scatter(centroids_x, centroids_y, marker='D', s=100, c='red', label='Cluster Centers')
    plt.title(f"Cluster Analysis ({datetime.datetime.now():%Y-%m-%d %H:%M:%S})")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    print("\nInspect the cluster plot shown.\nWhen ready, close the plot to proceed.")
    plt.show()
    return labels
if __name__ == "__main__":
    data_array = [[1, 2], [2, 3], [3, 4], [10, 9], [8, 7], [7, 6]]
    k = 2
    cluster_analysis(data_array, k)