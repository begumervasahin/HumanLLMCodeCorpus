import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b10, b1 = 4):
    b2 = {
        'Ward': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='ward'),
        'Complete': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='complete'),
        'Average': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='average'),
        'Single': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='single')
    }
    b3 = {b8: model.fit_predict(b10) for b8, model in b2.items()}
    return b3
def fonk3(b10, b3):
    b4 = ['red', 'blue', 'green', 'yellow']
    for b8, b6 in b3.items():
        plt.figure(b5 = (10, 7))
        for i in range(4):
            plt.scatter(b10[b6 = = i, 0], b10[b6 == i, 1], s=100, c=b4[i], label=f'Cluster {i+1}')
        plt.title(f'{b8} Method')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.legend()
        plt.show()
def fonk4(b10):
    b7 = ['ward', 'complete', 'average', 'single']
    for b8 in b7:
        plt.figure(b5 = (10, 7))
        sch.dendrogram(sch.linkage(b10, b8 = b8))
        plt.title(f'{b8.capitalize()} Dendrogram')
        plt.xlabel("Data Points")
        plt.ylabel("Euclidean Distance")
        plt.show()
def fonk5():
    b9 = fonk1('customers_dataset.csv')
    b10 = b9.iloc[:, 2:8].values
    b3 = fonk2(b10)
    fonk3(b10, b3)
    fonk4(b10)
if b11 = = "__main__":
    fonk5()