import matplotlib.pyplot as plt
from ktsne import Ktsne
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
def fonk1():
    b1 = datasets.load_digits()
    b3, b2 = shuffle(b1.data, b1.target)
    b3 = b3[:500]
    b2 = b2[:500]
    b4 = MinMaxScaler(feature_range=(-1, 1))
    b5 = b4.fit_transform(b3)
    return b5, b2
def fonk2(b13, b2):
    plt.subplot(2, 1, 1)
    x_min, b6 = b13[:, 0].min() - 0.5, b13[:, 0].max() + 0.5
    y_min, b7 = b13[:, 1].min() - 0.5, b13[:, 1].max() + 0.5
    plt.scatter(b13[:, 0], b13[:, 1], b8 = b2, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('p1')
    plt.ylabel('p2')
    plt.xlim(x_min, b6)
    plt.ylim(y_min, b7)
    plt.xticks(())
    plt.yticks(())
    plt.title("PCA without ktsne")
def fonk3(b16, b2, b12):
    plt.subplot(2, 1, 2)
    x1_min, b9 = b16[:, 0].min() - 0.5, b16[:, 0].max() + 0.5
    y1_min, b10 = b16[:, 1].min() - 0.5, b16[:, 1].max() + 0.5
    plt.scatter(b16[:, 0], b16[:, 1], b8 = b2, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('V1')
    plt.ylabel('V2')
    plt.xlim(x1_min, b9)
    plt.ylim(y1_min, b10)
    plt.xticks(())
    plt.yticks(())
    plt.title(f"With ktsne ({b12} b12)")
def fonk4():
    b5, b2 = fonk1()
    b11 = {
        'p_degree': 2.0,
        'p_dims': 12,
        'eta': 25.0,
        'perplexity': 50.0,
        'n_dims': 2,
        'ker': 'pca',
        'gamma': 1.0
    }
    b12 = b11["ker"]
    plt.clf()
    b13 = PCA(n_components=2).fit_transform(b5)
    fonk2(b13, b2)
    b14 = Ktsne(b5, b11=b11)
    b15 = b14.get_solution(steps=3000)
    b16 = MinMaxScaler(feature_range=(-1, 1)).fit_transform(b15)
    fonk3(b16, b2, b12)
    plt.subplots_adjust(b17 = 0.5)
    plt.show()
if b18 = = "__main__":
    fonk4()