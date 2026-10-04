from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
def load_data(file_path):
    data, labels = [], []
    with open(file_path, 'r') as file:
        for line in file:
            values = list(map(float, line.strip().split(',')))
            data.append(values[:-1])
            labels.append(int(values[-1]))
    return data, labels
def preprocess_data(data):
    normalized_data = normalize(data, axis=0)
    pca = PCA(n_components=2)
    return pca.fit_transform(normalized_data)
def plot_clusters(X, true_labels, n_clusters=3):
    plt.figure(figsize=(15, 5))
    linkage_methods = ['complete', 'average', 'ward', 'actual_data']
    for i, linkage in enumerate(linkage_methods, 1):
        if linkage == 'actual_data':
            labels = true_labels
        else:
            model = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
            labels = model.fit_predict(X)
        plt.subplot(1, len(linkage_methods), i)
        plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
        plt.title(f'Linkage: {linkage}')
    plt.tight_layout()
    plt.show()
def main():
    file_path = 'data/random_3_clusters.txt'
    data, true_labels = load_data(file_path)
    X = preprocess_data(data)
    plot_clusters(X, true_labels)
if __name__ == "__main__":
    main()