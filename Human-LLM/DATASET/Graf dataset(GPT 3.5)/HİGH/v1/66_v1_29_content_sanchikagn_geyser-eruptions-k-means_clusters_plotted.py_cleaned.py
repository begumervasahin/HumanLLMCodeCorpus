import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
b1 = pd.read_csv('C:/Users/Admin/PycharmProjects/GeyserEruption/resources/faithful_geyser.csv')
b2 = StandardScaler().fit_transform(b1)
b3 = KMeans(n_clusters=2, max_iter=100)
b3.fit(b2)
b4 = b3.cluster_centers_
fig, b5 = plt.subplots(figsize=(8, 8))
plt.scatter(b2[b3.b6 = = 0, 0], b2[b3.b6 == 0, 1],
            b7 = 'green', label='cluster 1')
plt.scatter(b2[b3.b6 = = 1, 0], b2[b3.b6 == 1, 1],
            b7 = 'blue', label='cluster 2')
plt.scatter(b4[:, 0], b4[:, 1], b8 = 'X', s=100,
            b7 = 'r', label='centroid')
plt.legend()
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('Eruption time (minutes)',  b9 = 16)
plt.ylabel('Waiting time to next eruption (minutes)', b9 = 16)
plt.title('Clustered Data from Old Faithful Geyser, \n Yellowstone, USA',  b9 = 20, fontweight='bold')
b5.set_aspect('equal')
plt.savefig('plot-clusters.png')
plt.show()