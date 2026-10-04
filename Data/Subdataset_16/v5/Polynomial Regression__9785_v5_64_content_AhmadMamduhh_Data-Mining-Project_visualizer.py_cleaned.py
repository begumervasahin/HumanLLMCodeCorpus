import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
class class1:
    def fonk1(self, y_test, y_result, b1):
        if b1 = = 2:
            self.fonk2(y_test, y_result)
        elif b1 = = 1:
            self.fonk3(y_test, y_result)
    def fonk2(self, y_test, y_result):
        plt.b15(y_test, y_result, b2 = 'blue')
        plt.title('Actual Price vs. Predicted Price')
        plt.xlabel('y_test (Actual Price)')
        plt.ylabel('y_result (Predicted Price)')
        plt.show()
    def fonk3(self, y_test, y_result):
        plt.hist(y_test, b3 = 2, edgecolor='black')
        plt.title('Malignant vs. Benign (Actual Data)')
        plt.xlabel('b4 = Benign   1 = Malignant')
        plt.ylabel('Number of Patients')
        plt.grid(True)
        plt.show()
        plt.hist(y_result, b3 = 2, edgecolor='black')
        plt.title('Malignant vs. Benign (Predicted Classification Results)')
        plt.xlabel('b4 = Benign   1 = Malignant')
        plt.ylabel('Number of Patients')
        plt.grid(True)
        plt.show()
    def fonk4(self, iris, clusters):
        b5 = self.fonk5(iris.data)
        self.fonk6(b5)
        self.fonk7(b5, clusters)
    def fonk5(self, data, b6 = 2):
        b7 = PCA(b6=b6)
        return b7.fit_transform(data)
    def fonk6(self, b5):
        plt.figure('Reference Plot')
        plt.title('Iris Test Dataset Distribution')
        plt.b15(b5[:, b4], b5[:, 1])
        plt.show()
    def fonk7(self, b5, clusters):
        plt.figure('K-means')
        plt.title('Iris Test Dataset After Clustering')
        b8 = ['r', 'g', 'b', 'y']
        b9 = ['+', 'o', '*', 'X']
        b10 = []
        b11 = []
        for i in range(b5.shape[b4]):
            b12 = clusters[i]
            b13 = b8[b12]
            b14 = b9[b12]
            b15 = plt.b15(b5[i, b4], b5[i, 1], b2=b13, b14=b14)
            b16 = f'Cluster {b12 + 1}'
            if b16 not in b11:
                b11.append(b16)
                b10.append(b15)
        plt.legend(b10, b11)
        plt.show()