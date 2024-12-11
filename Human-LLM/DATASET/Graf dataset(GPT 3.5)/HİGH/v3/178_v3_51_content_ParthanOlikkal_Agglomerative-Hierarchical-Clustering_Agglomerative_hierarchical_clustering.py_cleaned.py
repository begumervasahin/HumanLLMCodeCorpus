import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from scipy.spatial import distance_matrix
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets.samples_generator import make_blobs
def fonk1():
    b5, b1 = make_blobs(n_samples=50, centers=[[4, 4], [-2, -1], [1, 1], [10, 4]], cluster_std=0.9)
    return b5, b1
def fonk2(b5, b1, labels):
    plt.scatter(b5[:, 0], b5[:, 1], b2 = 'o')
    plt.figure(b3 = (6, 4))
    x_min, b4 = np.min(b5, axis=0), np.max(b5, axis=0)
    b5 = (b5 - x_min) / (b4 - x_min)
    for i in range(b5.shape[0]):
        plt.text(b5[i, 0], b5[i, 1], str(b1[i]), b6 = plt.cm.nipy_spectral(labels[i] / 10.),
                 b7 = {'weight': 'bold', 'size': 9})
    plt.xticks([])
    plt.yticks([])
    plt.scatter(b5[:, 0], b5[:, 1], b2 = '.')
    plt.show()
def fonk3(b5):
    return distance_matrix(b5, b5)
def fonk4(distance_matrix):
    b8 = hierarchy.linkage(distance_matrix, 'complete')
    b9 = hierarchy.dendrogram(b8)
b5, b1 = fonk1()
b10 = AgglomerativeClustering(n_clusters=4, linkage='average')
b10.fit(b5, b1)
b11 = b10.labels_
fonk2(b5, b1, b11)
b12 = fonk3(b5)
print(b12)
fonk4(b12)