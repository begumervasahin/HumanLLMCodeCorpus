import numpy as np
from sklearn.mixture import GaussianMixture
from itertools import groupby
def generate_data():
    from sklearn.datasets import make_classification
    X, _ = make_classification(n_samples=178, n_features=13, n_classes=3, n_clusters_per_class=1, random_state=42)
    return X
def apply_em_algorithm(X, n_clusters):
    model = GaussianMixture(n_components=n_clusters, covariance_type='diag')
    fitted_model = model.fit(X)
    print("Means of the components:")
    print(fitted_model.means_)
    print("\nWeights of the components:")
    print(fitted_model.weights_)
    em_predictions = model.predict(X)
    print("\nCluster sizes for subsets:")
    print("Subset 1 (samples 0-58):")
    print_cluster_sizes(em_predictions[:59])
    print("Subset 2 (samples 59-129):")
    print_cluster_sizes(em_predictions[59:130])
    print("Subset 3 (samples 130-177):")
    print_cluster_sizes(em_predictions[130:178])
def print_cluster_sizes(labels):
    labels.sort()
    cluster_sizes = [len(list(group)) for _, group in groupby(labels)]
    print(cluster_sizes)
def load_data(file_path):
    try:
        data = np.genfromtxt(file_path, delimiter=',')
        print("Successfully loaded data from file.")
        return data
    except IOError:
        print("Could not open file.")
        return