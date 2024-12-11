import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, maxdists
from scipy.spatial.distance import pdist
b1 = 'Flagdata.csv'
b2 = pd.read_csv(b1)
b3 = StandardScaler()
b4 = b3.fit_transform(b2)
b5 = linkage(b4, method="average")
coph_corr, b6 = cophenet(b5, pdist(b4))
print('Cophenet Correlation coefficient:', coph_corr)
print('Cophenet pairwise distances:', b6)
print("First Cluster:", b5[0])
b7 = maxdists(b5)
print("Distance Array:", b7)
plt.figure(b8 = (30, 15))
plt.title('Dendrogram for Flag Data')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
dendrogram(
    b5,
    b9 = 90.,
    b10 = 10.,
)
plt.show()
plt.figure(b8 = (20, 10))
dendrogram(
    b5,
    b11 = 'lastp',
    b12 = 12,
    b9 = 90.,
    b10 = 12.,
    b13 = True,
)
plt.show()