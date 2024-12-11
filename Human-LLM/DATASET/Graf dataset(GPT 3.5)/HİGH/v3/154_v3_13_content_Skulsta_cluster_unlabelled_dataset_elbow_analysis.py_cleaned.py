
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
b1 = [
    'area', 'perimeter', 'compactness', 'lengthOfKernel', 'widthOfKernel',
    'asymmetryCoefficient', 'lengthOfKernelGrove', 'classifier'
]
def fonk1(file_path, column_names):
    return pd.read_csv(file_path, b2 = '\s+', names=column_names)
def fonk2(data):
    b3 = data.drop('classifier', axis=1)
    b4 = data['classifier']
    b5 = StandardScaler()
    b6 = b5.fit_transform(b3)
    return b6
def fonk3(b3):
    b7 = PCA(n_components=2)
    return b7.fit_transform(b3)
def fonk4(b3, b8 = 6):
    b9 = []
    for num_clusters in range(1, b8 + 1):
        b10 = KMeans(n_clusters=num_clusters)
        b10.fit(b3)
        b9.append(b10.inertia_)
    return b9
def fonk5(cluster_range, b9):
    plt.figure(b11 = (12, 6))
    plt.plot(cluster_range, b9, b12 = "o")
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Within-cluster Sum of Squares')
    plt.grid(True)
    plt.show()
b13 = fonk1("seeds_dataset.txt", b1)
b6 = fonk2(b13)
b14 = fonk3(b6)
b9 = fonk4(b14)
fonk5(range(1, 7), b9)