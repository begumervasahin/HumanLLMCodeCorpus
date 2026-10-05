from sklearn import mixture
import numpy as np
def fit_gaussian_mixture(input_data, num_clusters):
    model = mixture.GaussianMixture(n_components=num_clusters, covariance_type='diag')
    model.fit(input_data)
    print("Means of the Gaussian components:")
    print(model.means_)
    print("Weights of the Gaussian components:")
    print(model.weights_)
    cluster_labels = model.predict(input_data)
    print_cluster_info(cluster_labels)
def print_cluster_info(cluster_labels):
    first_cluster_labels, second_cluster_labels, third_cluster_labels = split_clusters(cluster_labels)
    print_cluster_part_info("first", first_cluster_labels)
    print_cluster_part_info("second", second_cluster_labels)
    print_cluster_part_info("third", third_cluster_labels)
def split_clusters(cluster_labels):
    return cluster_labels[:59], cluster_labels[59:130], cluster_labels[130:178]
def print_cluster_part_info(part_name, cluster_labels):
    cluster_labels.sort()
    print(f"Cluster information for the {part_name} part:")
    print_cluster_counts(cluster_labels)
def print_cluster_counts(cluster_labels):
    cluster_counts = [len(list(group)) for _, group in groupby(cluster_labels)]
    print(cluster_labels)
    print(cluster_counts)
try:
    input_data = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv", delimiter=',')
except Exception as e:
    print("Could not open file:", e)
input_data = input_data[:, :13]
print("Shape of input data:", input_data.shape)
fit_gaussian_mixture(input_data, 3)
print("Completed")