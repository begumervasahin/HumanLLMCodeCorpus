
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
sns.set()
file_path = "./yelp.csv"
data = pd.read_csv(file_path, sep=',', quotechar='"', header=0)
features = ['latitude', 'longitude', 'reviewCount', 'checkins']
data = data[features]
latitude = data['latitude'].values
longitude = data['longitude'].values
X = np.column_stack((latitude, longitude))
num_clusters = 4
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
print("Within-cluster sum of squares: %f" % kmeans.inertia_)
for i, centroid in enumerate(centroids):
    print(f"Centroid {i+1}: {centroid}")
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='*', s=200, alpha=0.5)
plt.title("Latitude vs. Longitude")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.savefig('Latitude-Longitude.jpg')
plt.show()
