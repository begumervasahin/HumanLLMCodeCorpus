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
b5 = {b9: model.fit_predict(b2) for b9, model in b3.items()}
b6 = ['red', 'blue', 'green', 'yellow']
for b9, b8 in b5.items():
    plt.figure(b7 = (10, 7))
    for i, color in enumerate(b6):
        plt.scatter(b2[b8 = = i, 0], b2[b8 == i, 1], s=100, c=color, label=f'Cluster {i + 1}')
    plt.title(f'{b9} Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.show()
for b9 in b3.keys():
    plt.figure(b7 = (10, 7))
    sch.dendrogram(sch.linkage(b2, b9 = b9.lower()))
    plt.title(f'{b9} Dendrogram')
    plt.xlabel("Data Points")
    plt.ylabel("Euclidean Distance")
    plt.show()