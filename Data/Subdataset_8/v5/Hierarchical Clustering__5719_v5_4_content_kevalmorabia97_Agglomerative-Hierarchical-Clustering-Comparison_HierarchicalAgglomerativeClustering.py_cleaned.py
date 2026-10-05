from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
num_clusters = 3
with open('data/random_3_clusters.txt', 'r') as file:
    data = []
    true_labels = []
    for line in file:
        line_data = line.strip().split(',')
        tmp_data = [float(value) for value in line_data]
        data.append(tmp_data[:-1])
        true_labels.append(int(tmp_data[-1]))
normalized_data = normalize(data, axis=0)
pca = PCA(n_components=2)
transformed_data = pca.fit_transform(normalized_data)
linkage_methods = ['complete', 'average', 'ward', 'actual_data']
num_subplots = len(linkage_methods)
plt.figure(figsize=(10, 10))
for i, linkage_method in enumerate(linkage_methods):
    plt.subplot(1, num_subplots, i + 1)
    if linkage_method == 'actual_data':
        labels = true_labels
    else:
        model = AgglomerativeClustering(linkage=linkage_method, n_clusters=num_clusters)
        labels = model.fit_predict(transformed_data)
    plt.scatter(transformed_data[:, 0], transformed_data[:, 1], c=labels)
    plt.title('Linkage Method: %s' % linkage_method)
plt.show()