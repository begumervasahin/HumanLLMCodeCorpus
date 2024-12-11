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
fig, b6 = plt.subplots(figsize=(8, 8))
for cluster_label, color in zip(range(2), ['green', 'blue']):
    plt.scatter(b3[b4.b7 = = cluster_label, 0], b3[b4.b7 == cluster_label, 1],
                b8 = color, label=f'Cluster {cluster_label + 1}')
plt.scatter(b5[:, 0], b5[:, 1], b9 = 'X', s=100,
            b8 = 'r', label='Centroid')
plt.legend()
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('Eruption time (minutes)', b10 = 16)
plt.ylabel('Waiting time to next eruption (minutes)', b10 = 16)
plt.title('Clustered Data from Old Faithful Geyser, \n Yellowstone, USA', b10 = 20, fontweight='bold')
b6.set_aspect('equal')
plt.savefig('plot-clusters.png')