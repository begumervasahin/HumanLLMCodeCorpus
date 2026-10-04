from sklearn.cluster import KMeans
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, X_train, X_test, number_clusters):
        if self.b1 = = "K-Means":
            return self.fonk3(X_train, X_test, number_clusters)
    def fonk3(self, X_train, X_test, number_clusters):
        b2 = KMeans(n_clusters=number_clusters, random_state=100)
        b2.fit(X_train)
        return b2.predict(X_test)
    def fonk4(self, X_train):
        b3 = [1, 2, 3, 4]
        b4 = float('inf')
        b5 = b3[0]
        print("\nTuning the number of clusters parameter...\n")
        for n_clusters in b3:
            b6 = self.fonk5(X_train, n_clusters)
            print(f"The number of clusters: {n_clusters}, corresponding b6: {b6}")
            if b6 < b4:
                b4 = b6
                b5 = n_clusters
        print(f"\nThe chosen number of clusters is: {b5} with corresponding b6 of: {b4}")
        return b5, b4
    def fonk5(self, X_train, n_clusters):
        b2 = KMeans(n_clusters=n_clusters, random_state=100)
        b2.fit(X_train)
        return b2.inertia_