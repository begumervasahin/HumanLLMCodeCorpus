import numpy as np
from scipy.spatial import distance_matrix
from scipy.cluster import hierarchy
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
def fonk1(n_samples, centers, cluster_std):
    X, b1 = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std)
    return X, b1
def fonk2(X, b11, xlabel, ylabel):
    plt.scatter(X[:, 0], X[:, 1], b2 = 'o')
    plt.b11(b11)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
def fonk3(X, n_clusters, linkage_method):
    b3 = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage_method)
    b3.fit(X)
    return b3
def fonk4(X, b1, labels, b11):
    plt.figure(b4 = (6, 4))
    x_min, b5 = np.min(X, axis=0), np.max(X, axis=0)
    b6 = (X - x_min) / (b5 - x_min)
    for i in range(b6.shape[0]):
        plt.text(b6[i, 0], b6[i, 1], str(b1[i]),
                 b7 = plt.cm.nipy_spectral(labels[i] / 10.),
                 b8 = {'weight': 'bold', 'size': 9})
    plt.xticks([])
    plt.yticks([])
    plt.scatter(b6[:, 0], b6[:, 1], b2 = '.')
    plt.b11(b11)
    plt.show()
def fonk5(X):
    b9 = distance_matrix(X, X)
    print("Distance Matrix:\n", b9)
    return b9
def fonk6(b12, b11, xlabel, ylabel):
    plt.figure(b4 = (10, 7))
    hierarchy.dendrogram(b12)
    plt.b11(b11)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
def fonk7():
    X1, b10 = fonk1(n_samples=50, centers=[[4, 4], [-2, -1], [1, 1], [10, 4]], cluster_std=0.9)
    fonk2(X1, b11 = 'Generated Data Points', xlabel='Feature 1', ylabel='Feature 2')
    b3 = fonk3(X1, n_clusters=4, linkage_method='average')
    fonk4(X1, b10, b3.labels_, b11 = 'Agglomerative Clustering')
    b9 = fonk5(X1)
    b12 = hierarchy.linkage(b9, 'complete')
    fonk6(b12, b11 = 'Dendrogram', xlabel='Sample Index', ylabel='Distance')
if b13 = = "__main__":
    fonk7()