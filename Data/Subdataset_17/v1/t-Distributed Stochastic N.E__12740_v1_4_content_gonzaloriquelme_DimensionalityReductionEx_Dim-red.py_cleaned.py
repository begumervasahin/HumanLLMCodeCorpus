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
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
RS = 123
def load_mnist(path, kind='train'):
    labels_path = os.path.join(path, f'{kind}-labels-idx1-ubyte.gz')
    images_path = os.path.join(path, f'{kind}-images-idx3-ubyte.gz')
    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)
    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(-1, 784)
    return images, labels
def fashion_scatter(x, colors):
    num_classes = len(np.unique(colors))
    palette = np.array(sns.color_palette("hls", num_classes))
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:, 0], x[:, 1], lw=0, s=40, c=palette[colors.astype(int)])
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    ax.axis('off')
    ax.axis('tight')
    txts = []
    for i in range(num_classes):
        xtext, ytext = np.median(x[colors == i, :], axis=0)
        txt = ax.text(xtext, ytext, str(i), fontsize=24)
        txt.set_path_effects([PathEffects.Stroke(linewidth=5, foreground="w"), PathEffects.Normal()])
        txts.append(txt)
    return plt.gcf(), ax, sc, txts
def main():
    X_train, y_train = load_mnist(os.getcwd(), kind='train')
    x_subset = X_train[:20000]
    y_subset = y_train[:20000]
    print("Unique labels in subset:", np.unique(y_subset))
    print("Performing PCA...")
    start_time = time.time()
    pca = PCA(n_components=4)
    pca_result = pca.fit_transform(x_subset)
    print(f"PCA done! Time elapsed: {time.time() - start_time:.2f} seconds")
    pca_df = pd.DataFrame(pca_result, columns=['pca1', 'pca2', 'pca3', 'pca4'])
    print('Variance explained per principal component:', pca.explained_variance_ratio_)
    print("Visualizing PCA...")
    fashion_scatter(pca_df[['pca1', 'pca2']].values, y_subset)
    print("Performing t-SNE...")
    start_time = time.time()
    tsne = TSNE(random_state=RS)
    tsne_result = tsne.fit_transform(x_subset)
    print(f"t-SNE done! Time elapsed: {time.time() - start_time:.2f} seconds")
    print("Visualizing t-SNE...")
    fashion_scatter(tsne_result, y_subset)
    print("Performing PCA with 50 components...")
    start_time = time.time()
    pca_50 = PCA(n_components=50)
    pca_result_50 = pca_50.fit_transform(x_subset)
    print(f"PCA with 50 components done! Time elapsed: {time.time() - start_time:.2f} seconds")
    print('Cumulative variance explained by 50 principal components:', np.sum(pca_50.explained_variance_ratio_))
    print("Performing t-SNE on PCA results...")
    start_time = time.time()
    tsne_pca = TSNE(random_state=RS)
    tsne_pca_result = tsne_pca.fit_transform(pca_result_50)
    print(f"t-SNE done! Time elapsed: {time.time() - start_time:.2f} seconds")
    print("Visualizing t-SNE on PCA results...")
    fashion_scatter(tsne_pca_result, y_subset)
if __name__ == "__main__":
    main()