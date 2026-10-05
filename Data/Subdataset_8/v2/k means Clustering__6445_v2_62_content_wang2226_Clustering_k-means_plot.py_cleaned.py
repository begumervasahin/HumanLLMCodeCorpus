
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
file_path = "./yelp.csv"
data = pd.read_csv(file_path, sep=',', quotechar='"', header=0)
data = data[['latitude', 'longitude', 'reviewCount', 'checkins']]
scaled_features = scale(data[['latitude', 'longitude']])
num_clusters = 4
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(scaled_features)
cluster_labels = kmeans.predict(scaled_features)
centroids = kmeans.cluster_centers_
print("Within-cluster sum of squares: %f" % kmeans.inertia_)
for i, centroid in enumerate(centroids):
    print(f"Centroid {i + 1}: Latitude = {centroid[0]}, Longitude = {centroid[1]}")
plt.figure(figsize=(10, 6))
plt.scatter(data['latitude'], data['longitude'], c=cluster_labels, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='*', s=200, alpha=0.5)
plt.title("Latitude vs. Longitude")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.savefig('Latitude-Longitude.jpg')
plt.show()
