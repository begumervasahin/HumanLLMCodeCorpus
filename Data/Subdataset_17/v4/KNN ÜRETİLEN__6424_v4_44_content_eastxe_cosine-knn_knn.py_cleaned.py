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
        X = np.array([X]).reshape(-1, 1)
        distances = []
        for data_point in self.data:
            sim = pairwise_distances(X, data_point.reshape(1, -1), metric='cosine')
            heapq.heappush(distances, (float(sim), data_point))
        nearest_labels = []
        for _ in range(self.n_neighbors):
            min_sim, vector = heapq.heappop(distances)
            for idx, item in enumerate(self.data):
                if np.array_equal(item, vector):
                    nearest_labels.append(self.labels[idx])
                    break
        label_count = {}
        for label in nearest_labels:
            if label in label_count:
                label_count[label] += 1
            else:
                label_count[label] = 1
        y_pred = max(label_count.items(), key=lambda item: item[1])[0]
        return y_pred
if __name__ == '__main__':
    knn = CosineKNN(n_neighbors=2)
    X = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    y = [1, 1, 0, 0]
    knn.fit(X, y)
    print('Answer:', knn.predict([0.7, 0.7]))
    print('Answer:', knn.predict([-0.7, -0.7]))