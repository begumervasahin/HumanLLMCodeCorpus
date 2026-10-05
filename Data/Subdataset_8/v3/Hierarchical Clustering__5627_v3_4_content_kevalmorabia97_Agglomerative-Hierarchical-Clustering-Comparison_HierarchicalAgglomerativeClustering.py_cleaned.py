from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
with open('data/random_3_clusters.txt', 'r') as file:
    data = []
    correct_labels = []
    for line in file:
        line = line.strip().split(',')
        data.append([float(i) for i in line[:-1]])
        correct_labels.append(int(line[-1]))
X = normalize(data, axis=0)
pca = PCA(n_components=2)
X = pca.fit_transform(X)
linkages = ['complete', 'average', 'ward', 'actual_data']
n_clusters = 3
num_subplots = len(linkages)
plt.figure(figsize=(5 * num_subplots, 5))
for i, linkage in enumerate(linkages):
    plt.subplot(1, num_subplots, i + 1)
    if linkage == 'actual_data':
        labels = correct_labels
    else:
        model = AgglomerativeClustering(linkage=linkage, n_clusters=n_clusters)
        labels = model.fit_predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=labels)
    plt.title('Linkage Method: %s' % linkage)
plt.show()