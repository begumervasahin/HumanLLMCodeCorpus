from sklearn import mixture
import numpy as np
def fonk1(b5, num_clusters):
    b1 = mixture.GaussianMixture(n_components=num_clusters, covariance_type='diag')
    b1.fit(b5)
    print("Means of the Gaussian components:")
    print(b1.means_)
    print("Weights of the Gaussian components:")
    print(b1.weights_)
    b2 = b1.predict(b5)
    fonk2(b2)
def fonk2(b2):
    first_cluster_labels, second_cluster_labels, b3 = fonk3(b2)
    fonk4("first", first_cluster_labels)
    fonk4("second", second_cluster_labels)
    fonk4("third", b3)
def fonk3(b2):
    return b2[:59], b2[59:130], b2[130:178]
def fonk4(part_name, b2):
    b2.sort()
    print(f"Cluster information for the {part_name} part:")
    fonk5(b2)
def fonk5(b2):
    b4 = [len(list(group)) for _, group in groupby(b2)]
    print(b2)
    print(b4)
try:
    b5 = np.genfromtxt("C:\\Users\\SUMANTH C\\Desktop\\Deep Learning\\Datasets\\wine_sort.csv", delimiter=',')
except Exception as e:
    print("Could not open file:", e)
b5 = b5[:, :13]
print("Shape of input data:", b5.shape)
fonk1(b5, 3)
print("Completed")