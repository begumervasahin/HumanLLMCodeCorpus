import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.mixture import GaussianMixture
from itertools import groupby
def fonk1():
    X, b1 = make_classification(n_samples=178, n_features=13, n_classes=3, n_clusters_per_class=1, random_state=42)
    return X
def fonk2(X, n_clusters):
    b2 = GaussianMixture(n_components=n_clusters, covariance_type='diag')
    b3 = b2.fit(X)
    print("Means:")
    print(b3.means_)
    print("Weights:")
    print(b3.weights_)
    b4 = b2.predict(X)
    print("Cluster sizes:")
    fonk3(b4[:59])
    fonk3(b4[59:130])
    fonk3(b4[130:178])
def fonk3(labels):
    labels.sort()
    b5 = [len(list(group)) for key, group in groupby(labels)]
    print(b5)
try:
    b6 = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv", delimiter=',')
except IOError:
    print("Could not open file")
b6 = b6[:, :13]
print("Input data shape:", b6.shape)
fonk2(b6, 3)
print("EM algorithm completed.")