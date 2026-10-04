import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
import numpy as np
def fonk1(b1, a1):
    b1 = np.array(b1)
    b2 = KMeans(n_clusters=a1, random_state=42)
    b3 = b2.fit_predict(b1)
    b4 = b1[:, 0]
    b5 = b1[:, 1]
    b6 = b2.cluster_centers_
    b7 = b6[:, 0]
    b8 = b6[:, 1]
    plt.scatter(b4, b5, b9 = b3, alpha=0.5, cmap='viridis')
    plt.scatter(b7, b8, b10 = 'D', s=100, b9='red', label='Centroids')
    plt.title("Cluster Analysis - " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.show()
    return b3
if b11 = = "__main__":
    b1 = np.array([[1, 2], [2, 3], [3, 4], [10, 9], [8, 7], [7, 6]])
    a1 = 2
    b12 = fonk1(b1, a1)
    print("Cluster Labels:", b12)