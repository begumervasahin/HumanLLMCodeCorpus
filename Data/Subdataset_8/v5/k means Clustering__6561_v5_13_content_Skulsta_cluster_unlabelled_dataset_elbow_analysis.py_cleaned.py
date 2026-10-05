
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
colnames = ['area', 'perimeter', 'compactness', 'lengthOfKernel', 'widthOfKernel', 'assymetryCoefficient',
            'lengthOfKernelGrove', 'classifier']
data = pd.read_table("seeds_dataset.txt", names=colnames, header=None, delimiter='\s+')
X = data.drop(columns=['classifier']).values
y = data['classifier'].values
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_pca)
cluster_range = range(1, 7)
cluster_errors = []
for num_clusters in cluster_range:
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X_scaled)
    cluster_errors.append(kmeans.inertia_)
clusters_df = pd.DataFrame({"num_clusters": cluster_range, "cluster_errors": cluster_errors})
print(clusters_df)
plt.figure(figsize=(12, 6))
plt.plot(clusters_df.num_clusters, clusters_df.cluster_errors, marker="o")
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Cluster Error (Inertia)')
plt.grid(True)
plt.show()