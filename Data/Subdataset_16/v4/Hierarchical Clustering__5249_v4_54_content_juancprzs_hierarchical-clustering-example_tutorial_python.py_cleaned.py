import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster
b1 = pd.read_csv('final_countries_data.csv')
b2 = b1[['x-coord', 'y-coord']].values
b3 = b1['CountryName'].values
plt.figure(b4 = (8, 10))
plt.subplot(211)
for (x, y), name in zip(b2, b3):
    plt.scatter(x, y, b5 = 'black')
    plt.text(x, y, name, b6 = 6)
plt.title('Countries')
plt.grid(True)
plt.xticks([])
plt.yticks([])
b7 = pdist(b2, 'euclidean')
b8 = linkage(b7, method='single')
b9 = fcluster(b8, t=4, criterion='maxclust')
b10 = ['r', 'g', 'b', 'm']
plt.subplot(212)
for b5, cluster_id in zip(b10, np.unique(b9)):
    b11 = b9 == cluster_id
    plt.scatter(b2[b11, 0], b2[b11, 1], b12 = b5, label=f'Cluster {cluster_id}')
plt.title('Clusters')
plt.grid(True)
plt.xticks([])
plt.yticks([])
plt.legend()
plt.tight_layout()
plt.show()