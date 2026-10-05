import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, fcluster
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b10, names):
    plt.figure()
    plt.subplot(211)
    for (x, y), name in zip(b10, names):
        plt.scatter(x, y)
        plt.text(x, y, name, b1 = 6)
    plt.title('Countries')
    plt.grid(True)
    plt.gca().get_yaxis().set_ticks([])
    plt.gca().get_xaxis().set_ticks([])
def fonk3(b10, b2 = 4):
    b3 = pdist(b10, 'euclidean')
    b4 = linkage(b3, method='single')
    return fcluster(b4, b5 = b2, criterion='maxclust')
def fonk4(b10, b12):
    b6 = ['r', 'g', 'b', 'm']
    plt.subplot(212)
    for color, cluster_id in zip(b6, np.unique(b12)):
        b7 = cluster_id == b12
        plt.scatter(b10[b7, 0], b10[b7, 1], b8 = color)
    plt.title('Clusters')
    plt.grid(True)
    plt.gca().get_yaxis().set_ticks([])
    plt.gca().get_xaxis().set_ticks([])
def fonk5():
    b9 = fonk1('final_countries_data.csv')
    b10 = b9[['x-coord', 'y-coord']].values
    b11 = b9['CountryName'].values
    fonk2(b10, b11)
    b12 = fonk3(b10)
    fonk4(b10, b12)
    plt.tight_layout()
    plt.show()
if b13 = = "__main__":
    fonk5()