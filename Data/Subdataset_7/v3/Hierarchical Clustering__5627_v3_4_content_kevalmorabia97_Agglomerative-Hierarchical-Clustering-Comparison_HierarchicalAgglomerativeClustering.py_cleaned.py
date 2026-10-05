from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
with open('b1/random_3_clusters.txt', 'r') as file:
    b1 = []
    b2 = []
    for b3 in file:
        b3 = b3.strip().split(',')
        b1.append([float(i) for i in b3[:-1]])
        b2.append(int(b3[-1]))
b4 = normalize(b1, axis=0)
b5 = PCA(n_components=2)
b4 = b5.fit_transform(b4)
b6 = ['complete', 'average', 'ward', 'actual_data']
a1 = 3
b7 = len(b6)
plt.figure(b8 = (5 * b7, 5))
for i, b9 in enumerate(b6):
    plt.subplot(1, b7, i + 1)
    if b9 = = 'actual_data':
        b10 = b2
    else:
        b11 = AgglomerativeClustering(b9=b9, a1=a1)
        b10 = b11.fit_predict(b4)
    plt.scatter(b4[:, 0], b4[:, 1], b12 = b10)
    plt.title('Linkage Method: %s' % b9)
plt.show()