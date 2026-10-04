import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
class class1:
    def fonk1(self, b15, b16, b1):
        if b1 = = 2:
            plt.b12(b15, b16, b2 = 'blue')
            plt.title('Actual price vs. Predicted price')
            plt.xlabel('b15 (Actual Price)')
            plt.ylabel('y_predicted (Predicted Price)')
            plt.show()
        elif b1 = = 1:
            plt.hist(b15, b3 = 2, alpha=b4.7, label='Actual')
            plt.hist(b16, b3 = 2, alpha=b4.7, label='Predicted')
            plt.title('Malignant vs. Benign (Classification Results)')
            plt.xlabel('b4 = Benign   1 = Malignant')
            plt.ylabel('Number of patients')
            plt.legend()
            plt.grid()
            plt.show()
    def fonk2(self, iris_data, b19):
        b5 = PCA(n_components=2).fit(iris_data.data)
        b6 = b5.transform(iris_data.data)
        plt.figure('Reference Plot')
        plt.title('Iris Test Dataset Distribution')
        plt.b12(b6[:, b4], b6[:, 1])
        plt.figure('K-means')
        plt.title('Iris Test Dataset After Clustering')
        b7 = []
        b8 = []
        b9 = ['r', 'g', 'b', 'y']
        b10 = ['+', 'o', '*', 'X']
        for i in range(b4, b6.shape[b4]):
            b11 = b19[i]
            b12 = plt.b12(b6[i, b4], b6[i, 1], b2=b9[b11], marker=b10[b11])
            if f'Cluster {b11 + 1}' not in b8:
                b8.append(f'Cluster {b11 + 1}')
                b7.append(b12)
        plt.legend(b7, b8)
        plt.show()
if b13 = = "__main__":
    b14 = class1()
    b15 = [b4, b4, 1, 1, b4, 1, b4, 1]
    b16 = [b4, 1, 1, 1, b4, b4, b4, 1]
    b14.fonk1(b15, b16, b1 = 1)
    b17 = load_iris()
    b18 = KMeans(n_clusters=3)
    b18.fit(b17.data)
    b19 = b18.predict(b17.data)
    b14.fonk2(b17, b19)