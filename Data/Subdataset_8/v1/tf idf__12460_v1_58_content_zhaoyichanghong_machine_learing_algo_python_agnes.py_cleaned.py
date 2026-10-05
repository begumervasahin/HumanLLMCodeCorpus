import numpy as np
from scipy.spatial import distance
class Agnes:
    def fit(self, X, n_clusters):
        '''
        Parameters
        ----------
        X : shape (n_samples, n_features)
            Training data
        n_clusters : The number of clusters
        Returns
        -------
        y : shape (n_samples,)
            Predicted cluster label per sample.
        '''
        n_samples = X.shape[0]
        clusters = [[i] for i in range(n_samples)]
        for j in reversed(range(n_clusters, n_samples)):
            centers = np.array([np.mean(X[cluster], axis=0).ravel() for cluster in clusters])
            distances = distance.squareform(distance.pdist(centers))
            np.fill_diagonal(distances, np.inf)
            near_indexes = np.unravel_index(np.argmin(distances), distances.shape)
            clusters[near_indexes[0]].extend(clusters[near_indexes[1]])
            del clusters[near_indexes[1]]
        y = np.zeros(n_samples)
        for i in range(len(clusters)):
            y[clusters[i]] = i
        return y
if __name__ == "__main__":
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [10, 2], [10, 4], [10, 0]])
    agnes = Agnes()
    n_clusters = 2
    predicted_labels = agnes.fit(X, n_clusters)
    print("Predicted labels:", predicted_labels)