import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
class KNearestNeighbors:
    def fit(self, training_data, target_values, n_neighbors, distance_metric=euclidean_distances):
        '''
        Fit the K Nearest Neighbors model with the given training data.
        Parameters
        ----------
        training_data : array-like, shape (n_samples, n_features)
            The training samples.
        target_values : array-like, shape (n_samples,)
            The target labels corresponding to the training data.
        n_neighbors : int
            Number of neighbors to consider for classification.
        distance_metric : function, optional
            The distance metric to use. Default is Euclidean distance.
        '''
        self.training_data = training_data
        self.target_values = target_values
        self.n_neighbors = n_neighbors
        self.distance_metric = distance_metric
    def __predict_single_sample(self, sample):
        '''
        Predict the label for a single sample.
        Parameters
        ----------
        sample : array-like, shape (n_features,)
            The sample for which to predict the label.
        Returns
        -------
        label : int
            The predicted label for the sample.
        '''
        distances = self.distance_metric(sample.reshape(1, -1), self.training_data)
        nearest_neighbors_indices = np.argpartition(distances, self.n_neighbors - 1)[:self.n_neighbors]
        return np.argmax(np.bincount(self.target_values[nearest_neighbors_indices].astype(int)))
    def predict(self, test_data):
        '''
        Predict the labels for a set of test samples.
        Parameters
        ----------
        test_data : array-like, shape (n_samples, n_features)
            The test samples for which to predict the labels.
        Returns
        -------
        predicted_labels : array-like, shape (n_samples,)
            The predicted labels for the test samples.
        '''
        return np.apply_along_axis(self.__predict_single_sample, 1, test_data)
if __name__ == "__main__":
    training_data = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    target_values = np.array([0, 0, 1, 1])
    test_data = np.array([[1.5, 2.5], [3.5, 4.5]])
    knn_model = KNearestNeighbors()
    knn_model.fit(training_data, target_values, n_neighbors=2)
    predictions = knn_model.predict(test_data)
    print("Predictions:", predictions)