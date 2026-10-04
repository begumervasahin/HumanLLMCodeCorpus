import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b9, b1 = 4):
    b2 = {
        'Ward': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='ward'),
        'Complete': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='complete'),
        'Average': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='average'),
        'Single': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='single')
    }
    return {b7: model.fit_predict(b9) for b7, model in b2.items()}
def fonk3(b9, b10, b1 = 4):
    b3 = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    for b7, b5 in b10.items():
        plt.figure(b4 = (10, 7))
        for i in range(b1):
            plt.scatter(b9[b5 = = i, 0], b9[b5 == i, 1], s=100, c=b3[i], label=f'Cluster {i+1}')
        plt.title(f'{b7} Method')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.legend()
        plt.show()
def fonk4(b9):
    b6 = ['ward', 'complete', 'average', 'single']
    for b7 in b6:
        plt.figure(b4 = (10, 7))
        sch.dendrogram(sch.linkage(b9, b7 = b7))
        plt.title(f'{b7.capitalize()} Dendrogram')
        plt.xlabel("Data Points")
        plt.ylabel("Euclidean Distance")
        plt.show()
def fonk5():
    b8 = fonk1('customers_dataset.csv')
    b9 = b8.iloc[:, 2:8].values
    b10 = fonk2(b9)
    fonk3(b9, b10)
    fonk4(b9)
if b11 = = "__main__":
    fonk5()