
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn import preprocessing
def load_mnist(path, kind='train'):
    labels_path = os.path.join(path, '%s-labels-idx1-ubyte.gz' % kind)
    images_path = os.path.join(path, '%s-images-idx3-ubyte.gz' % kind)
    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)
    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(len(labels), 784)
    return images, labels
def fashion_scatter(x, colors):
    num_classes = len(np.unique(colors))
    palette = np.array(sns.color_palette("hls", num_classes))
    f = plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40, c=palette[colors.astype(np.int)])
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
    return f, ax, sc, txts
X_train, y_train = load_mnist(os.getcwd(), kind='train')
x_subset = X_train[0:20000]
y_subset = y_train[0:20000]
pca = PCA(n_components=4)
pca_result = pca.fit_transform(x_subset)
pca_df = pd.DataFrame(columns=['pca1', 'pca2', 'pca3', 'pca4'])
pca_df['pca1'] = pca_result[:,0]
pca_df['pca2'] = pca_result[:,1]
pca_df['pca3'] = pca_result[:,2]
pca_df['pca4'] = pca_result[:,3]
top_two_comp = pca_df[['pca1', 'pca2']]
fashion_scatter(top_two_comp.values, y_subset)
fashion_tsne = TSNE(random_state=RS).fit_transform(x_subset)
fashion_scatter(fashion_tsne, y_subset)
pca_50 = PCA(n_components=50)
pca_result_50 = pca_50.fit_transform(x_subset)
fashion_pca_tsne = TSNE(random_state=RS).fit_transform(pca_result_50)
fashion_scatter(fashion_pca_tsne, y_subset)