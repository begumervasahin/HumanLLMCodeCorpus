import numpy as np
from sklearn.mixture import GaussianMixture
from itertools import groupby
def fonk1():
    from sklearn.datasets import make_classification
    X, b1 = make_classification(n_samples=178, n_features=13, n_classes=3, n_clusters_per_class=1, random_state=42)
    return X
def fonk2(X, n_clusters):
    b2 = GaussianMixture(n_components=n_clusters, covariance_type='diag')
    b3 = b2.fit(X)
    print("Means of the components:")
    print(b3.means_)
    print("\nWeights of the components:")
    print(b3.weights_)
    b4 = b2.predict(X)
    print("\nCluster sizes for subsets:")
    print("Subset 1 (samples 0-58):")
    fonk3(b4[:59])
    print("Subset 2 (samples 59-129):")
    fonk3(b4[59:130])
    print("Subset 3 (samples 130-177):")
    fonk3(b4[130:178])
def fonk3(labels):
    labels.sort()
    b5 = [len(list(group)) for b1, group in groupby(labels)]
    print(b5)
def fonk4(file_path):
    try:
        b6 = np.genfromtxt(file_path, delimiter=',')
        print("Successfully loaded b6 from file.")
        return b6
    except IOError:
        print("Could not open file.")
        return