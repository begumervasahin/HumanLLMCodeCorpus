from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
def fonk1(b14):
    b1 = []
    b2 = []
    with open(b14, 'r') as file:
        for line in file:
            b3 = list(map(float, line.strip().split(',')))
            b1.append(b3[:-1])
            b2.append(int(b3[-1]))
    return b1, b2
def fonk2(b1):
    b4 = normalize(b1, axis=0)
    b5 = PCA(n_components=2)
    return b5.fit_transform(b4)
def fonk3(b16, b15, b6 = 3):
    b7 = ['complete', 'average', 'ward', 'actual_data']
    b8 = len(b7)
    plt.figure(b9 = (15, 5))
    for i, b11 in enumerate(b7, b10 = 1):
        if b11 = = 'actual_data':
            b2 = b15
        else:
            b12 = AgglomerativeClustering(b11=b11, b6=b6)
            b2 = b12.fit_predict(b16)
        plt.subplot(1, b8, i)
        plt.scatter(b16[:, 0], b16[:, 1], b13 = b2, cmap='viridis')
        plt.title(f'Linkage: {b11}')
    plt.tight_layout()
    plt.show()
def fonk4():
    b14 = 'b1/random_3_clusters.txt'
    b1, b15 = fonk1(b14)
    b16 = fonk2(b1)
    fonk3(b16, b15)
if b17 = = "__main__":
    fonk4()