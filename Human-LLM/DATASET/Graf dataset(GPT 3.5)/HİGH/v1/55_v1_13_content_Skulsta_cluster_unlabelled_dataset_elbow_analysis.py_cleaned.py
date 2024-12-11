import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
b1 = ['area', 'perimeter', 'compactness', 'lengthOfKernel', 'widthOfKernel', 'asymmetryCoefficient', 'lengthOfKernelGrove', 'classifier']
b2 = pd.read_csv("seeds_dataset.txt", delimiter='\s+', names=b1)
b3 = b2.drop('classifier', axis=1)
b4 = b2['classifier']
b5 = StandardScaler()
b6 = b5.fit_transform(b3)
b7 = PCA(n_components=2)
b8 = b7.fit_transform(b6)
b9 = range(1, 7)
b10 = []
for num_clusters in b9:
    b11 = KMeans(n_clusters=num_clusters)
    b11.fit(b8)
    b10.append(b11.inertia_)
plt.figure(b12 = (12, 6))
plt.plot(b9, b10, b13 = "o")
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Within-cluster Sum of Squares')
plt.grid(True)
plt.show()