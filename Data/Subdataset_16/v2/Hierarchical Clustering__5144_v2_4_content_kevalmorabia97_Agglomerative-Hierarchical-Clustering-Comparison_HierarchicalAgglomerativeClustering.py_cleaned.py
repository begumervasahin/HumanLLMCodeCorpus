from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
def fonk1(b15):
    b1 = []
    b2 = []
    with open(b15, 'r') as file:
        for line in file:
            b3 = line.strip().split(',')
            b4 = [float(value) for value in b3[:-1]]
            b5 = int(b3[-1])
            b1.append(b4)
            b2.append(b5)
    return b1, b2
def fonk2(b1):
    b6 = normalize(b1, axis=0)
    b7 = PCA(n_components=2)
    b8 = b7.fit_transform(b6)
    return b8
def fonk3(b17, b16, b9 = 3):
    plt.figure(b10 = (15, 5))
    b11 = ['complete', 'average', 'ward', 'actual_data']
    for index, b12 in enumerate(b11, 1):
        if b12 = = 'actual_data':
            b2 = b16
        else:
            b13 = AgglomerativeClustering(b12=b12, b9=b9)
            b2 = b13.fit_predict(b17)
        plt.subplot(1, len(b11), index)
        plt.scatter(b17[:, 0], b17[:, 1], b14 = b2, cmap='viridis')
        plt.title(f'Linkage: {b12}')
    plt.tight_layout()
    plt.show()
def fonk4():
    b15 = 'b1/random_3_clusters.txt'
    b1, b16 = fonk1(b15)
    b17 = fonk2(b1)
    fonk3(b17, b16)
if b18 = = "__main__":
    fonk4()