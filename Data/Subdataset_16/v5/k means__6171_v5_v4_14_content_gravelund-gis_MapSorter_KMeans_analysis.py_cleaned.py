import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
def fonk1(data_array, k):
    b1 = KMeans(n_clusters=k)
    b2 = b1.fit_predict(data_array)
    xs, b3 = data_array[:, 0], data_array[:, 1]
    b4 = b1.cluster_centers_
    centroids_x, b5 = b4[:, 0], b4[:, 1]
    plt.scatter(xs, b3, b6 = b2, alpha=0.5, label='Data Points')
    plt.scatter(centroids_x, b5, b7 = 'D', s=100, color='red', label='Centroids')
    b8 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    plt.title(f"Cluster Analysis - {b8}")
    plt.legend()
    plt.show()
    print("\nInspect the cluster plot shown. When ready, close the plot and the images will be sorted "
          "and copied into subdirectories.")
    return b2