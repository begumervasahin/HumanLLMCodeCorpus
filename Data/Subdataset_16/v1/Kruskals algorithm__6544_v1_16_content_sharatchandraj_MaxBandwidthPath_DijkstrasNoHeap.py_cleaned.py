from collections import namedtuple
b1 = namedtuple('b1', ['vertex', 'weight'])
class class1:
    def fonk1(self, b2):
        self.b2 = b2
        self.b3 = {i: [] for i in range(b2)}
    def fonk2(self, u, b9, weight):
        self.b3[u].append(b1(b9, weight))
        self.b3[b9].append(b1(u, weight))
    def fonk3(self):
        return list(self.b3.keys())
    def fonk4(self, u):
        return self.b3[u]
class class2:
    def fonk5(self, b4):
        self.b4 = b4
        self.b2 = b4.b2
        self.b5 = ['unseen'] * self.b2
        self.b6 = [None] * self.b2
        self.b7 = [0] * self.b2
    def fonk6(self):
        a1 = 0
        b8 = None
        for i in range(self.b2):
            if self.b5[i] == 'fringe' and self.b7[i] > a1:
                a1 = self.b7[i]
                b8 = i
        return b8
    def fonk7(self, a3, a4):
        self.b5[a3] = 'intree'
        for edge in self.b4.fonk4(a3):
            self.b5[edge.vertex] = 'fringe'
            self.b7[edge.vertex] = edge.weight
            self.b6[edge.vertex] = a3
        while 'fringe' in self.b5:
            b9 = self.fonk6()
            if b9 is None:
                break
            self.b5[b9] = 'intree'
            for edge in self.b4.fonk4(b9):
                if self.b5[edge.vertex] == 'unseen':
                    self.b5[edge.vertex] = 'fringe'
                    self.b6[edge.vertex] = b9
                    self.b7[edge.vertex] = min(self.b7[b9], edge.weight)
                elif self.b5[edge.vertex] == 'fringe' and self.b7[edge.vertex] < min(self.b7[b9], edge.weight):
                    self.b6[edge.vertex] = b9
                    self.b7[edge.vertex] = min(self.b7[b9], edge.weight)
        b10 = []
        b11 = a4
        while b11 is not None:
            b10.append(b11)
            b11 = self.b6[b11]
        b10.reverse()
        return b10, self.b7[a4]
if b12 = = "__main__":
    a2 = 5000
    b4 = class1(a2)
    a3 = 0
    a4 = 4999
    b13 = class2(b4)
    path, b14 = b13.fonk7(a3, a4)
    print(f"Maximum Bandwidth Path: {path}")
    print(f"Maximum Bandwidth: {b14}")