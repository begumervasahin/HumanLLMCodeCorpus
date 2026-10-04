
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
sns.set()
b1 = "./yelp.csv"
b2 = pd.read_csv(b1, sep=',', quotechar='"', header=0)
b2 = b2[['b3', 'b4', 'reviewCount', 'checkins']]
b3 = b2['b3'].values
b4 = b2['b4'].values
b5 = np.array(list(zip(b3, b4)))
a1 = 4
b6 = KMeans(n_clusters=a1)
b6.fit(b5)
b7 = b6.predict(b5)
b8 = b6.cluster_centers_
print(f"Within-cluster sum of squares: {b6.inertia_}")
for i, centroid in enumerate(b8, b9 = 1):
    print(f"Centroid {i}: {centroid}")
plt.scatter(b5[:, 0], b5[:, 1], b10 = b7, s=50, cmap='viridis')
plt.scatter(b8[:, 0], b8[:, 1], b10 = 'red', marker='*', s=200, alpha=0.5)
plt.title("Latitude vs. Longitude")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.savefig('Latitude-Longitude.jpg')
plt.show()
