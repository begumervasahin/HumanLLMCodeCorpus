import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
import numpy as np
def fonk1(data_array, a1):
    b1 = KMeans(n_clusters=a1, random_state=0)
    b1.fit(data_array)
    b2 = b1.predict(data_array)
    x_coords, b3 = data_array[:, 0], data_array[:, 1]
    b4 = b1.cluster_centers_
    centroids_x, b5 = b4[:, 0], b4[:, 1]
    plt.figure(b6 = (8, 6))
    plt.scatter(x_coords, b3, b7 = b2, alpha=0.6, edgecolor='w', cmap='viridis')
    plt.scatter(centroids_x, b5, b8 = 'D', s=100, color='red', label='Centroids')
    plt.title('K-Means Clustering\n' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Cluster analysis complete. Close the plot to proceed.")
    return b2
if b9 = = "__main__":
    b10 = np.random.rand(100, 2)
    a1 = 3
    b11 = fonk1(b10, a1)
    print("Cluster b2:", b11)