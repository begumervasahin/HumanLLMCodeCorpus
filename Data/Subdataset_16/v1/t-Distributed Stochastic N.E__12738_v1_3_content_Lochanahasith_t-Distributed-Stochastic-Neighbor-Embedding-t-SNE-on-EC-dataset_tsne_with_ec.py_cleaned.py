import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn import preprocessing
import matplotlib.pyplot as plt
def fonk1(b8):
    b1 = pd.read_csv(b8)
    b2 = b1.dropna()
    b3 = b2.iloc[:, 1:]
    b4 = preprocessing.scale(b3.T)
    return b4
def fonk2(b4, b5 = 2, n_iter=2500, random_state=0):
    b6 = TSNE(b5=b5, n_iter=n_iter, random_state=random_state)
    b7 = b6.fit_transform(b4)
    return b7
def fonk3(b7):
    plt.scatter(b7[:, 0], b7[:, 1])
    plt.xlabel('t-SNE Component 1')
    plt.ylabel('t-SNE Component 2')
    plt.title('2D t-SNE Visualization')
    plt.show()
def fonk4():
    b8 = 'endometrial.csv'
    b4 = fonk1(b8)
    b7 = fonk2(b4)
    fonk3(b7)
if b9 = = "__main__":
    fonk4()