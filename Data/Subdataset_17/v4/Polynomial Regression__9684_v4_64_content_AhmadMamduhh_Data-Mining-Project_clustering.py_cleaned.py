class Clustering:
    def __init__(self, clustering_name):
        self.clustering_name = clustering_name
    def cluster(self, X_train, X_test, number_clusters):
        if self.clustering_name == "K-Means":
            from sklearn.cluster import KMeans
            kmeans = KMeans(n_clusters=number_clusters, random_state=100)
            kmeans.fit(X_train)
            return kmeans.predict(X_test)
    def tune_parameters(self, X_train):
        from sklearn.cluster import KMeans
        n_clusters = [1, 2, 3, 4]
        min_inertia = float('inf')
        best_n_clusters = n_clusters[0]
        print("\nTuning the number of clusters parameter...\n")
        for n in n_clusters:
            kmeans = KMeans(n_clusters=n, random_state=100)
            kmeans.fit(X_train)
            inertia = kmeans.inertia_
            print(f"The number of clusters: {n}, corresponding inertia: {inertia}")
            if inertia < min_inertia:
                min_inertia = inertia
                best_n_clusters = n
        print(f"\nThe chosen number of clusters is: {best_n_clusters} with corresponding inertia of: {min_inertia}")
        return best_n_clusters, min_inertia