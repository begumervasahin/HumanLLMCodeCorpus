import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b11, b1 = 4):
    b2 = {
        'Ward': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='ward'),
        'Complete': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='complete'),
        'Average': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='average'),
        'Single': AgglomerativeClustering(b1 = b1, affinity='euclidean', linkage='single')
    }
    b3 = {method_name: algorithm.fit_predict(b11) for method_name, algorithm in b2.items()}
    return b3
def fonk3(b11, b3, b1 = 4):
    b4 = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    for method_name, b6 in b3.items():
        plt.figure(b5 = (10, 7))
        for cluster_index in range(b1):
            plt.scatter(b11[b6 = = cluster_index, 0], b11[b6 == cluster_index, 1],
                        b7 = 100, c=b4[cluster_index], label=f'Cluster {cluster_index + 1}')
        plt.title(f'{method_name} Method')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.legend()
        plt.show()
def fonk4(b11):
    b8 = ['ward', 'complete', 'average', 'single']
    for b9 in b8:
        plt.figure(b5 = (10, 7))
        sch.dendrogram(sch.linkage(b11, b9 = b9))
        plt.title(f'{b9.capitalize()} Dendrogram')
        plt.xlabel("Data Points")
        plt.ylabel("Euclidean Distance")
        plt.show()
def fonk5():
    b10 = fonk1('customers_dataset.csv')
    b11 = b10.iloc[:, 2:8].values
    b3 = fonk2(b11)
    fonk3(b11, b3)
    fonk4(b11)
if b12 = = "__main__":
    fonk5()