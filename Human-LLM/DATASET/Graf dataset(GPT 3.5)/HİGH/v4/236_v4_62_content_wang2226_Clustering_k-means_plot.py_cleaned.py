
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()
b1 = "./yelp.csv"
b2 = pd.read_csv(b1, sep=',', quotechar='"', header=0)
b2 = b2[['b3', 'b4', 'reviewCount', 'b6']]
b3 = b2['b3'].values
b4 = b2['b4'].values
b5 = b2['reviewCount'].values
b6 = b2['b6'].values
b7 = np.array(list(zip(b3, b4)))
a1 = 4
b8 = KMeans(n_clusters=a1)
b8 = b8.fit(b7)
b9 = b8.predict(b7)
b10 = b8.cluster_centers_
print("Within-cluster sum of squares: %f" % b8.inertia_)
for i in range(a1):
    print("Centroid %d: %s" % (i + 1, b10[i]))
plt.scatter(b7[:, 0], b7[:, 1], b11 = b9, s=50, cmap='viridis')
plt.scatter(b10[:, 0], b10[:, 1], b11 = 'red', marker='*', s=200, alpha=0.5)
plt.title("Latitude vs. Longitude")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.savefig('Latitude-Longitude.jpg')
plt.show()
