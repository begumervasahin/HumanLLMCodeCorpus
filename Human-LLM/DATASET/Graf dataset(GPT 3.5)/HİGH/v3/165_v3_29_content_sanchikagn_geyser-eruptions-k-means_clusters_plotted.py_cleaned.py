import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
b1 = pd.read_csv('C:/Users/Admin/PycharmProjects/GeyserEruption/resources/faithful_geyser.csv')
b2 = StandardScaler()
b3 = b2.fit_transform(b1)
b4 = KMeans(n_clusters=2, max_iter=100)
b4.fit(b3)
b5 = b4.cluster_centers_
plt.figure(b6 = (8, 8))
plt.scatter(b3[b4.b7 = = 0, 0], b3[b4.b7 == 0, 1], c='green', label='Cluster 1')
plt.scatter(b3[b4.b7 = = 1, 0], b3[b4.b7 == 1, 1], c='blue', label='Cluster 2')
plt.scatter(b5[:, 0], b5[:, 1], b8 = 'X', s=100, c='red', label='Centroid')
plt.legend()
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('Eruption time (minutes)', b9 = 16)
plt.ylabel('Waiting time to next eruption (minutes)', b9 = 16)
plt.title('Clustered Data from Old Faithful Geyser, \n Yellowstone, USA', b9 = 20, fontweight='bold')
plt.gca().set_aspect('equal', b10 = 'box')
plt.savefig('plot-clusters.png')
plt.show()