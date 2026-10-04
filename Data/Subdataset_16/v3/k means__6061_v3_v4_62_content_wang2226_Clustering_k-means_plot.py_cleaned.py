
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()
b1 = "./yelp.csv"
b2 = pd.read_csv(b1, sep=',', quotechar='"', header=0)
b3 = ['b4', 'b5', 'reviewCount', 'checkins']
b2 = b2[b3]
b4 = b2['b4'].values
b5 = b2['b5'].values
b6 = np.array(list(zip(b4, b5)))
a1 = 4
b7 = KMeans(n_clusters=a1)
b7.fit(b6)
b8 = b7.predict(b6)
b9 = b7.cluster_centers_
print(f"Within-cluster sum of squares: {b7.inertia_:.2f}")
for i, centroid in enumerate(b9, b10 = 1):
    print(f"Centroid {i}: {centroid}")
def fonk1(b6, b8, b9):
    plt.figure(b11 = (10, 6))
    plt.scatter(b6[:, 0], b6[:, 1], b12 = b8, s=50, cmap='viridis', label='Data Points')
    plt.scatter(b9[:, 0], b9[:, 1], b12 = 'red', marker='*', s=200, alpha=0.5, label='Centroids')
    plt.title("Clustering of Yelp Data: Latitude vs. Longitude")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.legend()
    plt.savefig('Latitude-Longitude.jpg')
    plt.show()
fonk1(b6, b8, b9)