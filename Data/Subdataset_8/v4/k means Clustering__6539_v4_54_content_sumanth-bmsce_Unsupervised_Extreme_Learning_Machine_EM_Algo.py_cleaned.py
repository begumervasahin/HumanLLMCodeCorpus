import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.mixture import GaussianMixture
from itertools import groupby
def generate_data():
    X, _ = make_classification(n_samples=178, n_features=13, n_classes=3, n_clusters_per_class=1, random_state=42)
    return X
def apply_em_algorithm(X, n_clusters):
    model = GaussianMixture(n_components=n_clusters, covariance_type='diag')
    fitted_model = model.fit(X)
    print("Means:")
    print(fitted_model.means_)
    print("Weights:")
    print(fitted_model.weights_)
    em_predictions = model.predict(X)
    print("Cluster sizes:")
    print_cluster_sizes(em_predictions[:59])
    print_cluster_sizes(em_predictions[59:130])
    print_cluster_sizes(em_predictions[130:178])
def print_cluster_sizes(labels):
    labels.sort()
    cluster_sizes = [len(list(group)) for key, group in groupby(labels)]
    print(cluster_sizes)
try:
    input_data = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv", delimiter=',')
except IOError:
    print("Could not open file")
input_data = input_data[:, :13]
print("Input data shape:", input_data.shape)
apply_em_algorithm(input_data, 3)
print("EM algorithm completed.")