import numpy as np
from sklearn.cluster import SpectralClustering
from itertools import groupby
def fonk1(data, no_of_clusters):
    b1 = SpectralClustering(n_clusters=no_of_clusters, eigen_solver='arpack', affinity="nearest_neighbors").fit_predict(data)
    print("Cluster labels for samples 1-59:")
    print(np.sort(b1[:59]))
    print("Cluster sizes for samples 1-59:")
    print([len(list(group)) for key, group in groupby(np.sort(b1[:59]))])
    print("Cluster labels for samples 60-130:")
    print(np.sort(b1[59:130]))
    print("Cluster sizes for samples 60-130:")
    print([len(list(group)) for key, group in groupby(np.sort(b1[59:130]))])
    print("Cluster labels for samples 131-178:")
    print(np.sort(b1[130:178]))
    print("Cluster sizes for samples 131-178:")
    print([len(list(group)) for key, group in groupby(np.sort(b1[130:178]))])
try:
    b2 = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv", delimiter=',')
except:
    print("Could not open file")
b2 = b2[:, :13]
print("Shape of input data:", b2.shape)
fonk1(b2, 3)
print("Completed")