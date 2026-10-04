from sklearn.cluster import KMeans
class Clustering:
    def __init__(self, clustering_name):
        self.clustering_name = clustering_name
    def cluster(self, X_train, X_test, number_clusters):
        if self.clustering_name == "K-Means":
            return self._kmeans_cluster(X_train, X_test, number_clusters)
    def _kmeans_cluster(self, X_train, X_test, number_clusters):
        kmeans = KMeans(n_clusters=number_clusters, random_state=100)
        kmeans.fit(X_train)
        return kmeans.predict(X_test)
    def tune_parameters(self, X_train):
        n_clusters_options = [1, 2, 3, 4]
        min_inertia = float('inf')
        best_n_clusters = n_clusters_options[0]
        print("\nTuning the number of clusters parameter...\n")
        for n_clusters in n_clusters_options:
            inertia = self._calculate_inertia(X_train, n_clusters)
            print(f"The number of clusters: {n_clusters}, corresponding inertia: {inertia}")
            if inertia < min_inertia:
                min_inertia = inertia
                best_n_clusters = n_clusters
        print(f"\nThe chosen number of clusters is: {best_n_clusters} with corresponding inertia of: {min_inertia}")
        return best_n_clusters, min_inertia
    def _calculate_inertia(self, X_train, n_clusters):
        kmeans = KMeans(n_clusters=n_clusters, random_state=100)
        kmeans.fit(X_train)
        return kmeans.inertia_