from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
with open('b1/random_3_clusters.txt', 'r') as f:
    b1 = []
    b2 = []
    for b3 in f:
        b3 = b3.strip().split(',')
        b4 = [float(i) for i in b3]
        b1.append(b4[:-1])
        b2.append(int(b4[-1]))
b5 = normalize(b1, axis=0)
b6 = PCA(n_components=2)
b5 = b6.fit_transform(b5)
b7 = ['complete', 'average', 'ward', 'actual_data']
a1 = 3
b8 = len(b7)
plt.figure(b9 = (5 * b8, 5))
for i, b10 in enumerate(b7):
    plt.subplot(1, b8, i + 1)
    if b10 = = 'actual_data':
        b11 = b2
    else:
        b12 = AgglomerativeClustering(b10=b10, a1=a1)
        b11 = b12.fit_predict(b5)
    plt.scatter(b5[:, 0], b5[:, 1], b13 = b11)
    plt.title('b10 = %s' % b10)
plt.show()