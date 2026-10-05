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
        self.similarity_tree = []
        distance_dict = {}
        label_dict = {}
        nearest_labels = []
        X = np.array([X])
        X.reshape(-1, 1)
        for data in self.data:
            similarity = pairwise_distances(X, np.array(data).reshape(1, -1), metric='cosine')
            distance_dict[float(similarity)] = data
            heapq.heappush(self.similarity_tree, similarity)
        for _ in range(self.n_neighbors):
            min_similarity = heapq.heappop(self.similarity_tree)
            vector = distance_dict[float(min_similarity)]
            for index, item in enumerate(self.data):
                if (item == vector).all():
                    break
            nearest_labels.append(self.labels[index])
        for label in nearest_labels:
            label_dict[label] = 0
        for label in nearest_labels:
            label_dict[label] += 1
        y_pred = self.get_key_with_max_value(label_dict)
        return y_pred
    def get_key_with_max_value(self, dictionary, max_value):
        for key, val in dictionary.items():
            if val == max_value:
                return key
if __name__ == '__main__':
    model = CosineKNN(n_neighbors=2)
    X_train = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    y_train = [1, 1, 0, 0]
    model.fit(X_train, y_train)
    print('Prediction for [0.7, 0.7]:', model.predict([0.7, 0.7]))
    print('Prediction for [-0.7, -0.7]:', model.predict([-0.7, -0.7]))