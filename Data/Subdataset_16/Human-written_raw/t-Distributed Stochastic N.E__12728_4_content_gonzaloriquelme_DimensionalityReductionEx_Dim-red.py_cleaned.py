
import os
def fonk1(path, b1 = 'train'):
    import os
    import gzip
    import numpy as np
    b2 = os.path.join(path,
                               '%s-b4-idx1-ubyte.gz'
                               % b1)
    b3 = os.path.join(path,
                               '%s-b6-idx3-ubyte.gz'
                               % b1)
    with gzip.open(b2, 'rb') as lbpath:
        b4 = np.frombuffer(lbpath.read(), dtype=np.uint8,
                               b5 = 8)
    with gzip.open(b3, 'rb') as imgpath:
        b6 = np.frombuffer(imgpath.read(), dtype=np.uint8,
                               b5 = 16).reshape(len(b4), 784)
    return b6, b4
X_train, b7 = fonk1(os.getcwd(), b1='train')
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import seaborn as sns
sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", b8 = 1.5,
                b9 = {"lines.b18": 2.5})
a1 = 123
def fonk2(x, colors):
    b10 = len(np.unique(colors))
    b11 = np.array(sns.color_palette("hls", b10))
    b12 = plt.figure(figsize=(8, 8))
    b13 = plt.subplot(aspect='equal')
    b14 = b13.scatter(x[:,0], x[:,1], lw=0, s=40, c=b11[colors.astype(np.int)])
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    b13.axis('off')
    b13.axis('tight')
    b15 = []
    for i in range(b10):
        xtext, b16 = np.median(x[colors == i, :], axis=0)
        b17 = b13.text(xtext, b16, str(i), fontsize=24)
        b17.set_path_effects([
            PathEffects.Stroke(b18 = 5, foreground="w"),
            PathEffects.Normal()])
        b15.append(b17)
    return b12, b13, b14, b15
b19 = X_train[0:20000]
b20 = b7[0:20000]
print (np.unique(b20))
from sklearn.decomposition import PCA
b21 = time.time()
b22 = PCA(n_components=4)
b23 = b22.fit_transform(b19)
print ('PCA done! Time elapsed: {} seconds'.format(time.time()-b21))
b24 = pd.DataFrame(columns = ['pca1','pca2','pca3','pca4'])
b24['pca1'] = b23[:,0]
b24['pca2'] = b23[:,1]
b24['pca3'] = b23[:,2]
b24['pca4'] = b23[:,3]
print ('Variance explained per principal component: {}'.format(b22.explained_variance_ratio_))
b25 = b24[['pca1','pca2']]
fonk2(b25.values,b20)
from sklearn.manifold import TSNE
import time
b21 = time.time()
b26 = TSNE(random_state=a1).fit_transform(b19)
print ('t-SNE done! Time elapsed: {} seconds'.format(time.time()-b21))
fonk2(b26, b20)
b21 = time.time()
b27 = PCA(n_components=50)
b28 = b27.fit_transform(b19)
print ('PCA with 50 components done! Time elapsed: {} seconds'.format(time.time()-b21))
print ('Cumulative variance explained by 50 principal components: {}'.format(np.sum(b27.explained_variance_ratio_)))
import time
b21 = time.time()
b29 = TSNE(random_state=a1).fit_transform(b28)
print ('t-SNE done! Time elapsed: {} seconds'.format(time.time()-b21))
