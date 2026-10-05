from sklearn import mixture
import sklearn.datasets
import matplotlib.pyplot as plt
import numpy as np
import generator as g;
from sklearn import preprocessing
def fonk1(input_array,no_of_clusters):
    b1 = sklearn.mixture.GaussianMixture(n_components=no_of_clusters,covariance_type='diag')
    b2 = b1.fit(X)
    print b2.means_
    print b2.weights_
    b3 = b1.predict(X)
    b4 = b3[:59];
    b4.sort();
    print b4;
    b5 = [len(list(group)) for key, group in groupby(b4)]
    print b5;
    b4 = b3[59:130];
    b4.sort();
    print b4;
    b5 = [len(list(group)) for key, group in groupby(b4)]
    print b5;
    b4 = b3[130:178];
    b4.sort();
    print b4;
    b5 = [len(list(group)) for key, group in groupby(b4)]
    print b5;
try:
    b6 = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv",delimiter=',');
except:
    print("Could not open file");
b6 = b6[:,:13];
print b6.shape;
fonk1(b6,3);
print("Completed");