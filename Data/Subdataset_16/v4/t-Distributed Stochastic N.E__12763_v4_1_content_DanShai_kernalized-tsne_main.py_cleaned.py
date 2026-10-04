import matplotlib.pyplot as plt
from ktsne import Ktsne
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
def fonk1(dataset, b1 = 500):
    b3, b2 = shuffle(dataset.data, dataset.target)
    b3 = b3[:b1]
    b2 = b2[:b1]
    b4 = MinMaxScaler(feature_range=(-1, 1))
    b5 = b4.fit_transform(b3)
    return b5, b2
def fonk2(b3, b2):
    b6 = PCA(n_components=2).fit_transform(b3)
    x_min, b7 = b6[:, 0].min() - 0.5, b6[:, 0].max() + 0.5
    y_min, b8 = b6[:, 1].min() - 0.5, b6[:, 1].max() + 0.5
    plt.subplot(2, 1, 1)
    plt.scatter(b6[:, 0], b6[:, 1], b9 = b2, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.xlim(x_min, b7)
    plt.ylim(y_min, b8)
    plt.xticks([])
    plt.yticks([])
    plt.title("PCA without ktsne")
def fonk3(b3, b2, b15, b10 = 3000):
    b11 = Ktsne(b3, b15=b15)
    b12 = b11.get_solution(b10)
    b13 = MinMaxScaler(feature_range=(-1, 1)).fit_transform(b12)
    x_min, b7 = b13[:, 0].min() - 0.5, b13[:, 0].max() + 0.5
    y_min, b8 = b13[:, 1].min() - 0.5, b13[:, 1].max() + 0.5
    plt.subplot(2, 1, 2)
    plt.scatter(b13[:, 0], b13[:, 1], b9 = b2, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.xlim(x_min, b7)
    plt.ylim(y_min, b8)
    plt.xticks([])
    plt.yticks([])
    plt.title(f"With ktsne ({b15['ker']} kernel)")
def fonk4():
    b14 = datasets.load_digits()
    b5, b2 = fonk1(b14)
    b15 = {
        'p_degree': 2.0,
        'p_dims': 12,
        'eta': 25.0,
        'perplexity': 50.0,
        'n_dims': 2,
        'ker': 'pca',
        'gamma': 1.0
    }
    plt.clf()
    fonk2(b5, b2)
    fonk3(b5, b2, b15)
    plt.subplots_adjust(b16 = 0.5)
    plt.show()
if b17 = = "__main__":
    fonk4()