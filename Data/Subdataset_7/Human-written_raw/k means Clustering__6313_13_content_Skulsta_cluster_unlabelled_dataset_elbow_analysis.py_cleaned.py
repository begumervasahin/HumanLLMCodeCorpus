from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
b1 = ['area', 'perimeter', 'compactness', 'lenghtOfKernel', 'widthOfKernel', 'assymetryCoefficient',
            'lengthOfKernelGrove', 'classifier']
b2 = pd.read_table("seeds_dataset.txt", index_col=False, names=b1, header=None, delimiter='\s+')
b3 = b2.values
b4 = b3[:, 7]
b5 = b3[:, :7]
b6 = PCA(n_components=2)
b6.fit(b5)
b5 = b6.transform(b5)
b7 = StandardScaler()
b8 = b7.fit_transform(b5)
b9 = range(1, 7)
b10 = []
for num_clusters in b9:
    b11 = KMeans(num_clusters)
    b11.fit(b8)
    b10.append(b11.inertia_)
b12 = pd.DataFrame({"num_clusters":b9, "b10": b10})
print(b12[0:10])
plt.figure(b13 = (12,6))
plt.plot(b12.num_clusters, b12.b10, b14 = "o")
plt.show()