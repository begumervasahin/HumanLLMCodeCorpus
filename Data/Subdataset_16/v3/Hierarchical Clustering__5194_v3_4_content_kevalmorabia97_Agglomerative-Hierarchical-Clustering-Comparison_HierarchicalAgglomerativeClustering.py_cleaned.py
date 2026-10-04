from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
def fonk1(b11):
    data, b1 = [], []
    with open(b11, 'r') as file:
        for line in file:
            b2 = list(map(float, line.strip().split(',')))
            data.append(b2[:-1])
            b1.append(int(b2[-1]))
    return data, b1
def fonk2(data):
    b3 = normalize(data, axis=0)
    b4 = PCA(n_components=2)
    return b4.fit_transform(b3)
def fonk3(b13, b12, b5 = 3):
    plt.figure(b6 = (15, 5))
    b7 = ['complete', 'average', 'ward', 'actual_data']
    for i, b8 in enumerate(b7, 1):
        if b8 = = 'actual_data':
            b1 = b12
        else:
            b9 = AgglomerativeClustering(b5=b5, b8=b8)
            b1 = b9.fit_predict(b13)
        plt.subplot(1, len(b7), i)
        plt.scatter(b13[:, 0], b13[:, 1], b10 = b1, cmap='viridis')
        plt.title(f'Linkage: {b8}')
    plt.tight_layout()
    plt.show()
def fonk4():
    b11 = 'data/random_3_clusters.txt'
    data, b12 = fonk1(b11)
    b13 = fonk2(data)
    fonk3(b13, b12)
if b14 = = "__main__":
    fonk4()