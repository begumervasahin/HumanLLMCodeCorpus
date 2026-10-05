import heapq
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
class class1:
    def fonk1(self, b1 = 5):
        self.b1 = b1
    def fonk2(self, X, y):
        self.b2 = np.array(X)
        self.b3 = np.array(y)
    def fonk3(self, X):
        b4 = pairwise_distances(X.reshape(1, -1), self.b2, metric='cosine')
        b5 = np.argsort(b4.flatten())[:self.b1]
        b6 = self.b3[b5]
        unique_labels, b7 = np.unique(b6, return_counts=True)
        b8 = unique_labels[np.argmax(b7)]
        return b8
if b9 = = '__main__':
    b10 = class1(b1=2)
    b11 = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    b12 = [1, 1, 0, 0]
    b10.fonk2(b11, b12)
    print('Prediction for [0.7, 0.7]:', b10.fonk3(np.array([0.7, 0.7])))
    print('Prediction for [-0.7, -0.7]:', b10.fonk3(np.array([-0.7, -0.7])))