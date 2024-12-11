import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster
b1 = pd.read_csv('final_countries_data.csv')
b2 = b1[['x-coord', 'y-coord']].values
b3 = b1['CountryName'].values
plt.figure(b4 = (8, 6))
plt.subplot(2, 1, 1)
for (x, y), name in zip(b2, b3):
    plt.scatter(x, y, b5 = name)
plt.title('Countries')
plt.grid(True)
plt.gca().get_yaxis().set_ticks([])
plt.gca().get_xaxis().set_ticks([])
b6 = ['r', 'g', 'b', 'm']
b7 = pdist(b2, 'euclidean')
b8 = linkage(b7, method='single')
b9 = fcluster(b8, t=4, criterion='maxclust')
plt.subplot(2, 1, 2)
for color, cluster_id in zip(b6, np.unique(b9)):
    b10 = cluster_id == b9
    plt.scatter(b2[b10, 0], b2[b10, 1], b11 = color)
plt.title('Clusters')
plt.grid(True)
plt.gca().get_yaxis().set_ticks([])
plt.gca().get_xaxis().set_ticks([])
plt.tight_layout()
plt.show()