import numpy as np
from sklearn.cluster import KMeans
class BisectingKMeans:
    def fit(self, X, n_clusters):
        '''
        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Training data.
        n_clusters : int
            The number of clusters to form.
        Returns
        -------
        y : ndarray of shape (n_samples,)
            Predicted cluster label per sample.
        '''
        n_samples = X.shape[0]
        data = X
        clusters = [np.arange(n_samples)]
        while len(clusters) < n_clusters:
            sse = [np.var(data[cluster]) for cluster in clusters]
            index_to_split = np.argmax(sse)
            data_to_split = data[clusters[index_to_split]]
            model = KMeans(n_clusters=2, random_state=0)
            label = model.fit_predict(data_to_split)
            new_clusters = [clusters[index_to_split][label == i] for i in range(2)]
            clusters[index_to_split] = new_clusters[0]
            clusters.append(new_clusters[1])
        y = np.zeros(n_samples, dtype=int)
        for i, cluster in enumerate(clusters):
            y[cluster] = i
        return y
if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.rand(100, 2)
    bkm = BisectingKMeans()
    n_clusters = 3
    labels = bkm.fit(X, n_clusters)
    print("Cluster labels:", labels)