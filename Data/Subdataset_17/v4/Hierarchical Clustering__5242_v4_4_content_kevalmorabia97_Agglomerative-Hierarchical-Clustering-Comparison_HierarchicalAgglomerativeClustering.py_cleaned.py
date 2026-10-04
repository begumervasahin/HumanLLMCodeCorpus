from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
def load_data(file_path):
    data = []
    labels = []
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
def plot_clusters(X, correct_labels, n_clusters=3):
    linkage_methods = ['complete', 'average', 'ward', 'actual_data']
    num_plots = len(linkage_methods)
    plt.figure(figsize=(15, 5))
    for i, linkage in enumerate(linkage_methods, start=1):
        if linkage == 'actual_data':
            labels = correct_labels
        else:
            model = AgglomerativeClustering(linkage=linkage, n_clusters=n_clusters)
            labels = model.fit_predict(X)
        plt.subplot(1, num_plots, i)
        plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
        plt.title(f'Linkage: {linkage}')
    plt.tight_layout()
    plt.show()
def main():
    file_path = 'data/random_3_clusters.txt'
    data, correct_labels = load_data(file_path)
    X = preprocess_data(data)
    plot_clusters(X, correct_labels)
if __name__ == "__main__":
    main()