
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
sns.set()
b1 = "./yelp.csv"
b2 = pd.read_csv(b1, sep=',', quotechar='"', header=0)
b2 = b2[['latitude', 'longitude', 'reviewCount', 'checkins']]
b3 = b2[['latitude', 'longitude']].values
a1 = 4
b4 = KMeans(a1=a1)
b4.fit(b3)
b5 = b4.predict(b3)
b6 = b4.cluster_centers_
print(f"Within-cluster sum of squares: {b4.inertia_}")
for i, centroid in enumerate(b6, b7 = 1):
    print(f"Centroid {i}: {centroid}")
plt.figure(b8 = (10, 6))
plt.scatter(b3[:, 0], b3[:, 1], b9 = b5, s=50, cmap='viridis', label='Data Points')
plt.scatter(b6[:, 0], b6[:, 1], b9 = 'red', marker='*', s=200, alpha=0.5, label='Centroids')
plt.title("Clustering of Yelp Data: Latitude vs. Longitude")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.legend()
plt.savefig('Latitude-Longitude.jpg')
plt.show()
