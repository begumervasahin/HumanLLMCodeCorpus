import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster
def fonk1(b14):
    return pd.read_csv(b14)
def fonk2(b11, names):
    plt.figure(b1 = (8, 12))
    plt.subplot(211)
    for (x, y), name in zip(b11, names):
        plt.scatter(x, y)
        plt.text(x, y, name, b2 = 6)
    plt.title('Countries')
    plt.grid(True)
    plt.xticks([])
    plt.yticks([])
def fonk3(b11, b9):
    b3 = ['r', 'g', 'b', 'm']
    plt.subplot(212)
    for color, cluster_id in zip(b3, np.unique(b9)):
        b4 = b9 == cluster_id
        plt.scatter(b11[b4, 0], b11[b4, 1], b5 = color, label=f'Cluster {cluster_id}')
    plt.title('Clusters')
    plt.grid(True)
    plt.xticks([])
    plt.yticks([])
    plt.legend()
def fonk4(b11, b6 = 4):
    b7 = pdist(b11, 'euclidean')
    b8 = linkage(b7, method='single')
    b9 = fcluster(b8, t=b6, criterion='maxclust')
    return b9
def fonk5(b14):
    b10 = fonk1(b14)
    b11 = b10[['x-coord', 'y-coord']].values
    b12 = b10['CountryName'].values
    fonk2(b11, b12)
    b9 = fonk4(b11)
    fonk3(b11, b9)
    plt.tight_layout()
    plt.show()
if b13 = = "__main__":
    b14 = 'final_countries_data.csv'
    fonk5(b14)