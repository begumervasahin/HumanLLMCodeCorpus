from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
def load_data(file_path):
    data = []
    correct_labels = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            features = [float(x) for x in line[:-1]]
            label = int(line[-1])
            data.append(features)
            correct_labels.append(label)
    return data, correct_labels
def preprocess_data(data):
    X_normalized = normalize(data, axis=0)
    pca = PCA(n_components=2)
    X_reduced = pca.fit_transform(X_normalized)
    return X_reduced
def plot_clusters(X, correct_labels, n_clusters=3, no_of_subplots=4):
    plt.figure(figsize=(10, no_of_subplots))
    plot_no = 0
    for linkage in ['complete', 'average', 'ward', 'actual_data']:
        if linkage == 'actual_data':
            labels = correct_labels
        else:
            model = AgglomerativeClustering(linkage=linkage, n_clusters=n_clusters)
            labels = model.fit_predict(X)
        plot_no += 1
        plt.subplot(1, no_of_subplots, plot_no)
        plt.scatter(X[:, 0], X[:, 1], c=labels)
        plt.title(f'linkage={linkage}')
    plt.show()
def main():
    file_path = 'data/random_3_clusters.txt'
    data, correct_labels = load_data(file_path)
    X = preprocess_data(data)
    plot_clusters(X, correct_labels)
if __name__ == "__main__":
    main()