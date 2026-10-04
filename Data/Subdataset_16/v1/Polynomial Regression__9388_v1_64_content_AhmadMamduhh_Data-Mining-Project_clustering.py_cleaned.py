from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, X_train, b10, number_clusters):
        if self.b1 = = "K-Means":
            b2 = KMeans(b3=number_clusters, random_state=100).fit(X_train)
            return b2.predict(b10)
    def fonk3(self, X_train):
        ''' This method runs the training algorithm with multiple
        iterations and chooses different values for the number of clusters
        on each iteration and calculates the inertia each time.
        The parameter value of the b5 with the lowest inertia is returned
        '''
        b3 = [1, 2, 3, 4]
        b4 = float('inf')
        a1 = 0
        print("\nTuning the number of clusters parameter...\n")
        for i in range(len(b3)):
            b5 = KMeans(b3=b3[i], random_state=100).fit(X_train)
            b6 = b5.inertia_
            print(f"The number of clusters: {b3[i]} corresponding inertia: {b6}")
            if b6 < b4:
                b4 = b6
                a1 = i
        print(f"\nThe chosen number of clusters is: {b3[a1]} with corresponding inertia of: {b4}")
        return b3[a1], b4
if b7 = = "__main__":
    b8 = load_iris()
    b9 = b8.data
    X_train, b10 = train_test_split(b9, test_size=0.2, random_state=100)
    b11 = class1(b1="K-Means")
    best_n_clusters, b12 = b11.fonk3(X_train)
    b13 = b11.fonk2(X_train, b10, best_n_clusters)
    print("\nCluster b13 for the test data:\n", b13)