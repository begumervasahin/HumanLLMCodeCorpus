import pandas as pd
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, maxdists
from scipy.spatial.distance import pdist
b1 = 'Flagdata.csv'
b2 = pd.read_csv(b1)
b3 = StandardScaler()
b4 = b3.fit_transform(b2)
b5 = linkage(b4, method="average")
cophenet_corr, b6 = cophenet(b5, pdist(b4))
print('Cophenet Correlation b7 = ', cophenet_corr)
print('Cophenet pairwise b8 = ', b6)
print("First Cluster:", b5[0])
b9 = maxdists(b5)
print("Distance Array:", b9)
plt.figure(b10 = (30, 15))
plt.title('Dendrogram for Flag data')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
dendrogram(
    b5,
    b11 = 90.,
    b12 = 10.,
)
plt.show()
plt.figure(b10 = (20, 10))
dendrogram(
    b5,
    b13 = 'lastp',
    b14 = 12,
    b11 = 90.,
    b12 = 12.,
    b15 = True,
)
plt.show()