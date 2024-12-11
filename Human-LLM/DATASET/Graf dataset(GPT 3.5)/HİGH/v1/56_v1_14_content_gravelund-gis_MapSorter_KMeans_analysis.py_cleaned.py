import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import datetime
def fonk1(b11, a1):
    """
    Groups (clusters) the input images into "a1" groups (user input for a1 is expected), based on K-Means clustering.
    Outputs a plot of the resulting clusters, including the cluster centers. No data scaling is performed.
    :param b11, a1:
    :return cluster plot, b2:
    """
    b1 = KMeans(n_clusters=int(a1))
    b1.fit(b11)
    b2 = b1.predict(b11)
    b3 = b11[:, 0]
    b4 = b11[:, 1]
    b5 = b1.cluster_centers_
    b6 = b5[:, 0]
    b7 = b5[:, 1]
    plt.scatter(b3, b4, b8 = b2, alpha=0.5)
    plt.scatter(b6, b7, b9 = 'D', s=30)
    plt.title(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("\nInspect the cluster plot shown.\nWhen ready, close the plot and the images will be sorted\n"
          "and copied into subdirectories.")
    plt.show()
    return b2
if b10 = = "__main__":
    b11 = [[1, 2], [2, 3], [3, 4], [10, 9], [8, 7], [7, 6]]
    a1 = 2
    fonk1(b11, a1)