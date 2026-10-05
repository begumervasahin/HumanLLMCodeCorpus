import heapq
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
class class1:
    def fonk1(self, b1 = 5):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b9, y):
        self.b2 = np.array(b9)
        self.b3 = np.array(y)
    def fonk3(self, b9):
        b4 = self.fonk4(b9)
        b5 = {}
        for label in b4:
            b5[label] = b5.get(label, 0) + 1
        b6 = self.fonk5(b5)
        return b6
    def fonk4(self, b9):
        self.b7 = []
        b8 = {}
        b9 = np.array([b9])
        for b2 in self.b2:
            b10 = pairwise_distances(b9, np.array(b2).reshape(1, -1), metric='cosine')
            b8[float(b10)] = b2
            heapq.heappush(self.b7, b10)
        b4 = []
        for _ in range(self.b1):
            b11 = heapq.heappop(self.b7)
            b12 = b8[float(b11)]
            b4.append(self.b3[np.where((self.b2 = = b12).all(axis=1))[0][0]])
        return b4
    def fonk5(self, dictionary):
        b13 = max(dictionary.values())
        for key, b14 in dictionary.items():
            if b14 = = b13:
                return key
if b15 = = '__main__':
    b16 = class1(b1=2)
    b17 = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    b18 = [1, 1, 0, 0]
    b16.fonk2(b17, b18)
    print('Prediction for [0.7, 0.7]:', b16.fonk3([0.7, 0.7]))
    print('Prediction for [-0.7, -0.7]:', b16.fonk3([-0.7, -0.7]))