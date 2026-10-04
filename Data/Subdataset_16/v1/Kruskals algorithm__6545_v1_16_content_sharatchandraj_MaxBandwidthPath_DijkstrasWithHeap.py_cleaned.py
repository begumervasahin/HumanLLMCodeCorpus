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
    def fonk2(self, u, b9, weight):
        self.b6[u].append(b1(b7 = b9, weight=weight))
        self.b6[b9].append(b1(b7 = u, weight=weight))
    def fonk3(self, b8, b7, weight):
        heapq.heappush(b8, (-weight, b7))
    def fonk4(self, b8):
        weight, b7 = heapq.heappop(b8)
        return -weight, b7
    def fonk5(self, a2, b11):
        b8 = []
        self.b3[a2] = 'intree'
        for edge in self.b6[a2]:
            self.b3[edge.b7] = 'fringe'
            self.b4[edge.b7] = edge.weight
            self.fonk3(b8, edge.b7, edge.weight)
            self.b5[edge.b7] = a2
        while b8:
            max_weight, b9 = self.fonk4(b8)
            if b9 = = b11:
                break
            self.b3[b9] = 'intree'
            for edge in self.b6[b9]:
                if self.b3[edge.b7] == 'unseen':
                    self.b3[edge.b7] = 'fringe'
                    self.b5[edge.b7] = b9
                    self.b4[edge.b7] = min(max_weight, edge.weight)
                    self.fonk3(b8, edge.b7, self.b4[edge.b7])
                elif self.b3[edge.b7] == 'fringe' and self.b4[edge.b7] < min(max_weight, edge.weight):
                    self.b5[edge.b7] = b9
                    self.b4[edge.b7] = min(max_weight, edge.weight)
                    self.fonk3(b8, edge.b7, self.b4[edge.b7])
        return self.fonk6(b11), self.b4[b11]
    def fonk6(self, b11):
        b10 = []
        while b11 is not None:
            b10.append(b11)
            b11 = self.b5[b11]
        b10.reverse()
        return b10
if b12 = = "__main__":
    a1 = 5000
    b13 = class1(a1)
    a2 = 0
    b11 = 4999
    max_bw_path, b14 = b13.fonk5(a2, b11)
    print(f"Maximum bandwidth b10: {max_bw_path}")
    print(f"Maximum bandwidth: {b14}")