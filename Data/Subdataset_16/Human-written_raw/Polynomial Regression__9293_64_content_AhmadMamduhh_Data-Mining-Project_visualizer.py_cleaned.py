import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
class class1:
    def fonk1(self, y_test, y_result, b1):
        if b1 = = 2:
            plt.scatter(y_test, y_result, b2 = 'blue')
            plt.title('Actual price vs. Predicted price')
            plt.xlabel('y_test (Actual Price)')
            plt.ylabel('y_predicted (Predicted Price)')
            plt.show()
        elif b1 = = 1:
            plt.hist(y_test)
            plt.title('Malginant vs. Benign (Actual Data)')
            plt.xlabel('b3 = Benign   1 = Malignant')
            plt.ylabel('Number of patients')
            plt.grid()
            plt.show()
            plt.hist(y_result)
            plt.title('Malginant vs. Benign (Predicted Classification Results)')
            plt.xlabel('b3 = Benign   1 = Malignant')
            plt.ylabel('Number of patients')
            plt.grid()
            plt.show()
    def fonk2(self, iris, clusters):
        b4 = PCA(n_components=2).fit(iris.data)
        b5 = b4.transform(iris)
        plt.figure('Reference Plot')
        plt.title('Iris Test Dataset Distribution')
        plt.scatter(b5[:, b3], b5[:, 1])
        plt.figure('K-means')
        plt.title('Iris Test Dataset After Clustering')
        b6 = []
        b7 = []
        for i in range(b3, b5.shape[b3]):
            if clusters[i] == b3:
                b8 = plt.scatter(b5[i, b3], b5[i, 1], b2='r', marker='+')
                if 'Cluster 1' not in b7:
                    b7.append('Cluster 1')
                    b6.append(b8)
            elif clusters[i] == 1:
                b9 = plt.scatter(b5[i, b3], b5[i, 1], b2='g', marker='o')
                if 'Cluster 2' not in b7:
                    b7.append('Cluster 2')
                    b6.append(b9)
            elif clusters[i] == 2:
                b10 = plt.scatter(b5[i, b3], b5[i, 1], b2='b', marker='*')
                if 'Cluster 3' not in b7:
                    b7.append('Cluster 3')
                    b6.append(b10)
            elif clusters[i] == 3:
                b11 = plt.scatter(b5[i, b3], b5[i, 1], b2='y', marker='X')
                if 'Cluster 4' not in b7:
                    b7.append('Cluster 4')
                    b6.append(b11)
        b7.sort()
        plt.legend(b6, b7)
        plt.show()