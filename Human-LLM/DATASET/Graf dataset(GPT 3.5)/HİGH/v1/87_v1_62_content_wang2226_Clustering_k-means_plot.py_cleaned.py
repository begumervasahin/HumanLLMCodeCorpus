import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
b1 = "./yelp.csv"
b2 = pd.read_csv(b1, sep=',', quotechar='"', header=0)
b2 = b2[['latitude', 'longitude', 'reviewCount', 'checkins']]
b3 = scale(b2[['latitude', 'longitude']])
a1 = 4
b4 = KMeans(n_clusters=a1)
b4 = b4.fit(b3)
b5 = b4.predict(b3)
b6 = b4.cluster_centers_
print("within-cluster sum of squares: %f" % b4.inertia_)
for i in range(a1):
    print("Centroid%d %s" % (i + 1, b6[i]))
plt.figure(b7 = (10, 6))
plt.scatter(b2['latitude'], b2['longitude'], b8 = b5, s=50, cmap='viridis')
plt.scatter(b6[:, 0], b6[:, 1], b8 = 'red', marker='*', s=200, alpha=0.5)
plt.title("Latitude vs. Longitude")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.savefig('Latitude-Longitude.jpg')
plt.show()