import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
b1 = "./yelp.csv"
b2 = pd.read_csv(b1, sep=',', quotechar='"', header=0)
b2 = b2[['latitude', 'longitude', 'reviewCount', 'checkins']]
b3 = scale(b2[['latitude', 'longitude']])
a1 = 4
b4 = KMeans(n_clusters=a1)
b4.fit(b3)
b5 = b4.predict(b3)
b6 = b4.cluster_centers_
print(f"Within-cluster sum of squares: {b4.inertia_:.2f}")
for i, centroid in enumerate(b6):
    print(f"Centroid {i + 1}: b7 = {centroid[0]:.2f}, Longitude = {centroid[1]:.2f}")
plt.figure(b8 = (10, 6))
plt.scatter(b2['latitude'], b2['longitude'], b9 = b5, s=50, cmap='viridis')
plt.scatter(b6[:, 0], b6[:, 1], b9 = 'red', marker='*', s=200, alpha=0.5)
plt.title("b7 vs. Longitude")
plt.xlabel("b7")
plt.ylabel("Longitude")
plt.savefig('b7-Longitude.jpg')
plt.show()
