import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data_frame = pd.read_csv('C:/Users/Admin/PycharmProjects/GeyserEruption/resources/faithful_geyser.csv')
scaler = StandardScaler()
X_std = scaler.fit_transform(data_frame)
kmeans = KMeans(n_clusters=2, max_iter=100)
kmeans.fit(X_std)
centroids = kmeans.cluster_centers_
fig, ax = plt.subplots(figsize=(8, 8))
plt.scatter(X_std[kmeans.labels_ == 0, 0], X_std[kmeans.labels_ == 0, 1],
            c='green', label='Cluster 1')
plt.scatter(X_std[kmeans.labels_ == 1, 0], X_std[kmeans.labels_ == 1, 1],
            c='blue', label='Cluster 2')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=100,
            c='red', label='Centroid')
plt.legend()
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('Eruption time (minutes)', fontsize=16)
plt.ylabel('Waiting time to next eruption (minutes)', fontsize=16)
plt.title('Clustered Data from Old Faithful Geyser, \n Yellowstone, USA', fontsize=20, fontweight='bold')
ax.set_aspect('equal')
plt.savefig('plot-clusters.png')
plt.show()