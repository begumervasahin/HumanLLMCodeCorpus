import heapq
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
class class1():
    def fonk1(self, b1 = 5):
        self.b1 = b1
    def fonk2(self, b8, b18):
        self.b2 = np.array(b8)
        self.b3 = np.array(b18)
    def fonk3(self, b8):
        self.b4 = []
        b5 = {}
        b6 = {}
        b7 = []
        b8 = np.array([b8])
        b8.reshape(-1, 1)
        for b2 in self.b2:
            b9 = pairwise_distances(b8, np.array(b2).reshape(1, -1),
                    b10 = 'cosine')
            b5[float(b9)] = b2
            heapq.heappush(self.b4, b9)
        for i in xrange(self.b1):
            b11 = heapq.heappop(self.b4)
            b12 = b5[float(b11)]
            for index, b13 in enumerate(self.b2):
                if (b13 = = b12).all():
                    break
            b7.append(self.b3[index])
        for label in b7:
            b6[label] = 0
        for label in b7:
            b6[label] += 1
        b14 = self.fonk4(b6, max(b6.values()))
        return b14
    def fonk4(self, b6, value):
        for key, b15 in zip(b6.keys(), b6.values()):
            if b15 = = value:
                return key
if b16 = = '__main__':
    b17 = class1(b1=2)
    b8 = [[0.5, 0.86], [0.86, 0.5], [-0.5, -0.86], [-0.86, -0.5]]
    b18 = [1, 1, 0, 0]
    b17.fonk2(b8, b18)
    print 'answer:', b17.fonk3([0.7, 0.7])
    print 'answer:', b17.fonk3([-0.7, -0.7])