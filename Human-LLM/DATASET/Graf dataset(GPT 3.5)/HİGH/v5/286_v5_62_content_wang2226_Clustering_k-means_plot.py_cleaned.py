
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
sns.set()
b1 = "./yelp.csv"
b2 = pd.read_csv(b1, sep=',', quotechar='"', header=0)
b3 = ['b4', 'b5', 'reviewCount', 'checkins']
b2 = b2[b3]
b4 = b2['b4'].values
b5 = b2['b5'].values
b6 = np.column_stack((b4, b5))
a1 = 4
b7 = KMeans(n_clusters=a1)
b7.fit(b6)
b8 = b7.labels_
b9 = b7.cluster_centers_
print("Within-cluster sum of squares: %f" % b7.inertia_)
for i, centroid in enumerate(b9):
    print(f"Centroid {i+1}: {centroid}")
plt.scatter(b6[:, 0], b6[:, 1], b10 = b8, s=50, cmap='viridis')
plt.scatter(b9[:, 0], b9[:, 1], b10 = 'red', marker='*', s=200, alpha=0.5)
plt.title("Latitude vs. Longitude")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.savefig('Latitude-Longitude.jpg')
plt.show()
