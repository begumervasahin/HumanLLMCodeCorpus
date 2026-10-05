from sklearn.cluster import KMeans
import sklearn.datasets
import numpy as np
import csv;
from itertools import groupby
from sklearn.cluster import SpectralClustering
def fonk1(b1, no_of_clusters):
    b1 = np.array(b1);
    b2 = SpectralClustering(n_clusters=no_of_clusters,eigen_solver='arpack', affinity="nearest_neighbors").fit_predict(b1)
    b3 = b2[:59];
    b3.sort();
    print b3;
    b4 = [len(list(group)) for key, group in groupby(b3)]
    print b4;
    b3 = b2[59:130];
    b3.sort();
    print b3;
    b4 = [len(list(group)) for key, group in groupby(b3)]
    print b4;
    b3 = b2[130:178];
    b3.sort();
    print b3;
    b4 = [len(list(group)) for key, group in groupby(b3)]
    print b4;
try:
    b5 = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv",delimiter=',');
except:
    print("Could not open file");
b5 = b5[:,:13];
print b5.shape;
fonk1(b5,3);
print("Completed");