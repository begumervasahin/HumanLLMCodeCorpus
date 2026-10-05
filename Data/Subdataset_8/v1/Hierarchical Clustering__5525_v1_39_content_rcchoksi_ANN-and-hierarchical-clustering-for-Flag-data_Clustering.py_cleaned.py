import pandas as pd
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, maxdists
from scipy.spatial.distance import pdist
file = 'Flagdata.csv'
df = pd.read_csv(file)
scaler = StandardScaler()
scaler.fit(df)
data = scaler.transform(df)
z = linkage(data, "average")
c, coph_dists = cophenet(z, pdist(data))
print('Cophenet Correlation coefficient = ', c)
print('Cophenet pairwise distances = ', coph_dists)
print("1st Cluster is ", z[0])
m = maxdists(z)
print("Distance Array ", m)
plt.figure(figsize=(30, 15))
plt.title('Dendrogram for Flag data')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
dendrogram(
    z,
    leaf_rotation=90.,
    leaf_font_size=10.,
)
plt.show()
plt.figure(figsize=(20, 10))
dendrogram(
    z,
    truncate_mode='lastp',
    p=12,
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,
)
plt.show()