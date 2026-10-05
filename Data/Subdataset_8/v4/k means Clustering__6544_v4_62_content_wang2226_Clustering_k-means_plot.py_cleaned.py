
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()
file_path = "./yelp.csv"
data = pd.read_csv(file_path, sep=',', quotechar='"', header=0)
data = data[['latitude', 'longitude', 'reviewCount', 'checkins']]
latitude = data['latitude'].values
longitude = data['longitude'].values
review_count = data['reviewCount'].values
checkins = data['checkins'].values
X = np.array(list(zip(latitude, longitude)))
K = 4
kmeans = KMeans(n_clusters=K)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_
print("Within-cluster sum of squares: %f" % kmeans.inertia_)
for i in range(K):
    print("Centroid %d: %s" % (i + 1, centroids[i]))
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='*', s=200, alpha=0.5)
plt.title("Latitude vs. Longitude")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.savefig('Latitude-Longitude.jpg')
plt.show()
