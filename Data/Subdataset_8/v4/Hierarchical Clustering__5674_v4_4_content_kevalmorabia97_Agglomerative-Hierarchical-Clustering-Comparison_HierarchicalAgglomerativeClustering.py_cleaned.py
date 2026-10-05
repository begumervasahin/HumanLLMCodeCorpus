from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
n_clusters = 3
with open('data/random_3_clusters.txt', 'r') as file:
    data = []
    correct_labels = []
    for line in file:
        line = line.strip().split(',')
        tmp = [float(i) for i in line]
        data.append(tmp[:-1])
        correct_labels.append(int(tmp[-1]))
X = normalize(data, axis=0)
pca = PCA(n_components=2)
X = pca.fit_transform(X)
linkage_methods = ['complete', 'average', 'ward', 'actual_data']
num_subplots = len(linkage_methods)
plt.figure(figsize=(10, 10))
for i, linkage in enumerate(linkage_methods):
    plt.subplot(1, num_subplots, i + 1)
    if linkage == 'actual_data':
        labels = correct_labels
    else:
        model = AgglomerativeClustering(linkage=linkage, n_clusters=n_clusters)
        labels = model.fit_predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=labels)
    plt.title('Linkage Method: %s' % linkage)
plt.show()