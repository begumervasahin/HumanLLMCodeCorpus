import os
import gzip
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", b1 = 1.5, rc={"lines.b15": 2.5})
a1 = 123
def fonk1(b23, b2 = 'train'):
    b3 = os.path.join(b23, f'{b2}-b5-idx1-ubyte.gz')
    b4 = os.path.join(b23, f'{b2}-b6-idx3-ubyte.gz')
    with gzip.open(b3, 'rb') as label_file:
        b5 = np.frombuffer(label_file.read(), dtype=np.uint8, offset=8)
    with gzip.open(b4, 'rb') as image_file:
        b6 = np.frombuffer(image_file.read(), dtype=np.uint8, offset=16).reshape(len(b5), 784)
    return b6, b5
def fonk2(embedding, b5):
    b7 = len(np.unique(b5))
    b8 = np.array(sns.color_palette("hls", b7))
    plt.figure(b9 = (8, 8))
    b10 = plt.subplot(aspect='equal')
    b11 = b10.b11(embedding[:, 0], embedding[:, 1], lw=0, s=40, c=b8[b5.astype(int)])
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    b10.axis('off')
    b10.axis('tight')
    b12 = []
    for i in range(b7):
        x_text, b13 = np.median(embedding[b5 == i, :], axis=0)
        b14 = b10.b14(x_text, b13, str(i), fontsize=24)
        b14.set_path_effects([PathEffects.Stroke(b15 = 5, foreground="w"), PathEffects.Normal()])
        b12.append(b14)
    return plt.gcf(), b10, b11, b12
def fonk3(data, b16 = 2):
    b17 = PCA(b16=b16)
    b18 = b17.fit_transform(data)
    b19 = b17.explained_variance_ratio_
    print(f'Variance explained by each principal component: {b19}')
    return b18, b19
def fonk4(data, b20 = a1):
    b21 = TSNE(b20=b20)
    b22 = b21.fit_transform(data)
    return b22
def fonk5():
    b23 = os.getcwd()
    X_train, b24 = fonk1(b23, b2='train')
    a2 = 20000
    b25 = X_train[:a2]
    b26 = b24[:a2]
    print("Unique b5 in the subset:", np.unique(b26))
    print("Performing PCA with 4 components...")
    b27 = time.time()
    b18, b28 = fonk3(b25, b16=4)
    print(f"PCA completed in {time.time() - b27:.2f} seconds")
    b29 = pd.DataFrame(b18, columns=['pca1', 'pca2', 'pca3', 'pca4'])
    print(f'Variance explained per principal component: {b29.var()}')
    b30 = b29[['pca1', 'pca2']]
    fonk2(b30.values, b26)
    plt.title("PCA - Top Two Components")
    plt.show()
    print("Performing t-SNE...")
    b27 = time.time()
    b22 = fonk4(b25)
    print(f"t-SNE completed in {time.time() - b27:.2f} seconds")
    fonk2(b22, b26)
    plt.title("t-SNE Visualization")
    plt.show()
    print("Performing PCA with 50 components...")
    b27 = time.time()
    pca_50_result, b28 = fonk3(b25, b16=50)
    print(f"PCA with 50 components completed in {time.time() - b27:.2f} seconds")
    print(f"Cumulative variance explained by 50 principal components: {np.sum(pca_50_result.var())}")
    print("Performing t-SNE on PCA-reduced data...")
    b27 = time.time()
    b31 = fonk4(pca_50_result)
    print(f"t-SNE on PCA-reduced data completed in {time.time() - b27:.2f} seconds")
    fonk2(b31, b26)
    plt.title("t-SNE on PCA-reduced Data")
    plt.show()
if b32 = = "__main__":
    fonk5()