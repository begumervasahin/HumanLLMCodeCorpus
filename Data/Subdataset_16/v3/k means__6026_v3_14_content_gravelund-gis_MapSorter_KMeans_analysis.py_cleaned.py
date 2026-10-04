import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
def fonk1(b11, a1):
    b1 = KMeans(n_clusters=int(a1))
    b1.fit(b11)
    b2 = b1.predict(b11)
    b3 = b11[:, 0]
    b4 = b11[:, 1]
    b5 = b1.cluster_centers_
    b6 = b5[:, 0]
    b7 = b5[:, 1]
    plt.scatter(b3, b4, b8 = b2, alpha=0.5, label='Data Points')
    plt.scatter(b6, b7, b9 = 'D', s=100, b8='red', label='Cluster Centers')
    plt.title(f"Cluster Analysis ({datetime.datetime.now():%Y-%m-%d %H:%M:%S})")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    print("\nInspect the cluster plot shown.\nWhen ready, close the plot to proceed.")
    plt.show()
    return b2
if b10 = = "__main__":
    b11 = [[1, 2], [2, 3], [3, 4], [10, 9], [8, 7], [7, 6]]
    a1 = 2
    fonk1(b11, a1)