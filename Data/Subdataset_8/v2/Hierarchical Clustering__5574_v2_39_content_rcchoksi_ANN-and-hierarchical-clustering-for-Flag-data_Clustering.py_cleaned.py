import pandas as pd
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, maxdists
from scipy.spatial.distance import pdist
file = 'Flagdata.csv'
df = pd.read_csv(file)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
linkage_matrix = linkage(scaled_data, method="average")
cophenet_corr, cophenet_distances = cophenet(linkage_matrix, pdist(scaled_data))
print('Cophenet Correlation coefficient =', cophenet_corr)
print('Cophenet pairwise distances =', cophenet_distances)
print("First Cluster:", linkage_matrix[0])
max_distances = maxdists(linkage_matrix)
print("Distance Array:", max_distances)
plt.figure(figsize=(30, 15))
plt.title('Dendrogram for Flag data')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
dendrogram(
    linkage_matrix,
    leaf_rotation=90.,
    leaf_font_size=10.,
)
plt.show()
plt.figure(figsize=(20, 10))
dendrogram(
    linkage_matrix,
    truncate_mode='lastp',
    p=12,
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,
)
plt.show()