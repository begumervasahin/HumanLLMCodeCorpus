import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
b1 = pd.read_csv('endometrial.csv')
b2 = b1.dropna()
b2 = b2.iloc[:, 1:]
b3 = scale(b2.T)
b4 = TSNE(n_components=2, n_iter=2500, random_state=0)
b5 = b4.fit_transform(b3)
plt.scatter(b5[:, 0], b5[:, 1])
plt.title('t-SNE Visualization of EC Dataset')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.show()