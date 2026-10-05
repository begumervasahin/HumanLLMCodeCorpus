import matplotlib.pyplot as plt
from ktsne import Ktsne
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
def main():
    digits = datasets.load_digits()
    X = digits.data
    y = digits.target
    X, y = shuffle(X, y)
    X = X[:500]
    y = y[:500]
    scaler = MinMaxScaler(feature_range=(-1, 1))
    X_scaled = scaler.fit_transform(X)
    tsne_options = {
        'p_degree': 2.0,
        'p_dims': 12,
        'eta': 25.0,
        'perplexity': 50.0,
        'n_dims': 2,
        'kernel': 'pca',
        'gamma': 1.0
    }
    plot_original_pca(X_scaled, y)
    plot_tsne_with_ktsne(X_scaled, tsne_options)
    plt.subplots_adjust(hspace=0.5)
    plt.show()
def plot_original_pca(X_scaled, y):
    X_pca = PCA(n_components=2).fit_transform(X_scaled)
    plt.subplot(2, 1, 1)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('PCA Bileþeni 1')
    plt.ylabel('PCA Bileþeni 2')
    plt.title('t-SNE olmadan PCA')
def plot_tsne_with_ktsne(X_scaled, tsne_options):
    k_tsne = Ktsne(X_scaled, f_opts=tsne_options)
    X_reduced = k_tsne.get_solution(3000)
    scaler = MinMaxScaler(feature_range=(-1, 1))
    X_reduced = scaler.fit_transform(X_reduced)
    plt.subplot(2, 1, 2)
    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('t-SNE Bileþeni 1')
    plt.ylabel('t-SNE Bileþeni 2')
    plt.title('PCA çekirdeði ile t-SNE')
if __name__ == "__main__":
    main()