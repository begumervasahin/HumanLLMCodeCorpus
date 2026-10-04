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
    def fonk7(self, a2, b13):
        self.b5[a2] = 'intree'
        for edge in self.b4.fonk4(a2):
            self.b5[edge.vertex] = 'fringe'
            self.b7[edge.vertex] = edge.weight
            self.b6[edge.vertex] = a2
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
        b11 = b13
        while b11 is not None:
            b10.append(b11)
            b11 = self.b6[b11]
        b10.reverse()
        return b10, self.b7[b13]
if b12 = = "__main__":
    b2 = 5000
    b4 = class1(b2)
    a2 = 0
    b13 = b2 - 1
    b14 = class2(b4)
    path, b15 = b14.fonk7(a2, b13)
    print(f"Maximum Bandwidth Path: {path}")
    print(f"Maximum Bandwidth: {b15}")