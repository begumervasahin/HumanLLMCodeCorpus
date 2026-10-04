import heapq
from collections import namedtuple, defaultdict
b1 = namedtuple('b1', ['b7', 'weight'])
class class1:
    def fonk1(self, b2):
        self.b2 = b2
        self.b3 = ['unseen'] * b2
        self.b4 = [float('-inf')] * b2
        self.b5 = [None] * b2
        self.b6 = defaultdict(list)
    def fonk2(self, u, v, weight):
        self.b6[u].append(b1(b7 = v, weight=weight))
        self.b6[v].append(b1(b7 = u, weight=weight))
    def fonk3(self, b8, b7, weight):
        heapq.heappush(b8, (-weight, b7))
    def fonk4(self, b8):
        weight, b7 = heapq.heappop(b8)
        return -weight, b7
    def fonk5(self, a1, b12):
        b8 = []
        self.b3[a1] = 'intree'
        for edge in self.b6[a1]:
            self.b3[edge.b7] = 'fringe'
            self.b4[edge.b7] = edge.weight
            self.fonk3(b8, edge.b7, edge.weight)
            self.b5[edge.b7] = a1
        while b8:
            current_bandwidth, b9 = self.fonk4(b8)
            if b9 = = b12:
                break
            self.b3[b9] = 'intree'
            for edge in self.b6[b9]:
                b10 = min(current_bandwidth, edge.weight)
                if self.b3[edge.b7] == 'unseen':
                    self.b3[edge.b7] = 'fringe'
                    self.b4[edge.b7] = b10
                    self.b5[edge.b7] = b9
                    self.fonk3(b8, edge.b7, b10)
                elif self.b3[edge.b7] == 'fringe' and self.b4[edge.b7] < b10:
                    self.b4[edge.b7] = b10
                    self.b5[edge.b7] = b9
                    self.fonk3(b8, edge.b7, b10)
        return self.fonk6(b12), self.b4[b12]
    def fonk6(self, b12):
        b11 = []
        while b12 is not None:
            b11.append(b12)
            b12 = self.b5[b12]
        return b11[::-1]
if b13 = = "__main__":
    b2 = 5000
    b14 = class1(b2)
    a1 = 0
    b12 = 4999
    max_bw_path, b4 = b14.fonk5(a1, b12)
    print(f"Maximum bandwidth b11: {max_bw_path}")
    print(f"Maximum bandwidth: {b4}")