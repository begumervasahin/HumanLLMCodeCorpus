
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()
file_path = "./yelp.csv"
data = pd.read_csv(file_path, sep=',', quotechar='"', header=0)
columns_of_interest = ['latitude', 'longitude', 'reviewCount', 'checkins']
data = data[columns_of_interest]
latitude = data['latitude'].values
longitude = data['longitude'].values
X = np.array(list(zip(latitude, longitude)))
num_clusters = 4
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_
print(f"Within-cluster sum of squares: {kmeans.inertia_:.2f}")
for i, centroid in enumerate(centroids, start=1):
    print(f"Centroid {i}: {centroid}")
def plot_clusters(X, labels, centroids):
    plt.figure(figsize=(10, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis', label='Data Points')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='*', s=200, alpha=0.5, label='Centroids')
    plt.title("Clustering of Yelp Data: Latitude vs. Longitude")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.legend()
    plt.savefig('Latitude-Longitude.jpg')
    plt.show()
plot_clusters(X, labels, centroids)