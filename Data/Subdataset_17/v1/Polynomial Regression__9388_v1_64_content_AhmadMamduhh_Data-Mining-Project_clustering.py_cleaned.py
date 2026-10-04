from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
class Clustering:
    def __init__(self, clustering_name):
        self.clustering_name = clustering_name
    def cluster(self, X_train, X_test, number_clusters):
        if self.clustering_name == "K-Means":
            trained_model = KMeans(n_clusters=number_clusters, random_state=100).fit(X_train)
            return trained_model.predict(X_test)
    def tune_parameters(self, X_train):
        ''' This method runs the training algorithm with multiple
        iterations and chooses different values for the number of clusters
        on each iteration and calculates the inertia each time.
        The parameter value of the model with the lowest inertia is returned
        '''
        n_clusters = [1, 2, 3, 4]
        min_inertia = float('inf')
        index = 0
        print("\nTuning the number of clusters parameter...\n")
        for i in range(len(n_clusters)):
            model = KMeans(n_clusters=n_clusters[i], random_state=100).fit(X_train)
            temp_inertia = model.inertia_
            print(f"The number of clusters: {n_clusters[i]} corresponding inertia: {temp_inertia}")
            if temp_inertia < min_inertia:
                min_inertia = temp_inertia
                index = i
        print(f"\nThe chosen number of clusters is: {n_clusters[index]} with corresponding inertia of: {min_inertia}")
        return n_clusters[index], min_inertia
if __name__ == "__main__":
    iris = load_iris()
    X = iris.data
    X_train, X_test = train_test_split(X, test_size=0.2, random_state=100)
    clustering = Clustering(clustering_name="K-Means")
    best_n_clusters, best_inertia = clustering.tune_parameters(X_train)
    predictions = clustering.cluster(X_train, X_test, best_n_clusters)
    print("\nCluster predictions for the test data:\n", predictions)