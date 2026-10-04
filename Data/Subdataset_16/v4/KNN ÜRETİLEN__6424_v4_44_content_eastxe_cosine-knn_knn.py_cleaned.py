import heapq
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
class class1:
    def fonk1(self, b1 = 5):
        self.b1 = b1
    def fonk2(self, b4, b13):
        self.b2 = np.array(b4)
        self.b3 = np.array(b13)
    def fonk3(self, b4):
        b4 = np.array([b4]).reshape(-1, 1)
        b5 = []
        for data_point in self.b2:
            b6 = pairwise_distances(b4, data_point.reshape(1, -1), metric='cosine')
            heapq.heappush(b5, (float(b6), data_point))
        b7 = []
        for _ in range(self.b1):
            min_sim, b8 = heapq.heappop(b5)
            for idx, item in enumerate(self.b2):
                if np.array_equal(item, b8):
                    b7.append(self.b3[idx])
                    break
        b9 = {}
        for label in b7:
            if label in b9:
                b9[label] += 1
            else:
                b9[label] = 1
        b10 = max(b9.items(), key=lambda item: item[1])[0]
        return b10
if b11 = = '__main__':
    b12 = class1(b1=2)
    b4 = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    b13 = [1, 1, 0, 0]
    b12.fonk2(b4, b13)
    print('Answer:', b12.fonk3([0.7, 0.7]))
    print('Answer:', b12.fonk3([-0.7, -0.7]))