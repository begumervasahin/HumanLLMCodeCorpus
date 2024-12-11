import numpy as np
from sklearn.cluster import SpectralClustering
from itertools import groupby
def fonk1(data, no_of_clusters):
    b1 = SpectralClustering(n_clusters=no_of_clusters, eigen_solver='arpack', affinity="nearest_neighbors").fit_predict(data)
    print("Clusters for samples 1-59:")
    fonk2(np.sort(b1[:59]))
    print("Clusters for samples 60-130:")
    fonk2(np.sort(b1[59:130]))
    print("Clusters for samples 131-178:")
    fonk2(np.sort(b1[130:178]))
def fonk2(cluster_labels):
    for key, group in groupby(cluster_labels):
        print(f"Cluster {key}: Size {len(list(group))}")
try:
    b2 = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv", delimiter=',')
except:
    print("Failed to open the file.")
b2 = b2[:, :13]
print("Shape of input data:", b2.shape)
fonk1(b2, 3)
print("Clustering completed.")