import numpy as np
from sklearn.cluster import SpectralClustering
from itertools import groupby
def spectral_clustering(data, no_of_clusters):
    spectral = SpectralClustering(n_clusters=no_of_clusters, eigen_solver='arpack', affinity="nearest_neighbors").fit_predict(data)
    print("Clusters for samples 1-59:")
    print_cluster_info(np.sort(spectral[:59]))
    print("Clusters for samples 60-130:")
    print_cluster_info(np.sort(spectral[59:130]))
    print("Clusters for samples 131-178:")
    print_cluster_info(np.sort(spectral[130:178]))
def print_cluster_info(cluster_labels):
    for key, group in groupby(cluster_labels):
        print(f"Cluster {key}: Size {len(list(group))}")
try:
    input_data = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv", delimiter=',')
except:
    print("Failed to open the file.")
input_data = input_data[:, :13]
print("Shape of input data:", input_data.shape)
spectral_clustering(input_data, 3)
print("Clustering completed.")