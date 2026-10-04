import matplotlib.pyplot as plt
from ktsne import Ktsne
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
def fonk1(dataset, b1 = 500):
    X, b2 = shuffle(dataset.data, dataset.target)
    X, b2 = X[:b1], b2[:b1]
    b3 = MinMaxScaler(feature_range=(-1, 1))
    b4 = b3.fit_transform(X)
    return b4, b2
def fonk2(X, b2):
    b5 = PCA(n_components=2).fit_transform(X)
    x_min, b6 = b5[:, 0].min() - 0.5, b5[:, 0].max() + 0.5
    y_min, b7 = b5[:, 1].min() - 0.5, b5[:, 1].max() + 0.5
    plt.subplot(2, 1, 1)
    plt.scatter(b5[:, 0], b5[:, 1], b8 = b2, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.xlim(x_min, b6)
    plt.ylim(y_min, b7)
    plt.xticks([])
    plt.yticks([])
    plt.title("PCA without ktsne")
def fonk3(X, b2, b14, b9 = 3000):
    b10 = Ktsne(X, b14=b14)
    b11 = b10.get_solution(b9)
    b12 = MinMaxScaler(feature_range=(-1, 1)).fit_transform(b11)
    x_min, b6 = b12[:, 0].min() - 0.5, b12[:, 0].max() + 0.5
    y_min, b7 = b12[:, 1].min() - 0.5, b12[:, 1].max() + 0.5
    plt.subplot(2, 1, 2)
    plt.scatter(b12[:, 0], b12[:, 1], b8 = b2, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.xlim(x_min, b6)
    plt.ylim(y_min, b7)
    plt.xticks([])
    plt.yticks([])
    plt.title(f"With ktsne ({b14['ker']} kernel)")
def fonk4():
    b13 = datasets.load_digits()
    b4, b2 = fonk1(b13)
    b14 = {
        'p_degree': 2.0,
        'p_dims': 12,
        'eta': 25.0,
        'perplexity': 50.0,
        'n_dims': 2,
        'ker': 'pca',
        'gamma': 1.0
    }
    plt.clf()
    fonk2(b4, b2)
    fonk3(b4, b2, b14)
    plt.subplots_adjust(b15 = 0.5)
    plt.show()
if b16 = = "__main__":
    fonk4()