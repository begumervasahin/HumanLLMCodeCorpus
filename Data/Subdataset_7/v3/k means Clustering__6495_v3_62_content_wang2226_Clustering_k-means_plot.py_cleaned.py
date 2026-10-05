
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
b1 = "./yelp.csv"
b2 = pd.read_csv(b1, sep=',', quotechar='"', header=0)
b3 = ['latitude', 'longitude']
b2 = b2[b3 + ['reviewCount', 'checkins']]
b4 = scale(b2[b3])
a1 = 4
b5 = KMeans(n_clusters=a1)
b5.fit(b4)
b6 = b5.predict(b4)
b7 = b5.cluster_centers_
print("Within-cluster sum of squares:", b5.inertia_)
for i, centroid in enumerate(b7):
    print(f"Centroid {i + 1}: b8 = {centroid[0]}, Longitude = {centroid[1]}")
plt.figure(b9 = (10, 6))
plt.scatter(b2['latitude'], b2['longitude'], b10 = b6, s=50, cmap='viridis')
plt.scatter(b7[:, 0], b7[:, 1], b10 = 'red', marker='*', s=200, alpha=0.5)
plt.title("b8 vs. Longitude")
plt.xlabel("b8")
plt.ylabel("Longitude")
plt.savefig('b8-Longitude.jpg')
plt.show()
