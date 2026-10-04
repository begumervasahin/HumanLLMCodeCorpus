import matplotlib.pyplot as plt
from ktsne import Ktsne
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
def load_and_prepare_data(sample_size=500):
    digits = datasets.load_digits()
    X, y = shuffle(digits.data, digits.target)
    X = X[:sample_size]
    y = y[:sample_size]
    scaler = MinMaxScaler(feature_range=(-1, 1))
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y
def plot_pca(X_pca, y):
    plt.subplot(2, 1, 1)
    x_min, x_max = X_pca[:, 0].min() - 0.5, X_pca[:, 0].max() + 0.5
    y_min, y_max = X_pca[:, 1].min() - 0.5, X_pca[:, 1].max() + 0.5
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks([])
    plt.yticks([])
    plt.title("PCA without ktsne")
def plot_ktsne(X_reduced_scaled, y, kernel):
    plt.subplot(2, 1, 2)
    x_min, x_max = X_reduced_scaled[:, 0].min() - 0.5, X_reduced_scaled[:, 0].max() + 0.5
    y_min, y_max = X_reduced_scaled[:, 1].min() - 0.5, X_reduced_scaled[:, 1].max() + 0.5
    plt.scatter(X_reduced_scaled[:, 0], X_reduced_scaled[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks([])
    plt.yticks([])
    plt.title(f"ktsne with {kernel} kernel")
def main():
    X_scaled, y = load_and_prepare_data(sample_size=500)
    ktsne_options = {
        'p_degree': 2.0,
        'p_dims': 12,
        'eta': 25.0,
        'perplexity': 50.0,
        'n_dims': 2,
        'ker': 'pca',
        'gamma': 1.0
    }
    kernel = ktsne_options["ker"]
    plt.clf()
    X_pca = PCA(n_components=2).fit_transform(X_scaled)
    plot_pca(X_pca, y)
    k_tsne = Ktsne(X_scaled, f_opts=ktsne_options)
    X_reduced = k_tsne.get_solution(steps=3000)
    X_reduced_scaled = MinMaxScaler(feature_range=(-1, 1)).fit_transform(X_reduced)
    plot_ktsne(X_reduced_scaled, y, kernel)
    plt.subplots_adjust(hspace=0.5)
    plt.show()
if __name__ == "__main__":
    main()