import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster
def fonk1(b15):
    b1 = pd.read_csv(b15)
    b2 = b1[['x-coord', 'y-coord']].values
    b3 = b1['CountryName'].values
    return b2, b3
def fonk2(b2, b3):
    plt.figure(b4 = (8, 10))
    plt.subplot(211)
    for (x, y), name in zip(b2, b3):
        plt.scatter(x, y, b5 = 'black')
        plt.text(x, y, name, b6 = 6)
    plt.title('Countries')
    plt.grid(True)
    plt.xticks([])
    plt.yticks([])
def fonk3(b2, b7 = 4):
    b8 = pdist(b2, 'euclidean')
    b9 = linkage(b8, method='single')
    b10 = fcluster(b9, t=b7, criterion='maxclust')
    return b10
def fonk4(b2, b10):
    b11 = ['r', 'g', 'b', 'm']
    plt.subplot(212)
    for b5, cluster_id in zip(b11, np.unique(b10)):
        b12 = b10 == cluster_id
        plt.scatter(b2[b12, 0], b2[b12, 1], b13 = b5, label=f'Cluster {cluster_id}')
    plt.title('Clusters')
    plt.grid(True)
    plt.xticks([])
    plt.yticks([])
    plt.legend()
def fonk5(b15):
    b2, b3 = fonk1(b15)
    fonk2(b2, b3)
    b10 = fonk3(b2)
    fonk4(b2, b10)
    plt.tight_layout()
    plt.show()
if b14 = = "__main__":
    b15 = 'final_countries_data.csv'
    fonk5(b15)