import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster
data = pd.read_csv('final_countries_data.csv')
coordinates = data[['x-coord', 'y-coord']].values
names = data['CountryName'].values
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
for (x, y), name in zip(coordinates, names):
    plt.scatter(x, y, label=name)
plt.title('Countries')
plt.grid(True)
plt.gca().get_yaxis().set_ticks([])
plt.gca().get_xaxis().set_ticks([])
colors = ['r', 'g', 'b', 'm']
distances = pdist(coordinates, 'euclidean')
linkage_matrix = linkage(distances, method='single')
clusters = fcluster(linkage_matrix, t=4, criterion='maxclust')
plt.subplot(2, 1, 2)
for color, cluster_id in zip(colors, np.unique(clusters)):
    cluster_mask = cluster_id == clusters
    plt.scatter(coordinates[cluster_mask, 0], coordinates[cluster_mask, 1], c=color)
plt.title('Clusters')
plt.grid(True)
plt.gca().get_yaxis().set_ticks([])
plt.gca().get_xaxis().set_ticks([])
plt.tight_layout()
plt.show()