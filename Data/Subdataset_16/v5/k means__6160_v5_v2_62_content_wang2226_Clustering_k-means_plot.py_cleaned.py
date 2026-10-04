import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
b1 = "./yelp.csv"
b2 = pd.read_csv(b1, sep=',', quotechar='"', header=0)
b3 = ['latitude', 'longitude', 'reviewCount', 'checkins']
b2 = b2[b3]
b4 = b2[['latitude', 'longitude']]
b5 = scale(b4)
a1 = 4
b6 = KMeans(n_clusters=a1, random_state=42)
b6.fit(b5)
b7 = b6.predict(b5)
b8 = b6.cluster_centers_
print(f"Within-cluster sum of squares: {b6.inertia_:.2f}")
for i, centroid in enumerate(b8):
    print(f"Centroid {i + 1}: b9 = {centroid[0]:.2f}, Longitude = {centroid[1]:.2f}")
plt.figure(b10 = (10, 6))
plt.scatter(b2['latitude'], b2['longitude'], b11 = b7, s=50, cmap='viridis', label='Data Points')
plt.scatter(b8[:, 0], b8[:, 1], b11 = 'red', marker='*', s=200, alpha=0.5, label='Centroids')
plt.title("Clusters of b9 and Longitude")
plt.xlabel("b9")
plt.ylabel("Longitude")
plt.legend()
plt.savefig('b9-Longitude.jpg')
plt.show()
