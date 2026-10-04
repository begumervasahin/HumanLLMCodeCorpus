class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, X_train, X_test, number_clusters):
        if self.b1 = = "K-Means":
            from sklearn.cluster import KMeans
            b2 = KMeans(b3=number_clusters, random_state=100)
            b2.fit(X_train)
            return b2.predict(X_test)
    def fonk3(self, X_train):
        from sklearn.cluster import KMeans
        b3 = [1, 2, 3, 4]
        b4 = float('inf')
        b5 = b3[0]
        print("\nTuning the number of clusters parameter...\n")
        for n in b3:
            b2 = KMeans(b3=n, random_state=100)
            b2.fit(X_train)
            b6 = b2.inertia_
            print(f"The number of clusters: {n}, corresponding b6: {b6}")
            if b6 < b4:
                b4 = b6
                b5 = n
        print(f"\nThe chosen number of clusters is: {b5} with corresponding b6 of: {b4}")
        return b5, b4