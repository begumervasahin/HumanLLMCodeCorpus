import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster
data = pd.read_csv('final_countries_data.csv')
coords = data[['x-coord', 'y-coord']].values
country_names = data['CountryName'].values
plt.figure(figsize=(8, 12))
plt.subplot(211)
for (x, y), name in zip(coords, country_names):
    plt.scatter(x, y)
    plt.text(x, y, name, fontsize=6)
plt.title('Countries')
plt.grid(True)
plt.gca().get_yaxis().set_ticks([])
plt.gca().get_xaxis().set_ticks([])
distance_matrix = pdist(coords, 'euclidean')
Z = linkage(distance_matrix, method='single')
clusters = fcluster(Z, t=4, criterion='maxclust')
cluster_colors = ['r', 'g', 'b', 'm']
plt.subplot(212)
for color, cluster_id in zip(cluster_colors, np.unique(clusters)):
    cluster_points = clusters == cluster_id
    plt.scatter(coords[cluster_points, 0], coords[cluster_points, 1], c=color, label=f'Cluster {cluster_id}')
plt.title('Clusters')
plt.grid(True)
plt.gca().get_yaxis().set_ticks([])
plt.gca().get_xaxis().set_ticks([])
plt.legend()
plt.tight_layout()
plt.show()