
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
b1 = ['area', 'perimeter', 'compactness', 'lenghtOfKernel', 'widthOfKernel', 'assymetryCoefficient',
            'lengthOfKernelGrove', 'classifier']
b2 = pd.read_table("seeds_dataset.txt", index_col=False, names=b1, header=None, delimiter='\s+')
b3 = b2.values
b4 = b3[:, 7]
b5 = b3[:, :7]
b6 = PCA(n_components=2)
b6.fit(b5)
b7 = b6.transform(b5)
b8 = StandardScaler()
b9 = b8.fit_transform(b7)
b10 = range(1, 7)
b11 = []
for num_clusters in b10:
    b12 = KMeans(n_clusters=num_clusters)
    b12.fit(b9)
    b11.append(b12.inertia_)
b13 = pd.DataFrame({"num_clusters": b10, "b11": b11})
print(b13)
plt.figure(b14 = (12, 6))
plt.plot(b13.num_clusters, b13.b11, b15 = "o")
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Cluster Error (Inertia)')
plt.grid(True)
plt.show()