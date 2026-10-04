from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
def fonk1(b15):
    b1 = []
    b2 = []
    with open(b15, 'r') as file:
        for b3 in file:
            b3 = b3.strip().split(',')
            b4 = [float(x) for x in b3[:-1]]
            b5 = int(b3[-1])
            b1.append(b4)
            b2.append(b5)
    return b1, b2
def fonk2(b1):
    b6 = normalize(b1, axis=0)
    b7 = PCA(n_components=2)
    b8 = b7.fit_transform(b6)
    return b8
def fonk3(b16, b2, b9 = 3, no_of_subplots=4):
    plt.figure(b10 = (10, no_of_subplots))
    a1 = 0
    for b11 in ['complete', 'average', 'ward', 'actual_data']:
        if b11 = = 'actual_data':
            b12 = b2
        else:
            b13 = AgglomerativeClustering(b11=b11, b9=b9)
            b12 = b13.fit_predict(b16)
        a1 += 1
        plt.subplot(1, no_of_subplots, a1)
        plt.scatter(b16[:, 0], b16[:, 1], b14 = b12)
        plt.title(f'b11 = {b11}')
    plt.show()
def fonk4():
    b15 = 'b1/random_3_clusters.txt'
    b1, b2 = fonk1(b15)
    b16 = fonk2(b1)
    fonk3(b16, b2)
if b17 = = "__main__":
    fonk4()