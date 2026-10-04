import pandas as pd
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, maxdists
from scipy.spatial.distance import pdist
def fonk1(b14):
    b1 = pd.read_csv(b14)
    b2 = StandardScaler()
    b3 = b2.fit_transform(b1)
    return b3
def fonk2(data, b4 = 'average'):
    b5 = linkage(data, b4)
    coph_corr, b6 = cophenet(b5, pdist(data))
    b7 = maxdists(b5)
    return b5, coph_corr, b6, b7
def fonk3(b5, title, b8 = None, b12=None):
    plt.figure(b9 = (30, 15))
    plt.title(title)
    plt.xlabel('Sample Index')
    plt.ylabel('Distance')
    dendrogram(
        b5,
        b10 = 90.,
        b11 = 10.,
        b8 = b8,
        b12 = b12,
        b13 = True if b8 else False
    )
    plt.show()
def fonk4():
    b14 = 'Flagdata.csv'
    b3 = fonk1(b14)
    b5, coph_corr, b6, b7 = fonk2(b3)
    print(f'Cophenet Correlation Coefficient: {coph_corr}')
    print(f'Cophenet Pairwise Distances: {b6}')
    print(f'First Cluster: {b5[0]}')
    print(f'Distance Array: {b7}')
    fonk3(b5, 'Dendrogram for Flag Data')
    fonk3(b5, 'Truncated Dendrogram (Last 12 Merged Clusters)', b8 = 'lastp', b12=12)
if b15 = = "__main__":
    fonk4()