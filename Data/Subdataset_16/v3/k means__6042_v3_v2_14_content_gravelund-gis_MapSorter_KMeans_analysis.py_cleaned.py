import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import datetime
def fonk1(b1, k):
    b1 = np.array(b1)
    b2 = KMeans(n_clusters=k)
    b2.fit(b1)
    b3 = b2.predict(b1)
    b4 = b1[:, 0]
    b5 = b1[:, 1]
    b6 = b2.cluster_centers_
    b7 = b6[:, 0]
    b8 = b6[:, 1]
    plt.scatter(b4, b5, b9 = b3, alpha=0.5)
    plt.scatter(b7, b8, b10 = 'D', s=100, b9='red')
    plt.title(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("\nInspect the cluster plot shown.\nWhen ready, close the plot.")
    plt.show()
    return b3
if b11 = = "__main__":
    b12 = [[1, 2], [2, 3], [3, 4], [10, 9], [8, 7], [7, 6]]
    a1 = 2
    b13 = fonk1(b12, a1)
    print("Cluster b3:", b13)