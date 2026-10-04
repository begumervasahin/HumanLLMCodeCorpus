import numpy as np
from sklearn.datasets import make_classification
from sklearn.mixture import GaussianMixture
from itertools import groupby
def fonk1():
    X, b1 = make_classification(n_samples=178, n_features=13, n_classes=3, n_clusters_per_class=1, random_state=42)
    return X
def fonk2(X, n_clusters):
    b2 = GaussianMixture(n_components=n_clusters, covariance_type='diag')
    b3 = b2.fit(X)
    print("Means of the Gaussian components:")
    print(b3.means_)
    print("\nWeights of the Gaussian components:")
    print(b3.weights_)
    b4 = b2.predict(X)
    print("\nCluster sizes for each subset:")
    print("Subset 1 (samples 0-58):")
    fonk3(b4[:59])
    print("Subset 2 (samples 59-129):")
    fonk3(b4[59:130])
    print("Subset 3 (samples 130-177):")
    fonk3(b4[130:178])
def fonk3(labels):
    labels.sort()
    b5 = [len(list(group)) for key, group in groupby(labels)]
    print(b5)
def fonk4(b7):
    try:
        b6 = np.genfromtxt(b7, delimiter=',')
        print("Data loaded from file successfully.")
    except IOError:
        print("Could not open file. Generating synthetic b6 instead.")
        b6 = fonk1()
    return b6
def fonk5():
    b7 = "C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv"
    b8 = fonk4(b7)
    b8 = b8[:, :13]
    print("Input b6 shape:", b8.shape)
    fonk2(b8, 3)
    print("EM algorithm completed.")
if b9 = = "__main__":
    fonk5()