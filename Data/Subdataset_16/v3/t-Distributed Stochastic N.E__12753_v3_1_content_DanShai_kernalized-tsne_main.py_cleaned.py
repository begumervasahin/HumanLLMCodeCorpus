import matplotlib.pyplot as plt
from ktsne import Ktsne
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
def fonk1(b1 = 500):
    b2 = datasets.load_digits()
    b4, b3 = shuffle(b2.data, b2.target)
    b4 = b4[:b1]
    b3 = b3[:b1]
    b5 = MinMaxScaler(feature_range=(-1, 1))
    b6 = b5.fit_transform(b4)
    return b6, b3
def fonk2(b12, b3):
    plt.subplot(2, 1, 1)
    x_min, b7 = b12[:, 0].min() - 0.5, b12[:, 0].max() + 0.5
    y_min, b8 = b12[:, 1].min() - 0.5, b12[:, 1].max() + 0.5
    plt.scatter(b12[:, 0], b12[:, 1], b9 = b3, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.xlim(x_min, b7)
    plt.ylim(y_min, b8)
    plt.xticks([])
    plt.yticks([])
    plt.title("PCA without ktsne")
def fonk3(b15, b3, b11):
    plt.subplot(2, 1, 2)
    x_min, b7 = b15[:, 0].min() - 0.5, b15[:, 0].max() + 0.5
    y_min, b8 = b15[:, 1].min() - 0.5, b15[:, 1].max() + 0.5
    plt.scatter(b15[:, 0], b15[:, 1], b9 = b3, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.xlim(x_min, b7)
    plt.ylim(y_min, b8)
    plt.xticks([])
    plt.yticks([])
    plt.title(f"ktsne with {b11} b11")
def fonk4():
    b6, b3 = fonk1(b1=500)
    b10 = {
        'p_degree': 2.0,
        'p_dims': 12,
        'eta': 25.0,
        'perplexity': 50.0,
        'n_dims': 2,
        'ker': 'pca',
        'gamma': 1.0
    }
    b11 = b10["ker"]
    plt.clf()
    b12 = PCA(n_components=2).fit_transform(b6)
    fonk2(b12, b3)
    b13 = Ktsne(b6, f_opts=b10)
    b14 = b13.get_solution(steps=3000)
    b15 = MinMaxScaler(feature_range=(-1, 1)).fit_transform(b14)
    fonk3(b15, b3, b11)
    plt.subplots_adjust(b16 = 0.5)
    plt.show()
if b17 = = "__main__":
    fonk4()