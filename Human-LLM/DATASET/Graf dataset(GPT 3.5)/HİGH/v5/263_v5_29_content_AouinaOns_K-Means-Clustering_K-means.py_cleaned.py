import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
def fonk1():
    np.random.seed(0)
    b8, b1 = make_blobs(n_samples=5000, centers=[[4,4], [-2, -1], [2, -3], [1, 1]], cluster_std=0.9)
    return b8
def fonk2(b8, b10, b11):
    plt.figure(b2 = (6, 4))
    b3 = plt.gca()
    b4 = plt.cm.Spectral(np.linspace(0, 1, len(set(b10))))
    for k, col in zip(range(len(b11)), b4):
        b5 = (b10 == k)
        b6 = b11[k]
        b3.plot(b8[b5, 0], b8[b5, 1], 'w', b7 = col, marker='.')
        b3.plot(b6[0], b6[1], 'o', b7 = col, markeredgecolor='k', markersize=6)
    b3.set_title('KMeans')
    b3.set_xticks(())
    b3.set_yticks(())
    plt.show()
def fonk3():
    b8 = fonk1()
    b9 = KMeans(init="k-means++", n_clusters=4, n_init=12)
    b9.fit(b8)
    b10 = b9.labels_
    b11 = b9.cluster_centers_
    fonk2(b8, b10, b11)
if b12 = = "__main__":
    fonk3()