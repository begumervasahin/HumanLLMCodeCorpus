import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
file_path = "./yelp.csv"
data = pd.read_csv(file_path, sep=',', quotechar='"', header=0)
data = data[['latitude', 'longitude', 'reviewCount', 'checkins']]
X = scale(data[['latitude', 'longitude']])
K = 4
kmeans = KMeans(n_clusters=K)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_
print("within-cluster sum of squares: %f" % kmeans.inertia_)
for i in range(K):
    print("Centroid%d %s" % (i + 1, centroids[i]))
plt.figure(figsize=(10, 6))
plt.scatter(data['latitude'], data['longitude'], c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='*', s=200, alpha=0.5)
plt.title("Latitude vs. Longitude")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.savefig('Latitude-Longitude.jpg')
plt.show()