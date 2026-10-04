from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
class Clustering:
    def __init__(self, clustering_name):
        self.clustering_name = clustering_name
    def cluster(self, X_train, X_test, number_clusters):
        if self.clustering_name == "K-Means":
            model = KMeans(n_clusters=number_clusters, random_state=100)
            model.fit(X_train)
            return model.predict(X_test)
        else:
            raise ValueError("Unsupported clustering algorithm: {}".format(self.clustering_name))
    def tune_parameters(self, X_train):
        n_clusters_options = [1, 2, 3, 4]
        min_inertia = float('inf')
        best_n_clusters = 0
        print("\nTuning the number of clusters parameter...\n")
        for n_clusters in n_clusters_options:
            model = KMeans(n_clusters=n_clusters, random_state=100)
            model.fit(X_train)
            inertia = model.inertia_
            print(f"The number of clusters: {n_clusters} corresponding inertia: {inertia}")
            if inertia < min_inertia:
                min_inertia = inertia
                best_n_clusters = n_clusters
        print(f"\nThe chosen number of clusters is: {best_n_clusters} with corresponding inertia of: {min_inertia}")
        return best_n_clusters, min_inertia
if __name__ == "__main__":
    iris = load_iris()
    X = iris.data
    X_train, X_test = train_test_split(X, test_size=0.2, random_state=100)
    clustering = Clustering(clustering_name="K-Means")
    best_n_clusters, best_inertia = clustering.tune_parameters(X_train)
    predictions = clustering.cluster(X_train, X_test, best_n_clusters)
    print("\nCluster predictions for the test data:\n", predictions)