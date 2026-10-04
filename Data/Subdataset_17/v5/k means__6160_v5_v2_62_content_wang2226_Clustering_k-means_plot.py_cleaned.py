import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
file_path = "./yelp.csv"
data = pd.read_csv(file_path, sep=',', quotechar='"', header=0)
selected_columns = ['latitude', 'longitude', 'reviewCount', 'checkins']
data = data[selected_columns]
latitude_longitude = data[['latitude', 'longitude']]
scaled_features = scale(latitude_longitude)
num_clusters = 4
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(scaled_features)
cluster_labels = kmeans.predict(scaled_features)
centroids = kmeans.cluster_centers_
print(f"Within-cluster sum of squares: {kmeans.inertia_:.2f}")
for i, centroid in enumerate(centroids):
    print(f"Centroid {i + 1}: Latitude = {centroid[0]:.2f}, Longitude = {centroid[1]:.2f}")
plt.figure(figsize=(10, 6))
plt.scatter(data['latitude'], data['longitude'], c=cluster_labels, s=50, cmap='viridis', label='Data Points')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='*', s=200, alpha=0.5, label='Centroids')
plt.title("Clusters of Latitude and Longitude")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.legend()
plt.savefig('Latitude-Longitude.jpg')
plt.show()
