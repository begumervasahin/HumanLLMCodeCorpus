
from sklearn.cluster import KMeans, SpectralClustering
import sklearn.datasets
import numpy as np
import csv
from itertools import groupby
def spectral_clustering(data, no_of_clusters):
    data = np.array(data)
    spectral = SpectralClustering(n_clusters=no_of_clusters, eigen_solver='arpack', affinity="nearest_neighbors").fit_predict(data)
    def print_cluster_lengths(spectral, start, end):
        cluster_subset = spectral[start:end]
        cluster_subset.sort()
        print(cluster_subset)
        lengths = [len(list(group)) for key, group in groupby(cluster_subset)]
        print(lengths)
    print("Clusters for first range:")
    print_cluster_lengths(spectral, 0, 59)
    print("Clusters for second range:")
    print_cluster_lengths(spectral, 59, 130)
    print("Clusters for third range:")
    print_cluster_lengths(spectral, 130, 178)
try:
    input_data = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv", delimiter=',')
except:
    print("Could not open file")
input_data = input_data[:, :13]
print("Shape of input data:", input_data.shape)
spectral_clustering(input_data, 3)
print("Completed")