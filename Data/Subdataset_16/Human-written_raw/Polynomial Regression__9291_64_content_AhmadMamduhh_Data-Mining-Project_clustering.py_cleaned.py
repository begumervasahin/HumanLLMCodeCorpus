class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, X_train, X_test, number_clusters):
        if self.b1 = = "K-Means":
            from sklearn.cluster import KMeans
            b2 = KMeans(b3= number_clusters, random_state=100).fit(X_train)
            return b2.predict(X_test)
    def fonk3(self, X_train):
            ''' This method runs the training algorithm with multiple
            iterations and chooses different values for the number of clutsers
            on each iteration and calculates the inertia each time.
            The parameter value of the b4 with the lowest inertia is returned
            '''
            from sklearn.cluster import KMeans
            b3 = [1, 2, 3, 4]
            a1 = 9999
            a2 = 0
            print("\nTuning the number of clusters parameter...\n")
            for i in range(0,len(b3)):
                b4 = KMeans(b3= b3[i], random_state=100).fit(X_train)
                b5 = b4.inertia_
                print("The number of clusters: " + str(b3[i]) +
                      " corresponding inertia: " + str(b5))
                if b5 < a1:
                    a1 = b5
                    a2 = i
            print("\nThe chosen number of clusters is: " + str(b3[a2]) +
            " with corresponding inertia of: " + str(a1) )
            return b3[a2], a1