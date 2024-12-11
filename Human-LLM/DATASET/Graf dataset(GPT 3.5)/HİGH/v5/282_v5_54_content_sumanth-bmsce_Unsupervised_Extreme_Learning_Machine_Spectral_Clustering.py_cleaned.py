import numpy as np
from sklearn.cluster import SpectralClustering
def fonk1(b1, no_of_clusters):
    b1 = np.array(b1)
    b2 = SpectralClustering(n_clusters=no_of_clusters, eigen_solver='arpack', affinity="nearest_neighbors").fit_predict(b1)
    def fonk2(cluster_subset):
        cluster_subset.sort()
        print(cluster_subset)
        b3 = [len(list(group)) for key, group in groupby(cluster_subset)]
        print(b3)
    print("Clusters for first range:")
    fonk2(b2[:59])
    print("Clusters for second range:")
    fonk2(b2[59:130])
    print("Clusters for third range:")
    fonk2(b2[130:178])
try:
    b4 = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv", delimiter=',')
except:
    print("Could not open file")
b4 = b4[:, :13]
print("Shape of input b1:", b4.shape)
fonk1(b4, 3)
print("Completed")