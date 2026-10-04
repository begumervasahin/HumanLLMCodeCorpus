
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
sns.set()
file_path = "./yelp.csv"
data = pd.read_csv(file_path, sep=',', quotechar='"', header=0)
data = data[['latitude', 'longitude', 'reviewCount', 'checkins']]
latitude = data['latitude'].values
longitude = data['longitude'].values
X = np.array(list(zip(latitude, longitude)))
K = 4
kmeans = KMeans(n_clusters=K)
kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_
print(f"Within-cluster sum of squares: {kmeans.inertia_}")
for i, centroid in enumerate(centroids, start=1):
    print(f"Centroid {i}: {centroid}")
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='*', s=200, alpha=0.5)
plt.title("Latitude vs. Longitude")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.savefig('Latitude-Longitude.jpg')
plt.show()
