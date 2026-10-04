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
def fonk1(b22, b2 = 'train'):
    b3 = os.path.join(b22, f'{b2}-b5-idx1-ubyte.gz')
    b4 = os.path.join(b22, f'{b2}-b6-idx3-ubyte.gz')
    with gzip.open(b3, 'rb') as lb_path:
        b5 = np.frombuffer(lb_path.read(), dtype=np.uint8, offset=8)
    with gzip.open(b4, 'rb') as img_path:
        b6 = np.frombuffer(img_path.read(), dtype=np.uint8, offset=16).reshape(-1, 784)
    return b6, b5
def fonk2(data, b5):
    b7 = len(np.unique(b5))
    b8 = np.array(sns.color_palette("hls", b7))
    plt.figure(b9 = (8, 8))
    b10 = plt.subplot(aspect='equal')
    b11 = b10.scatter(data[:, 0], data[:, 1], lw=0, s=40, c=b8[b5.astype(int)])
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    b10.axis('off')
    b10.axis('tight')
    b12 = []
    for i in range(b7):
        x_text, b13 = np.median(data[b5 == i, :], axis=0)
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
    return b21.fit_transform(data)
def fonk5(data, b5, method_name):
    print(f"Visualizing {method_name} results...")
    fonk2(data, b5)
    plt.title(f"{method_name} Visualization")
    plt.show()
def fonk6():
    b22 = os.getcwd()
    b6, b5 = fonk1(b22, b2='train')
    a2 = 20000
    b23 = b6[:a2]
    b24 = b5[:a2]
    print("Unique b5 in the subset:", np.unique(b24))
    print("Performing PCA...")
    b25 = time.time()
    pca_results, b26 = fonk3(b23, b16=2)
    print(f"PCA completed in {time.time() - b25:.2f} seconds")
    fonk5(pca_results, b24, "PCA")
    print("Performing t-SNE...")
    b25 = time.time()
    b27 = fonk4(b23)
    print(f"t-SNE completed in {time.time() - b25:.2f} seconds")
    fonk5(b27, b24, "t-SNE")
    print("Performing PCA with 50 components...")
    b25 = time.time()
    pca_50_results, b26 = fonk3(b23, b16=50)
    print(f"PCA with 50 components completed in {time.time() - b25:.2f} seconds")
    print("Performing t-SNE on PCA-reduced data...")
    b25 = time.time()
    b28 = fonk4(pca_50_results)
    print(f"t-SNE on PCA-reduced data completed in {time.time() - b25:.2f} seconds")
    fonk5(b28, b24, "t-SNE on PCA-reduced data")
if b29 = = "__main__":
    fonk6()