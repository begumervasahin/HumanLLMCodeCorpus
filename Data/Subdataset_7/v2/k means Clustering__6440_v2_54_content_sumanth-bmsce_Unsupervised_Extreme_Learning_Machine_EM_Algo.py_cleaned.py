from sklearn import mixture
import numpy as np
def fonk1(b7, num_clusters):
    b1 = mixture.GaussianMixture(n_components=num_clusters, covariance_type='diag')
    b1.fit(b7)
    print("Means of the Gaussian components:")
    print(b1.means_)
    print("Weights of the Gaussian components:")
    print(b1.weights_)
    b2 = b1.predict(b7)
    fonk2(b2)
def fonk2(b2):
    b3 = b2[:59]
    b4 = b2[59:130]
    b5 = b2[130:178]
    b3.sort()
    b4.sort()
    b5.sort()
    print("Cluster information for the first part:")
    fonk3(b3)
    print("Cluster information for the second part:")
    fonk3(b4)
    print("Cluster information for the third part:")
    fonk3(b5)
def fonk3(b2):
    b6 = [len(list(group)) for _, group in groupby(b2)]
    print(b2)
    print(b6)
try:
    b7 = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv", delimiter=',')
except Exception as e:
    print("Could not open file:", e)
b7 = b7[:, :13]
print("Shape of input data:", b7.shape)
fonk1(b7, 3)
print("Completed")