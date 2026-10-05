import heapq
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
class CosineKNN:
    def __init__(self, n_neighbors=5):
        self.n_neighbors = n_neighbors
    def fit(self, X, y):
        self.data = np.array(X)
        self.labels = np.array(y)
    def predict(self, X):
        distances = pairwise_distances(X.reshape(1, -1), self.data, metric='cosine')
        nearest_indices = np.argsort(distances.flatten())[:self.n_neighbors]
        neighbor_labels = self.labels[nearest_indices]
        unique_labels, label_counts = np.unique(neighbor_labels, return_counts=True)
        predicted_label = unique_labels[np.argmax(label_counts)]
        return predicted_label
if __name__ == '__main__':
    model = CosineKNN(n_neighbors=2)
    X_train = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    y_train = [1, 1, 0, 0]
    model.fit(X_train, y_train)
    print('Prediction for [0.7, 0.7]:', model.predict(np.array([0.7, 0.7])))
    print('Prediction for [-0.7, -0.7]:', model.predict(np.array([-0.7, -0.7])))