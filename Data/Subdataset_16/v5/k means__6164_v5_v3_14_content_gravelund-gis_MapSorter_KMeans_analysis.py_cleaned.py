import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
import numpy as np
def fonk1(b1, k):
    b1 = np.array(b1)
    b2 = KMeans(n_clusters=k, random_state=42)
    b3 = b2.fit_predict(b1)
    xs, b4 = b1[:, 0], b1[:, 1]
    b5 = b2.cluster_centers_
    centroids_x, b6 = b5[:, 0], b5[:, 1]
    plt.scatter(xs, b4, b7 = b3, alpha=0.5, cmap='viridis', label='Data Points')
    plt.scatter(centroids_x, b6, b8 = 'D', s=100, b7='red', label='Cluster Centers')
    plt.title(f"Cluster Analysis ({datetime.datetime.now():%Y-%m-%d %H:%M:%S})")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    print("\nInspect the cluster plot shown.\nWhen ready, close the plot to proceed.")
    plt.show()
    return b3
if b9 = = "__main__":
    b10 = [
        [1, 2], [2, 3], [3, 4],
        [10, 9], [8, 7], [7, 6]
    ]
    a1 = 2
    fonk1(b10, a1)