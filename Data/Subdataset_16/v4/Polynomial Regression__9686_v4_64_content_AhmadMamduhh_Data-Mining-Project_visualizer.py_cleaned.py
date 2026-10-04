import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
class class1:
    def fonk1(self, y_test, y_result, b1):
        if b1 = = 2:
            plt.b14(y_test, y_result, b2 = 'blue')
            plt.title('Actual price vs. Predicted price')
            plt.xlabel('y_test (Actual Price)')
            plt.ylabel('y_result (Predicted Price)')
            plt.show()
        elif b1 = = 1:
            plt.hist(y_test, b3 = 2, edgecolor='black')
            plt.title('Malignant vs. Benign (Actual Data)')
            plt.xlabel('b4 = Benign   1 = Malignant')
            plt.ylabel('Number of patients')
            plt.grid(True)
            plt.show()
            plt.hist(y_result, b3 = 2, edgecolor='black')
            plt.title('Malignant vs. Benign (Predicted Classification Results)')
            plt.xlabel('b4 = Benign   1 = Malignant')
            plt.ylabel('Number of patients')
            plt.grid(True)
            plt.show()
    def fonk2(self, iris, clusters):
        b5 = PCA(n_components=2).fit(iris.data)
        b6 = b5.transform(iris.data)
        plt.figure('Reference Plot')
        plt.title('Iris Test Dataset Distribution')
        plt.b14(b6[:, b4], b6[:, 1])
        plt.show()
        plt.figure('K-means')
        plt.title('Iris Test Dataset After Clustering')
        b7 = ['r', 'g', 'b', 'y']
        b8 = ['+', 'o', '*', 'X']
        b9 = []
        b10 = []
        for i in range(b6.shape[b4]):
            b11 = clusters[i]
            b12 = b7[b11]
            b13 = b8[b11]
            b14 = plt.b14(b6[i, b4], b6[i, 1], b2=b12, b13=b13)
            b15 = f'Cluster {b11 + 1}'
            if b15 not in b10:
                b10.append(b15)
                b9.append(b14)
        plt.legend(b9, b10)
        plt.show()