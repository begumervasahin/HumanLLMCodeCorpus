from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
a1 = 3
with open('b1/random_3_clusters.txt', 'r') as file:
    b1 = []
    b2 = []
    for line in file:
        b3 = line.strip().split(',')
        b4 = [float(value) for value in b3]
        b1.append(b4[:-1])
        b2.append(int(b4[-1]))
b5 = normalize(b1, axis=0)
b6 = PCA(n_components=2)
b7 = b6.fit_transform(b5)
b8 = ['complete', 'average', 'ward', 'actual_data']
b9 = len(b8)
plt.figure(b10 = (10, 10))
for i, b11 in enumerate(b8):
    plt.subplot(1, b9, i + 1)
    if b11 = = 'actual_data':
        b12 = b2
    else:
        b13 = AgglomerativeClustering(linkage=b11, n_clusters=a1)
        b12 = b13.fit_predict(b7)
    plt.scatter(b7[:, 0], b7[:, 1], b14 = b12)
    plt.title('Linkage Method: %s' % b11)
plt.show()