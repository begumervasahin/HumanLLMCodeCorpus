
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
b1 = ['area', 'perimeter', 'compactness', 'lengthOfKernel', 'widthOfKernel', 'assymetryCoefficient',
            'lengthOfKernelGrove', 'classifier']
b2 = pd.read_table("seeds_dataset.txt", names=b1, header=None, delimiter='\s+')
b3 = b2.drop(columns=['classifier']).values
b4 = b2['classifier'].values
b5 = PCA(n_components=2)
b6 = b5.fit_transform(b3)
b7 = StandardScaler()
b8 = b7.fit_transform(b6)
b9 = range(1, 7)
b10 = []
for num_clusters in b9:
    b11 = KMeans(n_clusters=num_clusters)
    b11.fit(b8)
    b10.append(b11.inertia_)
b12 = pd.DataFrame({"num_clusters": b9, "b10": b10})
print(b12)
plt.figure(b13 = (12, 6))
plt.plot(b12.num_clusters, b12.b10, b14 = "o")
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Cluster Error (Inertia)')
plt.grid(True)
plt.show()