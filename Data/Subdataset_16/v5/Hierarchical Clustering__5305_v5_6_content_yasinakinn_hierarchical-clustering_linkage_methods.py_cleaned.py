import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
b1 = pd.read_csv('customers_dataset.csv')
b2 = b1.iloc[:, 2:8].values
b3 = {
    'Ward': AgglomerativeClustering(b4 = 4, affinity='euclidean', linkage='ward'),
    'Complete': AgglomerativeClustering(b4 = 4, affinity='euclidean', linkage='complete'),
    'Average': AgglomerativeClustering(b4 = 4, affinity='euclidean', linkage='average'),
    'Single': AgglomerativeClustering(b4 = 4, affinity='euclidean', linkage='single')
}
b5 = {name: algo.fit_predict(b2) for name, algo in b3.items()}
b6 = ['red', 'blue', 'green', 'yellow']
def fonk1(b2, b5, b6):
    for method_name, b8 in b5.items():
        plt.figure(b7 = (10, 7))
        for cluster_index, color in enumerate(b6):
            plt.scatter(b2[b8 = = cluster_index, 0], b2[b8 == cluster_index, 1],
                        b9 = 100, c=color, label=f'Cluster {cluster_index + 1}')
        plt.title(f'{method_name} Clustering')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.legend()
        plt.show()
def fonk2(b2, methods):
    for b10 in methods:
        plt.figure(b7 = (10, 7))
        sch.dendrogram(sch.linkage(b2, b10 = b10.lower()))
        plt.title(f'{b10} Dendrogram')
        plt.xlabel("Data Points")
        plt.ylabel("Euclidean Distance")
        plt.show()
fonk1(b2, b5, b6)
fonk2(b2, b3.keys())