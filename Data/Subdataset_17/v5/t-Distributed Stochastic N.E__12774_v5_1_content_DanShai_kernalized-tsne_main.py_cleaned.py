import matplotlib.pyplot as plt
from ktsne import Ktsne
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
def load_and_preprocess_data(dataset, sample_size=500):
    X, y = shuffle(dataset.data, dataset.target)
    X, y = X[:sample_size], y[:sample_size]
    scaler = MinMaxScaler(feature_range=(-1, 1))
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y
def plot_pca(X, y):
    X_pca = PCA(n_components=2).fit_transform(X)
    x_min, x_max = X_pca[:, 0].min() - 0.5, X_pca[:, 0].max() + 0.5
    y_min, y_max = X_pca[:, 1].min() - 0.5, X_pca[:, 1].max() + 0.5
    plt.subplot(2, 1, 1)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks([])
    plt.yticks([])
    plt.title("PCA without ktsne")
def plot_ktsne(X, y, f_opts, steps=3000):
    k_tsne = Ktsne(X, f_opts=f_opts)
    X_reduced = k_tsne.get_solution(steps)
    X_reduced_scaled = MinMaxScaler(feature_range=(-1, 1)).fit_transform(X_reduced)
    x_min, x_max = X_reduced_scaled[:, 0].min() - 0.5, X_reduced_scaled[:, 0].max() + 0.5
    y_min, y_max = X_reduced_scaled[:, 1].min() - 0.5, X_reduced_scaled[:, 1].max() + 0.5
    plt.subplot(2, 1, 2)
    plt.scatter(X_reduced_scaled[:, 0], X_reduced_scaled[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks([])
    plt.yticks([])
    plt.title(f"With ktsne ({f_opts['ker']} kernel)")
def main():
    digits = datasets.load_digits()
    X_scaled, y = load_and_preprocess_data(digits)
    f_opts = {
        'p_degree': 2.0,
        'p_dims': 12,
        'eta': 25.0,
        'perplexity': 50.0,
        'n_dims': 2,
        'ker': 'pca',
        'gamma': 1.0
    }
    plt.clf()
    plot_pca(X_scaled, y)
    plot_ktsne(X_scaled, y, f_opts)
    plt.subplots_adjust(hspace=0.5)
    plt.show()
if __name__ == "__main__":
    main()