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
        X = np.array(X).reshape(1, -1)
        simtree = []
        dist_dic = {}
        for data_point in self.data:
            sim = pairwise_distances(X, data_point.reshape(1, -1), metric='cosine')
            dist_dic[float(sim)] = data_point
            heapq.heappush(simtree, sim)
        nearest_labels = []
        for _ in range(self.n_neighbors):
            min_sim = heapq.heappop(simtree)
            vector = dist_dic[float(min_sim)]
            for idx, item in enumerate(self.data):
                if np.array_equal(item, vector):
                    nearest_labels.append(self.labels[idx])
                    break
        label_count = {}
        for label in nearest_labels:
            label_count[label] = label_count.get(label, 0) + 1
        y_pred = max(label_count, key=label_count.get)
        return y_pred
if __name__ == '__main__':
    knn = CosineKNN(n_neighbors=2)
    X_train = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    y_train = [1, 1, 0, 0]
    knn.fit(X_train, y_train)
    test_sample_1 = [0.7, 0.7]
    test_sample_2 = [-0.7, -0.7]
    print('Prediction for [0.7, 0.7]:', knn.predict(test_sample_1))
    print('Prediction for [-0.7, -0.7]:', knn.predict(test_sample_2))