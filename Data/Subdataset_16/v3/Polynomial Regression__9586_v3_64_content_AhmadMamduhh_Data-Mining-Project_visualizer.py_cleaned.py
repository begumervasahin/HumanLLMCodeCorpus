import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
class class1:
    def fonk1(self, b16, b17, b1):
        if b1 = = 2:
            self.fonk2(b16, b17)
        elif b1 = = 1:
            self.fonk3(b16, b17)
    def fonk2(self, b16, b17):
        plt.b12(b16, b17, b2 = 'blue')
        plt.title('Actual price vs. Predicted price')
        plt.xlabel('Actual Price')
        plt.ylabel('Predicted Price')
        plt.show()
    def fonk3(self, b16, b17):
        plt.hist(b16, b3 = 2, alpha=b4.7, label='Actual')
        plt.hist(b17, b3 = 2, alpha=b4.7, label='Predicted')
        plt.title('Malignant vs. Benign (Classification Results)')
        plt.xlabel('b4 = Benign   1 = Malignant')
        plt.ylabel('Number of patients')
        plt.legend()
        plt.grid()
        plt.show()
    def fonk4(self, iris_data, b20):
        b5 = self.fonk5(iris_data.data)
        self.fonk6(b5)
        self.fonk7(b5, b20)
    def fonk5(self, data):
        b6 = PCA(n_components=2).fit(data)
        return b6.transform(data)
    def fonk6(self, b5):
        plt.figure('Reference Plot')
        plt.title('Iris Test Dataset Distribution')
        plt.b12(b5[:, b4], b5[:, 1])
        plt.show()
    def fonk7(self, b5, b20):
        plt.figure('K-means')
        plt.title('Iris Test Dataset After Clustering')
        b7 = ['r', 'g', 'b', 'y']
        b8 = ['+', 'o', '*', 'X']
        b9 = []
        b10 = []
        for i in range(b5.shape[b4]):
            b11 = b20[i]
            b12 = plt.b12(b5[i, b4], b5[i, 1], b2=b7[b11], marker=b8[b11])
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
    b15.fonk4(b18, b20)