import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
import numpy as np
def fonk1(b1, k):
    b1 = np.array(b1)
    b2 = KMeans(n_clusters=k, random_state=42)
    b3 = b2.fit_predict(b1)
    b4 = b1[:, 0]
    b5 = b1[:, 1]
    b6 = b2.cluster_centers_
    b7 = b6[:, 0]
    b8 = b6[:, 1]
    plt.figure(b9 = (10, 6))
    plt.scatter(b4, b5, b10 = b3, cmap='viridis', alpha=0.6, edgecolor='w', s=100)
    plt.scatter(b7, b8, b10 = 'red', marker='D', s=150, label='Centroids')
    b11 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    plt.title(f"Cluster Analysis - {b11}")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.show()
    return b3
if b12 = = "__main__":
    b13 = np.array([[1, 2], [2, 3], [3, 4], [10, 9], [8, 7], [7, 6]])
    a1 = 2
    b14 = fonk1(b13, a1)
    print("Cluster Labels:", b14)