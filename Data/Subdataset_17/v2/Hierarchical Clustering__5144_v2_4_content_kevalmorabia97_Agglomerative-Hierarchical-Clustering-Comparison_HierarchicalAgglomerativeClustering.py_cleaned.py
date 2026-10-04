from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
def load_data(file_path):
    data = []
    labels = []
    with open(file_path, 'r') as file:
        for line in file:
            line_data = line.strip().split(',')
            features = [float(value) for value in line_data[:-1]]
            label = int(line_data[-1])
            data.append(features)
            labels.append(label)
    return data, labels
def preprocess_data(data):
    normalized_data = normalize(data, axis=0)
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(normalized_data)
    return reduced_data
def plot_clusters(X, true_labels, n_clusters=3):
    plt.figure(figsize=(15, 5))
    linkages = ['complete', 'average', 'ward', 'actual_data']
    for index, linkage in enumerate(linkages, 1):
        if linkage == 'actual_data':
            labels = true_labels
        else:
            model = AgglomerativeClustering(linkage=linkage, n_clusters=n_clusters)
            labels = model.fit_predict(X)
        plt.subplot(1, len(linkages), index)
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