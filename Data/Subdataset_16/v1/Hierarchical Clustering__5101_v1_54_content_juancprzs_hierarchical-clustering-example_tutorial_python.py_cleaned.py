import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster
b1 = pd.read_csv('final_countries_data.csv')
b2 = b1[['x-coord', 'y-coord']].values
b3 = b1['CountryName'].values
plt.figure(b4 = (8, 12))
plt.subplot(211)
for (x, y), name in zip(b2, b3):
    plt.scatter(x, y)
    plt.text(x, y, name, b5 = 6)
plt.title('Countries')
plt.grid(True)
plt.gca().get_yaxis().set_ticks([])
plt.gca().get_xaxis().set_ticks([])
b6 = pdist(b2, 'euclidean')
b7 = linkage(b6, method='single')
b8 = fcluster(b7, t=4, criterion='maxclust')
b9 = ['r', 'g', 'b', 'm']
plt.subplot(212)
for color, cluster_id in zip(b9, np.unique(b8)):
    b10 = b8 == cluster_id
    plt.scatter(b2[b10, 0], b2[b10, 1], b11 = color, label=f'Cluster {cluster_id}')
plt.title('Clusters')
plt.grid(True)
plt.gca().get_yaxis().set_ticks([])
plt.gca().get_xaxis().set_ticks([])
plt.legend()
plt.tight_layout()
plt.show()