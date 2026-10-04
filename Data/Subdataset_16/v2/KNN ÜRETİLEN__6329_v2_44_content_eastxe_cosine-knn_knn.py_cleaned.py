import heapq
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
class class1:
    def fonk1(self, b1 = 5):
        self.b1 = b1
    def fonk2(self, b4, y):
        self.b2 = np.array(b4)
        self.b3 = np.array(y)
    def fonk3(self, b4):
        b4 = np.array(b4).reshape(1, -1)
        b5 = []
        b6 = {}
        for data_point in self.b2:
            b7 = pairwise_distances(b4, data_point.reshape(1, -1), metric='cosine')
            b6[float(b7)] = data_point
            heapq.heappush(b5, b7)
        b8 = []
        for _ in range(self.b1):
            b9 = heapq.heappop(b5)
            b10 = b6[float(b9)]
            for idx, item in enumerate(self.b2):
                if np.array_equal(item, b10):
                    b8.append(self.b3[idx])
                    break
        b11 = {}
        for label in b8:
            b11[label] = b11.get(label, 0) + 1
        b12 = max(b11, key=b11.get)
        return b12
if b13 = = '__main__':
    b14 = class1(b1=2)
    b15 = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    b16 = [1, 1, 0, 0]
    b14.fonk2(b15, b16)
    b17 = [0.7, 0.7]
    b18 = [-0.7, -0.7]
    print('Prediction for [0.7, 0.7]:', b14.fonk3(b17))
    print('Prediction for [-0.7, -0.7]:', b14.fonk3(b18))