
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn import preprocessing
def fonk1(path, b1 = 'train'):
    b2 = os.path.join(path, '%s-b4-idx1-ubyte.gz' % b1)
    b3 = os.path.join(path, '%s-b5-idx3-ubyte.gz' % b1)
    with gzip.open(b2, 'rb') as lbpath:
        b4 = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)
    with gzip.open(b3, 'rb') as imgpath:
        b5 = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(len(b4), 784)
    return b5, b4
def fonk2(x, colors):
    b6 = len(np.unique(colors))
    b7 = np.array(sns.color_palette("hls", b6))
    b8 = plt.figure(figsize=(8, 8))
    b9 = plt.subplot(aspect='equal')
    b10 = b9.scatter(x[:,0], x[:,1], lw=0, s=40, c=b7[colors.astype(np.int)])
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    b9.axis('off')
    b9.axis('tight')
    b11 = []
    for i in range(b6):
        xtext, b12 = np.median(x[colors == i, :], axis=0)
        b13 = b9.text(xtext, b12, str(i), fontsize=24)
        b13.set_path_effects([PathEffects.Stroke(b14 = 5, foreground="w"), PathEffects.Normal()])
        b11.append(b13)
    return b8, b9, b10, b11
X_train, b15 = fonk1(os.getcwd(), b1='train')
b16 = X_train[0:20000]
b17 = b15[0:20000]
b18 = PCA(n_components=4)
b19 = b18.fit_transform(b16)
b20 = pd.DataFrame(columns=['pca1', 'pca2', 'pca3', 'pca4'])
b20['pca1'] = b19[:,0]
b20['pca2'] = b19[:,1]
b20['pca3'] = b19[:,2]
b20['pca4'] = b19[:,3]
b21 = b20[['pca1', 'pca2']]
fonk2(b21.values, b17)
b22 = TSNE(random_state=RS).fit_transform(b16)
fonk2(b22, b17)
b23 = PCA(n_components=50)
b24 = b23.fit_transform(b16)
b25 = TSNE(random_state=RS).fit_transform(b24)
fonk2(b25, b17)