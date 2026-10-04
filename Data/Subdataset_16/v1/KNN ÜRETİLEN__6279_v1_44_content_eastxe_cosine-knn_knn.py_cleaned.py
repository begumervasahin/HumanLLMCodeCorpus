import heapq
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
class class1:
    def fonk1(self, b1 = 5):
        self.b1 = b1
    def fonk2(self, b4, b16):
        self.b2 = np.array(b4)
        self.b3 = np.array(b16)
    def fonk3(self, b4):
        b4 = np.array([b4])
        b4 = b4.reshape(1, -1)
        b5 = []
        b6 = {}
        for b2 in self.b2:
            b7 = pairwise_distances(b4, np.array(b2).reshape(1, -1), metric='cosine')
            b6[float(b7)] = b2
            heapq.heappush(b5, b7)
        b8 = []
        for _ in range(self.b1):
            b9 = heapq.heappop(b5)
            b10 = b6[float(b9)]
            for index, b11 in enumerate(self.b2):
                if (b11 = = b10).all():
                    b8.append(self.b3[index])
                    break
        b12 = {}
        for label in b8:
            if label in b12:
                b12[label] += 1
            else:
                b12[label] = 1
        b13 = max(b12, key=b12.get)
        return b13
if b14 = = '__main__':
    b15 = class1(b1=2)
    b4 = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    b16 = [1, 1, 0, 0]
    b15.fonk2(b4, b16)
    print('Answer:', b15.fonk3([0.7, 0.7]))
    print('Answer:', b15.fonk3([-0.7, -0.7]))