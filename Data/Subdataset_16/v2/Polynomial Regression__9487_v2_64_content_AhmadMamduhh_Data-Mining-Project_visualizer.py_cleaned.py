import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
class class1:
    def fonk1(self, b16, b17, b1):
        if b1 = = 2:
            plt.b12(b16, b17, b2 = 'blue')
            plt.title('Actual price vs. Predicted price')
            plt.xlabel('b16 (Actual Price)')
            plt.ylabel('y_predicted (Predicted Price)')
            plt.show()
        elif b1 = = 1:
            plt.hist(b16, b3 = 2, alpha=b4.7, label='Actual')
            plt.hist(b17, b3 = 2, alpha=b4.7, label='Predicted')
            plt.title('Malignant vs. Benign (Classification Results)')
            plt.xlabel('b4 = Benign   1 = Malignant')
            plt.ylabel('Number of patients')
            plt.legend()
            plt.grid()
            plt.show()
    def fonk2(self, iris_data, b20):
        b5 = PCA(n_components=2).fit(iris_data.data)
        b6 = b5.transform(iris_data.data)
        plt.figure('Reference Plot')
        plt.title('Iris Test Dataset Distribution')
        plt.b12(b6[:, b4], b6[:, 1])
        plt.figure('K-means')
        plt.title('Iris Test Dataset After Clustering')
        b7 = ['r', 'g', 'b', 'y']
        b8 = ['+', 'o', '*', 'X']
        b9 = []
        b10 = []
        for i in range(b6.shape[b4]):
            b11 = b20[i]
            b12 = plt.b12(b6[i, b4], b6[i, 1], b2=b7[b11], marker=b8[b11])
            b13 = f'Cluster {b11 + 1}'
            if b13 not in b10:
                b10.append(b13)
                b9.append(b12)
        plt.legend(b9, b10)
        plt.show()
if b14 = = "__main__":
    b15 = class1()
    b16 = [b4, b4, 1, 1, b4, 1, b4, 1]
    b17 = [b4, 1, 1, 1, b4, b4, b4, 1]
    b15.fonk1(b16, b17, b1 = 1)
    b18 = load_iris()
    b19 = KMeans(n_clusters=3, random_state=42)
    b19.fit(b18.data)
    b20 = b19.predict(b18.data)
    b15.fonk2(b18, b20)