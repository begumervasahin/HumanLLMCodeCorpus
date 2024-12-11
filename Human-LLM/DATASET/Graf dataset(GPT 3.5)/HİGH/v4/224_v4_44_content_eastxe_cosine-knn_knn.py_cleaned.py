import heapq
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
class class1:
    def fonk1(self, b1 = 5):
        self.b1 = b1
    def fonk2(self, b8, y):
        self.b2 = np.array(b8)
        self.b3 = np.array(y)
    def fonk3(self, b8):
        self.b4 = []
        b5 = {}
        b6 = {}
        b7 = []
        b8 = np.array([b8])
        b8.reshape(-1, 1)
        for b2 in self.b2:
            b9 = pairwise_distances(b8, np.array(b2).reshape(1, -1), metric='cosine')
            b5[float(b9)] = b2
            heapq.heappush(self.b4, b9)
        for _ in range(self.b1):
            b10 = heapq.heappop(self.b4)
            b11 = b5[float(b10)]
            for index, b12 in enumerate(self.b2):
                if (b12 = = b11).all():
                    break
            b7.append(self.b3[index])
        for label in b7:
            b6[label] = 0
        for label in b7:
            b6[label] += 1
        b13 = self.fonk4(b6)
        return b13
    def fonk4(self, dictionary, max_value):
        for key, b14 in dictionary.items():
            if b14 = = max_value:
                return key
if b15 = = '__main__':
    b16 = class1(b1=2)
    b17 = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    b18 = [1, 1, 0, 0]
    b16.fonk2(b17, b18)
    print('Prediction for [0.7, 0.7]:', b16.fonk3([0.7, 0.7]))
    print('Prediction for [-0.7, -0.7]:', b16.fonk3([-0.7, -0.7]))