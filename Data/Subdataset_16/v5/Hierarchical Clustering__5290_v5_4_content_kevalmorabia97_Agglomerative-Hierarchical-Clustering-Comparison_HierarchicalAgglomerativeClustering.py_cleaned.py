from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
def fonk1(b13):
    data, b1 = [], []
    with open(b13, 'r') as file:
        for line in file:
            b2 = list(map(float, line.strip().split(',')))
            data.append(b2[:-1])
            b1.append(int(b2[-1]))
    return data, b1
def fonk2(data):
    b3 = normalize(data, axis=0)
    b4 = PCA(n_components=2)
    return b4.fit_transform(b3)
def fonk3(b15, b1, b16, b5 = 3):
    b6 = len(b16)
    plt.figure(b7 = (15, 5))
    for i, b9 in enumerate(b16, b8 = 1):
        if b9 = = 'actual_data':
            b10 = b1
        else:
            b11 = AgglomerativeClustering(b9=b9, b5=b5)
            b10 = b11.fit_predict(b15)
        plt.subplot(1, b6, i)
        plt.scatter(b15[:, 0], b15[:, 1], b12 = b10, cmap='viridis')
        plt.title(f'Linkage: {b9}')
    plt.tight_layout()
    plt.show()
def fonk4():
    b13 = 'data/random_3_clusters.txt'
    data, b14 = fonk1(b13)
    b15 = fonk2(data)
    b16 = ['complete', 'average', 'ward', 'actual_data']
    fonk3(b15, b14, b16)
if b17 = = "__main__":
    fonk4()