import heapq
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
class class1:
    def fonk1(self, b1 = 5):
        self.b1 = b1
    def fonk2(self, b4, b12):
        self.b2 = np.array(b4)
        self.b3 = np.array(b12)
    def fonk3(self, b4):
        b4 = np.array([b4])
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
            b9[label] = b9.get(label, 0) + 1
        b10 = max(b9.items(), key=lambda item: item[1])[0]
        return b10
def fonk4():
    b11 = class1(b1=2)
    b4 = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    b12 = [1, 1, 0, 0]
    b11.fonk2(b4, b12)
    print('Answer:', b11.fonk3([0.7, 0.7]))
    print('Answer:', b11.fonk3([-0.7, -0.7]))
if b13 = = '__main__':
    fonk4()