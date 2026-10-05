import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
def cluster_analysis(data_array, k):
    model = KMeans(n_clusters=int(k))
    labels = model.fit_predict(data_array)
    xs = data_array[:, 0]
    ys = data_array[:, 1]
    centroids = model.cluster_centers_
    centroids_x = centroids[:, 0]
    centroids_y = centroids[:, 1]
    plt.scatter(xs, ys, c=labels, alpha=0.5, label='Data Points')
    plt.scatter(centroids_x, centroids_y, marker='D', s=50, c='red', label='Centroids')
    plt.title(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    print("\nInspect the cluster plot shown.\nWhen ready, close the plot and the images will be sorted\n"
          "and copied into subdirectories.")
    plt.show()
    return labels