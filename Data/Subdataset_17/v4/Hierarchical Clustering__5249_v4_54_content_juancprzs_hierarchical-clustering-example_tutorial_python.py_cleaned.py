import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster
data = pd.read_csv('final_countries_data.csv')
coordinates = data[['x-coord', 'y-coord']].values
country_names = data['CountryName'].values
plt.figure(figsize=(8, 10))
plt.subplot(211)
for (x, y), name in zip(coordinates, country_names):
    plt.scatter(x, y, color='black')
    plt.text(x, y, name, fontsize=6)
plt.title('Countries')
plt.grid(True)
plt.xticks([])
plt.yticks([])
distance_matrix = pdist(coordinates, 'euclidean')
Z = linkage(distance_matrix, method='single')
clusters = fcluster(Z, t=4, criterion='maxclust')
cluster_colors = ['r', 'g', 'b', 'm']
plt.subplot(212)
for color, cluster_id in zip(cluster_colors, np.unique(clusters)):
    cluster_points = clusters == cluster_id
    plt.scatter(coordinates[cluster_points, 0], coordinates[cluster_points, 1], c=color, label=f'Cluster {cluster_id}')
plt.title('Clusters')
plt.grid(True)
plt.xticks([])
plt.yticks([])
plt.legend()
plt.tight_layout()
plt.show()