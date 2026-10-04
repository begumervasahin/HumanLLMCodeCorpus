from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
a1 = 3
b1 = open('b2/random_3_clusters.txt','r')
b2 = []
b3 = []
while True:
    b4 = b1.readline().replace("\n","")
    if b4 = ='': break
    b4 = b4.split(',')
    b5 = []
    for i in b4: b5.append(float(i))
    b2.append(b5[:-1])
    b3.append(int(b5[-1]))
b6 = normalize(b2,axis=0)
b7 = PCA(n_components=2)
b6 = b7.fit_transform(b6)
a2 = 4
plt.figure(b8 = (10, a2))
a3 = 0
for b9 in ['complete','average','ward','actual_data']:
    if b9 = ='actual_data':
        b10 = b3
    else:
        b11 = AgglomerativeClustering(b9=b9, a1=a1)
        b11.fit(b6)
        b10 = b11.labels_
    a3+=1
    plt.subplot(1, a2, a3)
    plt.scatter(b6[:, 0], b6[:, 1], b12 = b10)
    plt.title('b9 = %s' % (b9))
plt.show()