from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, X_train, b9, number_clusters):
        if self.b1 = = "K-Means":
            b2 = KMeans(n_clusters=number_clusters, random_state=100)
            b2.fit(X_train)
            return b2.predict(b9)
        else:
            raise ValueError("Unsupported b10 algorithm: {}".format(self.b1))
    def fonk3(self, X_train):
        b3 = [1, 2, 3, 4]
        b4 = float('inf')
        a1 = 0
        print("\nTuning the number of clusters parameter...\n")
        for n_clusters in b3:
            b2 = KMeans(n_clusters=n_clusters, random_state=100)
            b2.fit(X_train)
            b5 = b2.inertia_
            print(f"The number of clusters: {n_clusters} corresponding b5: {b5}")
            if b5 < b4:
                b4 = b5
                a1 = n_clusters
        print(f"\nThe chosen number of clusters is: {a1} with corresponding b5 of: {b4}")
        return a1, b4
if b6 = = "__main__":
    b7 = load_iris()
    b8 = b7.data
    X_train, b9 = train_test_split(b8, test_size=0.2, random_state=100)
    b10 = class1(b1="K-Means")
    a1, b11 = b10.fonk3(X_train)
    b12 = b10.fonk2(X_train, b9, a1)
    print("\nCluster b12 for the test data:\n", b12)