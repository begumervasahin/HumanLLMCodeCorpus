import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
b1 = [
    'area', 'perimeter', 'compactness', 'length_of_kernel',
    'width_of_kernel', 'asymmetry_coefficient', 'length_of_kernel_groove', 'classifier'
]
b2 = pd.read_table("seeds_dataset.txt", names=b1, header=None, delimiter='\s+')
b3 = b2.drop(columns=['classifier']).values
b4 = b2['classifier'].values
b5 = PCA(n_components=2)
b6 = b5.fit_transform(b3)
b7 = StandardScaler()
b8 = b7.fit_transform(b6)
def fonk1(b8, b9 = 6):
    b10 = range(1, b9 + 1)
    b11 = []
    for num_clusters in b10:
        b12 = KMeans(n_clusters=num_clusters)
        b12.fit(b8)
        b11.append(b12.inertia_)
    return pd.DataFrame({"num_clusters": b10, "b11": b11})
b13 = fonk1(b8)
print(b13)
plt.figure(b14 = (12, 6))
plt.plot(b13.num_clusters, b13.b11, b15 = "o")
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Cluster Error (Inertia)')
plt.grid(True)
plt.show()