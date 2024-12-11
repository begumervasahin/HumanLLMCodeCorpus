import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
def fonk1(data_array, k):
    b1 = KMeans(n_clusters=int(k))
    b2 = b1.fit_predict(data_array)
    b3 = data_array[:, 0]
    b4 = data_array[:, 1]
    b5 = b1.cluster_centers_
    b6 = b5[:, 0]
    b7 = b5[:, 1]
    plt.scatter(b3, b4, b8 = b2, alpha=0.5, label='Data Points')
    plt.scatter(b6, b7, b9 = 'D', s=50, b8='red', label='Centroids')
    plt.title(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    print("\nInspect the cluster plot shown.\nWhen ready, close the plot and the images will be sorted\n"
          "and copied into subdirectories.")
    plt.show()
    return b2