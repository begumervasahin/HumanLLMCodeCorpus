import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
data_frame = pd.read_csv('C:/Users/Admin/PycharmProjects/GeyserEruption/resources/faithful_geyser.csv')
scaler = StandardScaler()
X_std = scaler.fit_transform(data_frame)
kmeans = KMeans(n_clusters=2, max_iter=100)
kmeans.fit(X_std)
centroids = kmeans.cluster_centers_
fig, ax = plt.subplots(figsize=(8, 8))
for cluster_label, color in zip(range(2), ['green', 'blue']):
    plt.scatter(X_std[kmeans.labels_ == cluster_label, 0], X_std[kmeans.labels_ == cluster_label, 1],
                c=color, label=f'Cluster {cluster_label + 1}')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=100,
            c='r', label='Centroid')
plt.legend()
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('Eruption time (minutes)', fontsize=16)
plt.ylabel('Waiting time to next eruption (minutes)', fontsize=16)
plt.title('Clustered Data from Old Faithful Geyser, \n Yellowstone, USA', fontsize=20, fontweight='bold')
ax.set_aspect('equal')
plt.savefig('plot-clusters.png')